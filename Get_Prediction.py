
import subprocess

import json

 

cmd = "base64 pic_1L_327.jpg | curl -d @- https://detect.roboflow.com/solvent-level/2?api_key=pKCEf1sGVJg10T4haShH"

 

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
    height = jsonData["predictions"][pred]["y"]
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
		solvent_height = jsonData["predictions"][heights]["y"]
solvent_height=solvent_height*0.126
vol=250
if bottle_type == 1:
	vol = 1361- (2.61*solvent_height) - (0.00257*(solvent_height**2))
if bottle_type == 5:
	vol = 990 - (1.9*solvent_height) - (0.002*(solvent_height**2))
if bottle_type == 2:
	vol  = 2488 - (5.33*solvent_height) - (0.0025*(solvent_height**2))	
#vol = 1490.8378-3.8065466*solvent_height
print(vol) 
print(jsonData) 

