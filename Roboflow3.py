from roboflow import Roboflow


rf = Roboflow(api_key="pKCEf1sGVJg10T4haShH")
version = rf.workspace("senior-design-gkxxz").project("solvent-level").version(1,local="http://localhost:9001/")

prediction = version.model.predict("/home/team127/Downloads/pic_1L_285.jpg")
print(prediction.json())
