import pymongo

client = pymongo.MongoClient("mongodb+srv://khushbu:shahare#30@khushbu.rqfekah.mongodb.net/?retryWrites=true&w=majority")
db = client.test

data = {
    "name" : "harshal",
    "email_id" : "harshahare@77gmail.com",
    "subjects_name" : ["physic", "math" , 'computer science']
}

database = client["harsh_info"]
collection2 = database['yogi']
collection2.insert_one(data)

record = collection2.find()
for i in record :
    print(i)