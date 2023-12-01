#Calculate the volume in the bottle given the height taken by roboflow

bottle_size = input("Size of Bottle?")
height = float(input("What is the solvent height?"))

if bottle_size== '500':
	diameter=86
elif bottle_size == '1000':
	diameter=100
elif bottle_size == '2000':
	diameter=120
else: 
	print('Invalid Bottle Size')
	bottle_size = input("Size of bottle?")
if bottle_size  == '1000':
	volume= 1490.8378-3.8065466*height
#volume = (diameter/2)*height
print ("The volume is: ", volume )

