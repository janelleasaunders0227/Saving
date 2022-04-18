# Make sure to use the imports as well as api_key and auth_headers from Step 1
queue_id = '72405e3e-7f76-4321-904a-d12becdc9bef'
extraction_results_url = f'https://app.butlerlabs.ai/api/queues/{queue_id}/extraction_results'

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
print(f'Extracted data from {file_name}:')

fields = extraction_results['formFields']
for field in fields:
    field_name = field['fieldName']
    extracted_value = field['value']

    print(f'{field_name}: {extracted_value}')
