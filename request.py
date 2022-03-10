import requests
import json
get_url=requests.get("https://api.merakilearn.org/courses")
meraki_data=get_url.json()
with open("course.json","w") as file_data:
    file=json.dump(meraki_data,file_data,indent=4)
serial=1 
for i in meraki_data:
    print(serial,".",i["name"],".",i["id"])
    serial+=1
course_no=int(input("Enter which course you want::"))
print(meraki_data[course_no-1]["name"])
id=(meraki_data[course_no-1]["id"])
get_url_2=requests.get("http://api.merakilearn.org/courses/"+str(id)+"/exercises")
# print(get_url)
var=get_url_2.json()
with open("data.json","w") as a:
   file_2= json.dump(var,a,indent=4)
serial2=1
list1=[]
list2=[]
for j in var["course"]["exercises"]:
    if j["parent_exercise_id"]==None:
        print(serial2,j["name"])
        print(" ",serial2,j["slug"])
        serial2+=1
        new_number=1
        list1.append(j)
        list2.append(j)
        continue
    if j["parent_exercise_id"]==j["id"]:
        print(serial2,j["name"])
        serial2+=1
        new_number=1
        list1.append(j)
    for l in var["course"]["exercises"]:
        if j["parent_exercise_id"]!=j["id"]:
            print(" ",new_number,j["name"])
            new_number+=1
            list2.append(j)
            break
p_n=input("enter you want previous or next.....(n/p):")
if p_n=="p":
    serial=1
    for i in meraki_data:
        print(serial,".",i["name"],i["id"])
        serial+=1
    course_no=int(input("Enter which number you want::"))
    print(meraki_data[course_no-1]["name"])
    id=(meraki_data[course_no-1]["id"])
    get_url_2=requests.get("http://api.merakilearn.org/courses/"+str(id)+"/exercises")
    var=get_url_2.json()
    with open("topic.json","w") as a:
        json.dump(var,a,indent=4)
        serial2=1
        list1=[]
        list2=[]
    for j in var["course"]["exercises"]:
        if j ["parent_exercise_id"]==None:
            print(serial2,j["name"])
            print(" ",serial2,j["slug"])
            serial2+=1
            new_number=1
            list1.append(j)
            list2.append(j)
            continue
        if j["parent_exercise_id"]==j["id"]:
            print(serial2,j["name"])
            serial2+=1
            new_number=1
            list1.append(j)
        for l in var["course"]["exercises"]:
            if j["parent_exercise_id"]!=j["id"]:
                print(" ",new_number,j["name"])
                new_number+=1
                list2.append(j)
                break
            with open("topic1.json","w") as f:
                json.dump(list1,f,indent=4)
                parent=int(input("enter which parent exercise you want::"))
                for b in list1:
                    if b["parent_exercise_id"]==b["id"]:
                        print(list1[parent-1]["name"])
                        num=(list1[parent-1]["id"])
                        var1=[]
                        var2=[]
                        new_number2=1
                        for n in list2:
                            if n["parent_exercise_id"]==num:
                                print(" ",new_number2,n["name"])
                                var1.append(n["name"])
                                var2.append(n["content"])
                                new_number2+=1
                        child=int(input("enter the child exercise you want:: "))
                        new_number2=1
                        for s in range(0,len(var)):
                            if child==new_number2:
                                print(var1[s])
                                print(var2[s])
                            new_number2+=1
elif p_n=="n":
    with open("topic1.json","w") as f:
        json.dump(list1,f,indent=4)
        parent=int(input("enter parents excersie you want::"))
        print(list1[parent-1]["name"])
        for k in list1:
            if k["parent_exercise_id"]:
                num=(k[parent-1]["id"])
                var1=[]
                var2=[]
                new_number2=1
                for n in list2:
                    if n["parent_exercise_id"]==num:
                        print(" ",new_number2,n[parent-1]["name"])
                        var1.append(n["course_no"])
                        var2.append(n["content"])
                        new_number2+=1
                        child=int(input('enter child exercise you want::'))
                        new_number2=1
                        for e in range(0,len(var)):
                            if child==new_number2:
                                print(var1[e])
                                print(var2[e])
                            new_number2+=1










