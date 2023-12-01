
import requests

BASE_URL = "http://localhost:9001"
model_id= "solvent-level"
res = requests.post(
	f"{BASE_URL}/{model_id}?"
	+"&".join(
		[
			f"api_key={pKCEf1sGVJg10T4haShH}",
			f"confidence={50}",
			f"overlap={50}",
			f"image={pic_1L_285.jpg}",
			f"max_detections={4}",
		]
	)
)

print(res.json())
