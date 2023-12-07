import time 

import subprocess

import os

from subprocess import DEVNULL

import json

import datetime

from gpiozero import LED

from gpiozero import Buzzer

buzzer = Buzzer(17)
led = LED(27)
strip = LED(22)
strip.on()
os.environ["LIBCAMERA_LOG_LEVELS"] = "3" 
i = 1

while i < 100:

	current_time = datetime.datetime.now()

	filename = f"pic_{current_time.day}_{current_time.hour}_{current_time.minute}_{current_time.second}.jpg"
	cmd1 = f"libcamera-jpeg -o {filename}"
	subprocess.Popen(cmd1,shell=True, stdout=DEVNULL)
	time.sleep(10)

#	cmd = f"base64 {filename} | curl -d @- https://detect.roboflow.com/solvent-level/2?api_key=pKCEf1sGVJg10T4haShH"
	cmd = f"base64 {filename} | curl -d @- https://detect.roboflow.com/solvent-level-2/1?api_key=pKCEf1sGVJg10T4haShH"

 

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
		what_found = jsonData["predictions"][pred]["class"]
		conf_percent=round(conf*100, 1)
		print(f"    Prediction {pred+1}: {what_found} at {conf_percent}% Confidence")

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
			#print("No bottle  found")
			continue
	for heights in range(predictions):
		if jsonData["predictions"][heights]["class_id"] == 3:
			solvent_height = jsonData["predictions"][heights]["y"]
	solvent_height=solvent_height*0.126

	if bottle_type == 1:
		vol = 1361- (2.61*solvent_height) - (0.00257*(solvent_height**2))
		if vol < 200:
			led.on()
			buzzer.on()
			time.sleep(2)
			led.off()
			buzzer.off() 
	if bottle_type == 5:
		vol = 990 - (1.9*solvent_height) - (0.002*(solvent_height**2))
		if vol < 125:
			led.on()
			buzzer.on()
			time.sleep(2)
			led.off()
			buzzer.off() 
	if bottle_type == 2:
		vol  = 2488 - (5.33*solvent_height) - (0.0025*(solvent_height**2))	
		if vol < 400:
			led.on()
			buzzer.on()
			time.sleep(2)
			led.off()
			buzzer.off() 
#vol = 1490.8378-3.8065466*solvent_height
	round_vol=round(vol,1)
	print(f" The volume is {round_vol} mL")
	vol=0
	round_vol=0
	solvent_height=0
	bottle_type=-1
	i += 1
	time.sleep(10)
