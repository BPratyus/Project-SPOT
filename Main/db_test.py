import pymongo
import pytz
import Scene_detection

#Connect to Database
myclient=pymongo.MongoClient("mongodb://localhost:27017/")
db=myclient["capstone"]
col=db["camera_log"]

# x=col.insert_one(mydict)
# x=col.insert_many(myList)
# {},{"_id":0,"name":1,"address":1}

#Create a unique list
unique_cls=[]

def find(object_name:str):
    gen_time = None
    id = None
    doc=col.find({'name':object_name}).sort('_id',-1).limit(1)

    for x in doc:
        gen_time=x.get('_id').generation_time
        id=x['_id']

    if id:
       prev_docs = col.find({
                '_id': {'$lt': id},
        # '$and':[{'class':{'$ne':0}},{'name':{'$ne':object_name}}]
       }).limit(50)


       for x in prev_docs:
           if x['name'] not in unique_cls:
                unique_cls.append(x['name'])
       print(unique_cls)
       scene=Scene_detection.detect_scene(unique_cls)
       print(scene)


       ist = gen_time.astimezone(pytz.timezone('Asia/Kolkata'))
       time= ist.strftime("%d-%m-%Y %I:%M:%S %p")

       # print(id)
       return f"The {object_name} was last seen in {scene} at {time} "
    else:
        # print("not found")
        return None
from datetime import datetime

# Define the UTC time
# utc_time = datetime.strptime(time, "%Y-%m-%d %H:%M:%S%z")

# Convert to IST
# print(find('laptop'))

    # Print the IST time
    # print()
