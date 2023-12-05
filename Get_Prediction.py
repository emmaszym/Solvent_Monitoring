
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

#print(jsonData) 
