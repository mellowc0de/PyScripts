#!/usr/bin/python3

import subprocess

result = subprocess.run(["[ -f /var/run/reboot-required ]"], shell=True)


print("Return code: ", result.returncode)
print("STDOUT: ", result.stdout)
print("STDERR: ", result.stderr)

print(result)

if result.returncode == 0:
    subprocess.run(["sudo reboot"], shell=True)
else:
    subprocess.run(["sleep 5"], shell=True)  
    print("No Reboot Required")
