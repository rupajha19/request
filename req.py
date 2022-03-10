import requests
import json
get_url=requests.get("https://api.merakilearn.org/courses")
meraki_data=get_url.json()
with open("course.json","w") as file_data:
    json.dump(meraki_data,file_data,indent=4)
read_data=open("course.json","r")
read=read_data.read()
data=json.loads(read)
print()
i=0
while i<len(data):
    print(str(i+1)+".",data[i]["name"],data[i]["id"])
    i+=1
coures_no=int(input("enter which course number you want::"))
print(data[coures_no-1]["name"],data[coures_no-1]["id"])
print()
a=data[coures_no-1]["name"]+"_"+data[coures_no-1]["id"]+".json"
get_url_2=requests.get("http://api.merakilearn.org/courses/"+data[coures_no-1]["id"]+"/exercises")
meraki_data_2=get_url_2.json()
with open(a,"w") as file_data_2:
    json.dump(meraki_data_2,file_data_2,indent=4)
r=open(a,"r")
read=r.read()
data=json.loads(read)
i=0
while i<len(data["course"]["exercises"]):
    print(str(i+1)+".",data["course"]["exercises"][i]["name"])
    i+=1
topic=int(input("enter which topic you want::"))
topic-=1
i=0
while i<len(data["course"]["exercises"][topic]["content"]):
    print(data["course"]["exercises"][topic]["content"][i]["value"])
    print()
    i+=1
while topic<=len(data["course"]["exercises"]):
    p_n=input("enter which you want previous or next>>p/n::")
    if p_n=="p": 
        topic-=1
        if p_n=="p" and topic>1:
            print(data["course"]["exercises"][topic]["name"],"/n")
            i=0
            while i<len(data["course"]["exercises"][topic]["content"][i]["value"]):
                print(data["course"]["exercises"][topic]["content"]["value"])
                i+=1
        else:
            i=0
            while i<len(data):
                print(str(i+1),data["course"]["exercises"][i]["name"])
                i+=1
    elif p_n=="n":
        topic+=1
        if p_n=="n" and topic<len(data["course"]["exercises"]):
            print(data["course"]["exercises"][topic]["name"],"/n")
            i=0
            while i<len(data["course"]["exercises"][topic]["content"]):
                print(data["course"]["exercises"][topic]["content"][i]["value"])
                i+=1   
            break
                



































