# Import necessary python libraries
import requests
import time
import mimetypes
mimetypes.init()

# Specify variables for use in script below
api_base_url = 'https://app.butlerlabs.ai/api'

# Make sure to add the API Key you wrote down above to the auth headers
api_key = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJnb29nbGUtb2F1dGgyfDEwMzQ4ODc1Mjk1MDk3NTIzNjUxMCIsImVtYWlsIjoiamFuZWxsZWFzYXVuZGVyc0BnbWFpbC5jb20iLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwiaWF0IjoxNjUwMTMwNjQ4MDYzfQ.XecBqSrZ6-SdxMQWTvlYjFTAk43TQQOo0o-5t0MeBtg'
auth_headers = {
    'Authorization': f'Bearer {api_key}'
}

# Use the Queue API Id you grabbed earlier
queue_id = '72405e3e-7f76-4321-904a-d12becdc9bef'

# Specify the path to the file you would like to process
file_location = '/path/to/file'

# Specify the API URL
upload_url = f'{api_base_url}/queues/{queue_id}/uploads'

# Prepare file for upload
file = open(file_location, 'rb')
mime_type = mimetypes.guess_type(file_location)[0]

# If you want to upload more files, you can simply add them to this array
files_to_upload = [('files', (file_location, file, mime_type))]

# Upload file to api
print(f'Uploading {file} to Butler for processing')
upload_json = requests.post(upload_url, headers=auth_headers, files=files_to_upload).json()

file.close()

extraction_results_url = f'{api_base_url}/queues/{queue_id}/extraction_results'

# Prepare query parameters
upload_id = upload_json['uploadId']
params = { 'uploadId': upload_id }

# Poll on extraction results until the extraction job has completed
extraction_results = {'documentStatus': 'UploadingFile'}
while extraction_results['documentStatus'] != 'Completed':
    results_json = requests.get(
        extraction_results_url,
        headers=auth_headers,
        params=params
    ).json()

    # items contains the list of extraction results for all documents you
    # uploaded. For this guide, we'll assume you only uploaded a single doc
    extraction_results = results_json['items'][0]
    status = extraction_results['documentStatus']

    if status != 'Completed':
        print('Upload still processing. Sleeping for 10 seconds...')
        time.sleep(10)
    else:
        print('Uploaded complete. Extraction results ready')

# Print out the extraction results
file_name = extraction_results['fileName']
print(f'\nExtracted data from {file_name}:')

fields = extraction_results['formFields']
for field in fields:
    field_name = field['fieldName']
    extracted_value = field['value']

    print(f'{field_name}: {extracted_value}')
