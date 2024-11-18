from pymongo import MongoClient

client = MongoClient("mongodb+srv://2406363:Joel1234@dbtest.vqz9n.mongodb.net/toolsDB?retryWrites=true&w=majority")
db = client.toolsDB
comments_collection = db.comments

toolID = int(input("Enter tool ID: "))
user = input("Enter user name: ")
rating = int(input("Enter tool rating: "))
comment = input("Enter a comment about the tool: ")

# Test insertion
comment_data = {
    "tool_id": toolID, # "64abcd1234ef567890123456" # Replace with a valid ObjectId string from your tools collection
    "user": user, # "Test User"
    "rating": rating, # 5
    "comment": comment # "This is a test comment"
}

# Insert a comment to create the collection if it doesn’t exist
result = comments_collection.insert_one(comment_data)
print(f"Inserted comment ID: {result.inserted_id}")