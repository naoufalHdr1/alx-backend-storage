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
