import zipfile
import os
from pathlib import Path

c = Path.cwd()
link = c / 'Python_Scripts' / 'ORGANIZING'

file = 'resumes.zip'
text_file = 'test.txt'

zip_file = link / file

write_file = link / text_file

newZip = zipfile.ZipFile(zip_file, 'w')
newZip.write(write_file, compress_type=zipfile.ZIP_DEFLATED)
newZip.close()