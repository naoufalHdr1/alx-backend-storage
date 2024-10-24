# 0x01. NoSQL
`#Back-end` `#NoSQL` `#MongoDB`

## Project Overview

This project focuses on the fundamentals of NoSQL databases, specifically MongoDB. It covers essential operations such as creating, querying, updating, and deleting documents within a MongoDB database. By the end of this project, you will gain a solid understanding of NoSQL concepts and how they differ from traditional SQL databases.

## Learning Objectives

By the end of this project, you should be able to explain the following concepts:

- What NoSQL means
- Differences between SQL and NoSQL
- What ACID stands for
- What document storage is
- Types of NoSQL databases
- Benefits of using a NoSQL database
- How to query information from a NoSQL database
- How to insert, update, and delete information in a NoSQL database
- How to use MongoDB

## Resources

For a successful completion of this project, you are encouraged to read or watch the following resources:

- [NoSQL Databases Explained](https://riak.com/resources/nosql-databases/)
- [What is NoSQL?](https://www.youtube.com/watch?v=qUV2j3XBRHc)
- [MongoDB with Python Crash Course - Tutorial for Beginners](https://www.youtube.com/watch?v=E-1xI85Zog8)
- [MongoDB Tutorial: Insert, Update, Remove, Query](https://www.youtube.com/watch?v=CB9G5Dvv-EE)
- [Aggregation in MongoDB](https://www.mongodb.com/docs/manual/aggregation/)
- [Introduction to MongoDB and Python](https://realpython.com/introduction-to-mongodb-and-python/)
- [Mongo Shell Methods](https://www.mongodb.com/docs/manual/reference/method/)
- [Mongosh Documentation](https://www.mongodb.com/docs/mongodb-shell/#mongodb-binary-bin.mongosh)

## Requirements

### MongoDB Command File

- All files must be interpreted/compiled on **Ubuntu 18.04 LTS** using **MongoDB (version 4.2)**.
- The first line of all files should be a comment: `// my comment`.

### MongoDB Installation Instructions

To install MongoDB 4.2 on Ubuntu 18.04, follow these commands:
```bash
$ wget -qO - https://www.mongodb.org/static/pgp/server-4.2.asc | apt-key add -
$ echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu bionic/mongodb-org/4.2 multiverse" > /etc/apt/sources.list.d/mongodb-org-4.2.list
$ sudo apt-get update
$ sudo apt-get install -y mongodb-org
$ sudo service mongod status
```

Verify the installation:
```bash
$ mongo --version
```
Install PyMongo:
```bash
$ pip3 install pymongo
```

## Project Tasks

This project consists of several tasks. Each task corresponds to a specific requirement for interacting with MongoDB:

### Task 0: List all databases

Create a script that lists all databases in MongoDB.
**File:** `0-list_databases`

### Task 1: Create a database

Create a script that creates or uses the database `my_db`.
**File:** `1-use_or_create_database`

### Task 2: Insert document

Create a script that inserts a document into the `school` collection with the attribute `name` set to "Holberton school".
**File:** `2-insert`

### Task 3: All documents

Create a script that lists all documents in the `school` collection.
**File:** `3-all`

### Task 4: All matches

Create a script that lists all documents with `name="Holberton school"` in the `school` collection.
**File:** `4-match`

### Task 5: Count

Create a script that displays the number of documents in the `school` collection.
**File:** `5-count`

### Task 6: Update

Create a script that adds a new attribute address with the value "972 Mission street" to all documents with `name="Holberton school"`.
**File:** `6-update`

### Task 7: Delete by match

Create a script that deletes all documents with `name="Holberton school"` in the `school` collection.
**File:** `7-delete`

### Task 8: List all docuemnts in Python

Write a Python function that lists all documents in a collection:

- Prototype: `def list_all(mongo_collection):`
- Return an empty list if no document in the collection
- `mongo_collection` will be the `pymongo` collection object

**File:** `8-all.py`

### Task 9: Insert a document in Python

Write a Python function that inserts a new document in a collection based on `kwargs`:

- Prototype: `def insert_school(mongo_collection, **kwargs):`
- `mongo_collection` will be the `pymongo` collection object
- Returns the new `_id`

**File:** `9-insert_school.py`

### Task 10: Change school topics

Write a Python function that changes all topics of a school document based on the name:

- Prototype: `def update_topics(mongo_collection, name, topics):`
- `mongo_collection` will be the `pymongo` collection object
- `name` (string) will be the school name to update
- `topics` (list of strings) will be the list of topics approached in the school

**File:** `10-update_topics.py`

### Task 11: Where can I learn Python?

Write a Python function that returns the list of school having a specific topic:

- Prototype: `def schools_by_topic(mongo_collection, topic):`
- `mongo_collection` will be the `pymongo` collection object
- `topic` (string) will be topic searched

**File:** `11-schools_by_topic.py`

### Task 12: Log stats

Write a Python script that provides some stats about Nginx logs stored in MongoDB:

- Database: `logs`
- Collection: `nginx`
- Display (same as the example):
    - first line: `x logs` where `x` is the number of documents in this collection
    - second line: `Methods`:
    - 5 lines with the number of documents with the `method = ["GET", "POST", "PUT", "PATCH", "DELETE"]` in this order (see example below - warning: it’s a tabulation before each line)
    - one line with the number of documents with:
        - `method=GET`
        - `path=/status`

You can use this dump as data sample: [dump.zip](https://s3.amazonaws.com/intranet-projects-files/holbertonschool-webstack/411/dump.zip)

**File:** `12-log_stats.py`

### Task 13: Regex filter `#advanced`

Write a script that lists all documents with `name` starting by `Holberton` in the collection `school`:

- The database name will be passed as option of `mongo` command

**File:** `100-find`

### Task 15: Log stats - new version `#advanced`

Improve `12-log_stats.py` by adding the top 10 of the most present IPs in the collection `nginx` of the database logs:

- The IPs top must be sorted (like the example below)

**File:** `102-log_stats.py`

