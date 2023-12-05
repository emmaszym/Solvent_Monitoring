
import subprocess

import json

 

cmd = "base64 pic_1L_285.jpg | curl -d @- https://detect.roboflow.com/solvent-level/1?api_key=pKCEf1sGVJg10T4haShH"

 

def subprocess_cmd(command):

    result = []

    process = subprocess.Popen(command,stdout=subprocess.PIPE, shell=True)

    proc_stdout = process.communicate()[0].strip()

    for line in proc_stdout.decode().split('\n'):

        result.append(line)

    return result

 

output = subprocess_cmd(cmd)

jsonData = json.loads(output[0])

predictions = len(jsonData["predictions"])

print(f"Number of predictions: {predictions}")

for pred in range(predictions):

    conf = jsonData["predictions"][pred]["confidence"]
    height = jsonData["predictions"][pred]["height"]
    ccity = jsonData["predictions"][pred]["class_id"]

    print(f"    prediction {pred}: Confidence {conf} height {height} class_id {ccity}")

#Meniscus=3, 500mL=2, 1L=0, 2L=1
#getting bottle size
for entry in range(predictions):
	if jsonData["predictions"][entry]["class_id"] == 0:
		bottle_type=1
	elif jsonData["predictions"][entry]["class_id"] == 1:
		bottle_type=2
	elif jsonData["predictions"][entry]["class_id"] == 2:
		bottle_type=5
	else:
		continue
for heights in range(predictions):
	if jsonData["predictions"][heights]["class_id"] == 3:
		solvent_height = jsonData["predictions"][heights]["height"]

if bottle_type == 1:
	volume = 1490.8378-3.8065466*solvent_height
print(volume) 
#print(jsonData) 

