from pymongo import MongoClient
import readchar

# set the URL to connect to MongoDB
url = "mongodb+srv://admin:admin@cluster0.xojcllv.mongodb.net/" 

# creating a client instance
client = MongoClient(url)

# reference the pytech database
db = client.pytech

# reference students collection
students = db.students

# finding class list
class_list = students.find({})

print("\n  -- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY -- \n")

# printing information about students in class
for doc in class_list:
        print("\n  Student ID: " + doc["student_id"] + "\n  First Name: " + doc["first_name"] + "\n  Last Name: " + doc["last_name"] + "\n")

# call the update one method
result = db.students.update_one({"student_id": "1007"}, {"$set": {"last_name": "Smith"}})

# get student 1007
fred = students.find_one({"student_id": "1007"})

# print information about that student
print("\n  -- DISPLAYING STUDENT DOCUMENT 1007 --")
print("  Student ID: " + fred["student_id"] + "\n  First Name: " + fred["first_name"] + "\n  Last Name: " + fred["last_name"] + "\n")
print("\n\n\nEnd of program, press any key to exit...")

# end command line program
k = readchar.readchar()
