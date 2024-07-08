# Import necessary libraries
import pymongo

# Connect to MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["non_relational_data_model"]

# Define the collections
collections = ["channels", "videos", "playlists", "comments"]

# Task 1: Count of rows in each collection
for idx, collection in enumerate(collections, start=1):
    count = db[collection].count_documents({})
    print(f"Task 1: Count of rows in {collection}: {count}")
    print()

# Task 2: Show a sample of 3 documents from each collection
for idx, collection in enumerate(collections, start=1):
    sample_documents = db[collection].find().limit(3)
    print(f"Task 2: Sample documents from {collection}:")
    for i, document in enumerate(sample_documents, start=1):
        print(f"Document {i}: {document}")
    print()

# Task 3: Join two collections using local and foreign keys
# For example, if you have two collections 'channels' and 'videos' with a common key 'channel_id'
pipeline = [
    {
        "$lookup": {
            "from": "channels",
            "localField": "channel_id",
            "foreignField": "id",
            "as": "joined_data"
        }
    }
]

result = db.videos.aggregate(pipeline)

print("Task 3: Left Joining data between 'videos' and 'channels':")
for idx, doc in enumerate(result, start=1):
    print(f"Document {idx}: {doc}")
    print()

# Close the MongoDB connection
client.close()
