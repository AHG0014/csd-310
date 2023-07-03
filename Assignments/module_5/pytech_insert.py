from pymongo import MongoClient
import readchar
url = "mongodb+srv://admin:admin@cluster0.xojcllv.mongodb.net/"
client = MongoClient(url)
db = client.pytech
#three students

fred = {
    "first_name" : "Fred",
    "last_name" : "Fernandez",
    "student_id" : "1007",
}
sally = {
    "first_name" : "Sally",
    "last_name" : "Smith",
    "student_id" : "1008",
}
billy = {
    "first_name" : "Billy",
    "last_name" : "Boston",
    "student_id" : "1009",
}
students = db.students
print("\n  -- INSERT STATEMENTS --")
fred_student_id = students.insert_one(fred).inserted_id
print("  Inserted student record Fred Fernandez into the students collection with document_id " + str(fred_student_id))
sally_student_id = students.insert_one(sally).inserted_id
print("  Inserted student record Sally Smith into the students collection with document_id " + str(sally_student_id))
billy_student_id = students.insert_one(billy).inserted_id
print("  Inserted student record Sally Smith into the students collection with document_id " + str(billy_student_id))
print("\n\n\nEnd of program, press any key to exit...")
k = readchar.readchar()








 
