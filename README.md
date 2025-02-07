# Automation using streaming data and text classification ML 



<img width="964" alt="Screenshot 2023-12-03 at 7 52 58 PM" src="https://github.com/umbckhitk/691-data-intensive-/assets/105472386/d66850b9-5ea6-40d0-af90-17db65b099c8">




# Project Definition: ChatGPT Tweet Analysis Pipeline

## Project Goal:
### The goal of this project is to develop an end-to-end data analysis pipeline for real-time sentiment analysis of tweets using OpenAI's ChatGPT. The pipeline involves data ingestion from a Kaggle dataset containing tweets, streaming the data to a Kafka topic, processing and analyzing the tweets using Apache Spark, applying sentiment analysis with Natural Language Processing (NLP) techniques, storing the results in MongoDB, and presenting the findings through a Flask-based web application.

## Requirements:

## Functional Requirements:

## Data Ingestion:

 The system must ingest data from a Kaggle dataset in CSV format containing tweets.
Data must be sent to a Kafka topic at regular intervals (every 3 seconds) using a Kafka producer.
### Kafka Setup:

Configure and create Kafka brokers with the appropriate number of partitions.
Create a Kafka topic named "chatgpt_tweets" for tweet ingestion and "chatgpt_analysis_results" for storing analysis outcomes.
Kafka Consumer:

Develop a Kafka consumer in Python to subscribe to the "chatgpt_tweets" topic and receive tweets in real-time.

### Spark Kafka Integration:

Establish a Spark session to read and process the tweet stream from the Kafka topic.
Apply data transformations and utilize an NLP library for sentiment analysis on each tweet.
Write the analyzed results back to a Kafka topic named "chatgpt_analysis_results."
Flask Application:

Develop a Flask-based web application to display tweets and sentiment analysis results.
The application should provide real-time updates from the Kafka topic.
MongoDB Integration:

Use MongoDB as a NoSQL database to store both raw tweets and sentiment analysis results.
Develop functionality to query and retrieve data from MongoDB.
Non-Functional Requirements:

### Performance:

The pipeline should handle a high volume of tweets and provide low-latency real-time analysis.
Spark processing should be optimized for efficiency.

### Scalability:

The system should be designed to scale horizontally to accommodate increased data volume.
Kafka and Spark configurations should be adjustable for scalability.

### Reliability:

The pipeline should be robust and handle potential failures gracefully.
Implement mechanisms for error handling and recovery in case of system interruptions.

### Security:

Implement secure communication protocols for data transmission between components.
Ensure proper authentication and authorization for accessing Kafka, Spark, and MongoDB.

### Usability:

The Flask web application should have an intuitive user interface for easy interaction.
Provide appropriate logging and monitoring tools for system administrators.

### Maintainability:

Code should be well-documented, modular, and follow best practices.
Implement version control and continuous integration for ease of maintenance.

### Architecture Requirements:

The system should follow a microservices architecture with loosely coupled components.
Use containerization (e.g., Docker) for deploying and managing components.
Choose appropriate technologies for each component, considering interoperability and ease of integration.
By adhering to these functional and non-functional requirements, the project aims to deliver a robust, scalable, and real-time sentiment analysis pipeline for tweets.


## Project Design:

### 1. Data Models:

### Raw Tweets:

A NoSQL document-oriented model will be employed to store raw tweets in MongoDB. Each tweet will be represented as a document with fields such as tweet ID, user ID, timestamp, and tweet content.

### Analysis Results:

The results of sentiment analysis will also be stored in MongoDB using a document-based model. Each analysis result will include tweet ID, sentiment score, and any additional metadata.

### 2. Data Encoding:

Tweets will be stored in their original text format in MongoDB, while analysis results can be stored using appropriate serialization formats like JSON.

### 3. Querying:

MongoDB's flexible querying capabilities will be leveraged for both raw tweets and sentiment analysis results.
Queries will be optimized for efficient retrieval based on tweet ID, timestamp, and sentiment score.

### 4. Configurations for Scalability:

Configured with multiple brokers to distribute the load.
Adequate partitioning of topics for parallel processing.
Configured in a cluster mode for parallel and distributed processing.
Adjust Spark executors and memory configurations for scalability.
Deployed in a sharded cluster to horizontally scale the database.
Appropriate indexing to enhance query performance.

### 5. Configurations for Reliability::

Replication factor set to ensure fault tolerance and high availability.
Appropriate acknowledgment settings to ensure data durability.

Fault-tolerant configurations, such as checkpointing, to recover from failures.
Monitoring and alerting for job failures.
Configured with replication to ensure data availability in case of node failures.
Regular backups and automated recovery processes.

### 6. Chosen NoSQL Database:

MongoDB is selected as the NoSQL database for its flexibility, scalability, and ease of integration with both Spark and Flask.
It allows for efficient storage and retrieval of JSON-like documents, fitting the structure of tweets and analysis results.

