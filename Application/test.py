import pymongo
import pprint
import params as p

ziad = p.ZIAD_IP
mehdi = p.MEHDI_IP
rayane= p.RAYANE_IP

db_name : str = "mydatabase"

myclient = pymongo.MongoClient(f"mongodb://{mehdi}:{p.MEHDI_P}/")


collist = myclient.list_database_names()
if db_name in collist:
  myclient.drop_database(db_name)
  

mydb = myclient.Games
mycol = mydb.Magasin
for i in mycol.find({},{}):
  pprint.pprint(i)
  
  """
  
  
mylist = [
  { "name": "Amy", "address": "Apple st 652"},
  { "name": "Hannah", "address": "Mountain 21"},
  { "name": "Michael", "address": "Valley 345"},
  { "name": "Sandy", "address": "Ocean blvd 2"},
  { "name": "Betty", "address": "Green Grass 1"},
  { "name": "Richard", "address": "Sky st 331"},
  { "name": "Susan", "address": "One way 98"},
  { "name": "Vicky", "address": "Yellow Garden 2"},
  { "name": "Ben", "address": "Park Lane 38"},
  { "name": "William", "address": "Central st 954"},
  { "name": "Chuck", "address": "Main Road 989"},
  { "name": "Viola", "address": "Sideway 1633"}
]


x= mycol.insert_many(mylist)
for i in mycol.find({ "address": for i in mycol.find({},{}).sort("address",-1):
  pprint.pprint(i){"$regex": "^S"}}).sort("name",-1):
  pprint.pprint(i)
  
print("-----------------------")
x= mycol.delete_many({ "address": {"$regex": "^S"} })

for i in mycol.find({},{}).sort("address",-1):
  pprint.pprint(i)
print(x.deleted_count, " documents deleted.") 

mydb.list_collection_names()  
  
  """
