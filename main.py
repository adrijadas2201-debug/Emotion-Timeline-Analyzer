from transformers import pipeline
import pandas as pd
import matplotlib.pyplot as mtb
import matplotlib.dates as mdates
from datetime import datetime , timedelta

#Takes user input 
message=[]

num=int(input("How many messages? "))

for i in range(num):
    msg=input(f'Enter the messages {i+1} : ')
    message.append(msg)


#loads the AI emotion model 
classify = pipeline('text-classification',model="j-hartmann/emotion-english-distilroberta-base")

#Predicts emotions
result = []
for msg in message:
    output = classify(msg)[0]
    result.append(output)



#Creates a table to the data 
dt = pd.DataFrame(result)


#Adds a column of original messages
dt["message"] = message


#Adds timeline in the table
start_time= datetime.now()
time=[]

for i in range(len(message)):
    time.append(start_time + timedelta(seconds= i*2))

dt["time"]=time
dt['time_display']= dt['time'].dt.strftime("%H:%M:%S")


pd.set_option('display.max_columns',None)
pd.set_option('display.width', 1000)
pd.set_option('display.expand_frame_repr', False)


#Display results
print('\n---------------Emotion Analysis-----------------\n')
print(dt)

#Plot emotion vs time graph
mtb.figure()
mtb.plot(dt["time"],dt["score"],linestyle="--",alpha=1)
mtb.gca().xaxis.set_major_formatter(mdates.DateFormatter('%H:%M:%S'))
mtb.title("Emotion Timeline Analysis")
mtb.xlabel("Time")
mtb.ylabel("Emotion score")
mtb.grid(alpha=0.8)
mtb.xticks(rotation=45)
mtb.tight_layout()
mtb.show()