### 7. Data Warehouse (Optional):

Depending on the scale and need for historical data analysis, a data warehouse solution such as Amazon Redshift or Google BigQuery may be integrated.
The data warehouse can be used to store aggregated and historical analytics data for more complex querying and reporting.


## Project Architecture :

Img : Self made architecture image for reference 



### Using server for Kafla with 2 topics 
### Zookeeper started
### Chatgpt
### Chatgpt 2 
### Mongo db server connected. 
### Spark NLP server turned on that connects NLP for twitter analysis.
### Flask server at localhost: 5000

## 1. Kafka Deployment:
### 1.1 Zookeeper:
Ensure Zookeeper is running to coordinate the Kafka brokers.
Minimal configuration, typically no modifications needed for basic setups.
### 1.2 Kafka Broker Configuration:
Use server.properties to configure Kafka brokers.
zookeeper.connect: Zookeeper connection string.
### 1.3 Kafka Topics:
Create two topics: Chatgpt and Chatgpt2.
### 1.4 Kafka Producer :
### 1.5 Kafka Consumer:
## 2. Spark NLP Server:
### 2.1 Spark NLP Configuration:
Install and configure Apache Spark.
Configure Spark to connect to Kafka and MongoDB.
Key configurations:
Spark Kafka integration settings.
MongoDB connection settings.
### 2.1.Sentiment Analysis :
Tokenization  of the key words 
Lemmatizer 
Sentiment deduction 
## 3. MongoDB Deployment:
### 3.1 MongoDB Configuration:
Install and run MongoDB server.
Minimal configuration for local deployment.
### 3.2 MongoDB Data Model:
Use a document-based model for tweets and analysis results.
Example tweet document:
## 4. Flask Server:
### 4.1 Flask Configuration:
Install Flask and required dependencies.
Configure Flask to interact with Kafka for real-time updates.
## 5. Component Integration and Integration Tests:
Integration:
Ensure that Kafka producers are successfully sending tweets to the Chatgpt topic.
Confirm that the Spark NLP server can consume from the Chatgpt topic and perform sentiment analysis.
Verify that analysis results are correctly written to the Chatgpt2 topic.
Integration Tests:
Send sample tweets through the Kafka producer and verify their reception by the Kafka consumer.
Confirm that the Flask application displays real-time tweets from the Kafka topic.
Implementation Limitations

Endpoint Availability in Twitter API:
Description: The Twitter API offers limited free access to specific endpoints, restricting the ability to stream comprehensive data.
Impact: The project's data may not represent a diverse range of topics or capture the full scope of real-time Twitter conversations.
Mitigation: Explore options for obtaining premium access to Twitter API endpoints, keeping in mind associated costs.

### Project demo and codebase
### Git hub of Harish Krishnamoorthy - https://github.com/umbckhitk/691-data-intensive-/tree/main

### Git Hub  of Kavalakuntla Chakradhar- 
https://github.com/chakri0/seng691project

### Video presentation of Kavalakuntla Chakradhar
https://youtu.be/ipLdYbWBE_k

### Video presentation of Harish Krishnamoorthy - 
### https://youtu.be/HQ-o4CThWuI





# References
## Kafka:
Apache Kafka documentation: https://kafka.apache.org/20/documentation.html
Introduction to Apache Kafka: https://docs.confluent.io/kafka/introduction.html
## ZooKeeper:
Apache ZooKeeper documentation: https://zookeeper.apache.org/
ZooKeeper Explained: https://www.tutorialspoint.com/zookeeper/index.htm
## MongoDB:
MongoDB documentation: https://www.mongodb.com/docs/
MongoDB Tutorial: https://www.w3schools.com/mongodb/
## Spark NLP:
Spark NLP documentation: https://www.johnsnowlabs.com/importing-huggingface-models-into-spark-nlp/
Introducing Spark NLP for Natural Language Processing: https://medium.com/spark-nlp/spark-nlp-quickstart-tutorial-with-databricks-5df54853cf0a
## Flask:
Flask documentation: https://palletsprojects.com/
Flask Tutorial: https://realpython.com/python-web-applications-with-flask-part-i/
Real-time Data Processing:
Real-time Data Processing with Kafka Streams by Thomas Davidson, David P. Taylor, and Jacob Dean (2016)
Real-time Data Processing at Scale with Apache Kafka and Apache Spark Streaming by Kai Zheng, Xiaolin Jia, and Yunfei Gong (2017)
Natural Language Processing (NLP):
Natural Language Processing with Spark NLP: A Practical Guide by Yifan Yang (2021)
A Survey of Natural Language Processing Techniques for Sentiment Analysis by Dipanjan Sarkar and Sourav Chakrabarti (2017)
Topic Modeling for Text Analysis by David M. Blei (2012)

## Forums and Community Discussions:
Platforms like Stack Overflow and the official forums for each technology have been valuable for troubleshooting specific issues and learning from community discussions.
