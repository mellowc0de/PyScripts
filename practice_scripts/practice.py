import os
from pathlib import Path

# Variable assignment to Path.home() -> Path.
homeFolder = Path.home()
subFolder = Path('Downloads')

p = homeFolder / subFolder

find = list(p.glob('hardwareSearchResults*.csv'))

for i in find:
    print('Starting file erasure!')
    print(i)
    os.unlink(i)
    print('Erasure complete!')
    print('-----------------------------------------------')
    i=+1
