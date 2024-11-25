from pymongo import MongoClient

client = MongoClient("mongodb+srv://2406363:Joel1234@dbtest.vqz9n.mongodb.net/toolsDB?retryWrites=true&w=majority")
db = client.toolsDB
comments_collection = db.users

FirstName = input("Enter First name: ")
LastName = input("Enter Last name: ")
Email = input("Enter user name: ")
PhoneNo = int(input("Enter your phone Number: "))
Picture = input("Enter profile pic: ")
Password = input("Enter Password:  ")

# Test insertion
comment_data = {
    "fname": FirstName, # "64abcd1234ef567890123456" # Replace with a valid ObjectId string from your tools collection
    "lname": LastName,
    "email": Email, # "Test User"
    "phone": PhoneNo, # 5
    "picture": Picture,
    "password": Password # "This is a test comment"
}

# Insert a comment to create the collection if it doesn’t exist
result = comments_collection.insert_one(comment_data)
print(f"Inserted comment ID: {result.inserted_id}")
