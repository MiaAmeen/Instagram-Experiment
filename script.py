import os
import sys
import subprocess

if os.getcwd() == "/Users/destroyerofworlds/Documents/IG/Instagram-Experiment":
    pass
else:
    os.chdir("/Users/destroyerofworlds/Documents/IG/Instagram-Experiment")

accounts= {"repbotf_nc":"repbotf_nc123", "neutbot_nc":"neutbot_nc123"}
cmd= []
for key in accounts.keys():
    ID= key
    PASS= accounts[key]
    cmd.append("python accountManage.py " + ID + " " + PASS)

list_files = subprocess.run(cmd)
print("The exit code was: %d" % list_files.returncode)

#chdir Documents/IG/Instagram-Experiment
#python script.py
