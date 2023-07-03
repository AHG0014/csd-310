from pymongo import MongoClient
import readchar
url = "mongodb+srv://admin:admin@cluster0.xojcllv.mongodb.net/"
client = MongoClient(url)
db = client.pytech
students = db.students
class_list = students.find({})
print("\n  -- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")
for doc in class_list:
        print("  Student ID: " + doc["student_id"] + "\n  First Name: " + doc["first_name"] + "\n  Last Name: " + doc["last_name"] + "\n")
fred = students.find_one({"student_id": "1007"})
print("\n\n -- DISPLAYING STUDENT DOCUMENT FROM find_one() QUERY --")
print("  Student ID: " + fred["student_id"] + "\n  First Name: " + fred["first_name"] + "\n  Last Name: " + fred["last_name"] + "\n")
print("\n\n\nEnd of program, press any key to exit...")
k = readchar.readchar()



