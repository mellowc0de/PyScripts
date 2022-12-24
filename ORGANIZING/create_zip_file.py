import zipfile

newZip = zipfile.ZipFile('resumes.zip', 'w')
newZip.write('test.txt', compress_type=zipfile.ZIP_DEFLATED)
newZip.close()