from pymongo import MongoClient
import readchar

url = "mongodb+srv://admin:admin@cluster0.xojcllv.mongodb.net/"
client = MongoClient(url)
db = client.pytech

print(" -- Pytech C0llection List -- ")
print(db.list_collection_names())
print("\n\n\nEnd of program, press any key to exit...")
k = readchar.readchar()