from pymongo import MongoClient
import readchar
# Connect to MongoDB
url = "mongodb+srv://admin:admin@cluster0.xojcllv.mongodb.net/"
# Creating a client instanse

client = MongoClient(url)
# refrence the pytech database

db = client.pytech
#reference the student database

students = db.students 
# importing the student class list

class_list = students.find({})
# Students

print("\n  -- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY -- \n")

for doc in class_list:
    print("  Student ID: " + doc["student_id"] + "\n  First Name: " + doc["first_name"] + "\n  Last Name: " + doc["last_name"] + "\n")

student_test = {
    "student_id": "1010",
    "first_name": "John",
    "last_name": "Doe"
}
# Entering the student into the 

student_test_id = students.insert_one(student_test).inserted_id

#Insert statements and output 
print("\n  -- INSERT STATEMENTS --")
print("  Inserted student record into the students collection with document_id " + str(student_test_id))

#Find student with ID 1010

student_test_find = students.find_one({"student_id": "1010"})

#Displaying results

print("\n  -- DISPLAYING STUDENT TEST Find -- ")
print("  Student ID: " + student_test_find["student_id"] + "\n  First Name: " + student_test_find["first_name"] + "\n  Last Name: " + student_test_find["last_name"] + "\n")

# calling the delete one method and it will remove student test find

deleted_student_test_find = students.delete_one({"student_id": "1010"})

#finding all students and new list.

new_student_list = students.find({})

print("\n  -- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")

for doc in class_list:
    print("  Student ID: " + doc["student_id"] + "\n  First Name: " + doc["first_name"] + "\n  Last Name: " + doc["last_name"] + "\n")

#exit statement 
print("\n\n\nEnd of program, press any key to exit...")
k = readchar.readchar()






