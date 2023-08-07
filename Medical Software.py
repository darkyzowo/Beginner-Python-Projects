#You are developing software for a medical device that informs patients about their blood sugar level.


#glucose_level = 60 // low
#glucose_level = 100 // normal
#glucose_level = 150 // high 

glucose_level = int(input())

if glucose_level <= 60:
    print("Low glucose level")
   
elif glucose_level <=100:
    print("Normal range")
    
elif glucose_level <=150:
    print("High glucose level")