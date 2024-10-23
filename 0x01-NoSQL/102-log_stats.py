#!/usr/bin/env python3
"""
Script to provide stats about Nginx logs stored in MongoDB.
12-log_stats.py - Improved to include top 10 most frequent IPs
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

    # Top 10 most frequent IPs
    print("IPs:")
    pipeline = [
            {"$group": {"_id": "$ip", "count": {"$sum": 1}}},
            {"$sort": {"count": -1}},
            {"$limit": 10}
    ]

    top_ips = nginx_collection.aggregate(pipeline)
    for ip in top_ips:
        print(f"\t{ip['_id']}: {ip['count']}")


if __name__ == "__main__":
    log_stats()
