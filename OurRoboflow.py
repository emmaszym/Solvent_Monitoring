
import requests

BASE_URL = "http://localhost:9001"
model_id= "solvent-level"
res = requests.post(
	f"{BASE_URL}/{model_id}?"
	+"&".join(
		[
			#"api_key=pKCEf1sGVJg10T4haShH",
			"api_key=rf_37btToay9PR1mjSRRieEDv91xV53",
			"confidence=50",
			"overlap=50",
			"image=pic_1L_285.jpg",
			"max_detections=4",
		]
	)
)

print(res.json())
