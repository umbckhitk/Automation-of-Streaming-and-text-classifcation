from flask import Flask, render_template
from pymongo import MongoClient

app = Flask(__name__)

# Replace with your MongoDB connection string
mongo_uri = "mongodb+srv://pd15494:test1234@cluster0.7aqxfxw.mongodb.net/"
client = MongoClient(mongo_uri)
db = client.get_database("ChatgptTweets")
collection = db.get_collection("Tweets")
print(collection)
app = Flask(__name__ , template_folder = "templates")

@app.route('/index')
def index(data=None):
    # Retrieve data from MongoDB
    data = collection.find()
    print(data)
    # Render the template with data
    return render_template('index.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)
