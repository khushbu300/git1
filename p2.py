import pymongo

client = pymongo.MongoClient("mongodb+srv://khushbu:shahare#30@khushbu.rqfekah.mongodb.net/?retryWrites=true&w=majority")
db = client.test

database = client['myinfo']
collection = database['khush']
#record = collection.find()
#for i in record :
 #   print(i)

data = collection.find({"k2" : "shahare"})

for i in data :
    print(data)