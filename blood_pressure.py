
systolic = int( input( "Enter your systolic blood pressure:"))

while 0 > systolic:
    print( "Can't be negative.")
    systolic = int( input( "Enter your systolic blood pressure:"))

while not(systolic >= 80 and systolic <= 120):
    systolic = 'abnormal'
    break

diastolic = int( input( "Enter your diastolic blood pressure:"))

while diastolic < 0:
    print( "Cant be negative.")
    diastolic = int( input( "Enter you diastolic blood pressure:"))
    
if diastolic < 60 or diastolic > 80:
    diastolic = 'abnormal'
    
if systolic != 'abnormal' and diastolic != 'abnormal':
    print ("Your blood pressure is normal.")
else:
    print ("Your blood pressure is abnormal."
           
    
    
    