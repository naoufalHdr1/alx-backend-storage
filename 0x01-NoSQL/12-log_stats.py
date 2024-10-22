#!/usr/bin/env python3
"""
Script to provide stats about Nginx logs stored in MongoDB.
"""
from pymongo import MongoClient


def log_stats():
    """ Prints stats about Nginx logs stored in MongoDB """
    client = MongoClient('mongodb://localhost:27017')
    db = client['logs']
    nginx_collection = db['nginx']

    # Count total number of documents in the collection
    total_logs = nginx_collection.count_documents({})
    print(f"{total_logs} logs")

    # Count documents by HTTP method
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    for method in methods:
        count_method = nginx_collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count_method}")

    # Count documents with method=GET and path=/status
    status_check = nginx_collection.count_documents(
                        {"method": "GET", "path": "/status"}
                   )
    print(f"{status_check} status check")


if __name__ == "__main__":
    log_stats()
