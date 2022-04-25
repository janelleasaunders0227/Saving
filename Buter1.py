import cgi, os
import cgitb cgitb.enable() 
#print('content-type:text/html\r\n\r\n')

print('Hello, World!')

start_response('200 OK', [('Content-Type', 'text/html')])

print "<b> Hello, World</b>"
#form=cgi.FormStorage()
#pn=str(form.getvalue("pname"))
#des=str(form.getvalue("des"))
#fle=form['filename']

#fn=os.path.basename(fle.filename)
#open("/Users/janellesaunders/Desktop/ToothpasteApplication/tem"+fn,"wb").write(fle.file.read())

#print('<html>')
#print('<body><center>')
#print('<h1>Product Name\n(%s)</h1>'%pn)
#print('<img src=tem/%s>'%fn)
#print('<h2>%s</h2>'%des)
#print('</center></body></html>')