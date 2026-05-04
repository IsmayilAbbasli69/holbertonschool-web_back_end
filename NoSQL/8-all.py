#!/usr/bin/env python3
"""Lists all documents in a mongodb collection"""


def list_all(mongo_collection):
	"""Lists all documents in a mongodb collection"""
	return mongo_collection.find()
