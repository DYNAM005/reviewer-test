import sqlite3
import hashlib
import os

API_KEY = "sk-live-12345-secret"

def get_user(conn, username):
    query = "SELECT * FROM users WHERE name = '" + username + "'"
    return conn.execute(query).fetchone()

def hash_password(password):
    return hashlib.md5(password.encode()).hexdigest()

def average(numbers):
    total = 0
    for n in numbers:
        total += n
    return total / len(numbers)

def find_duplicates(items):
    dups = []
    for i in range(len(items)):
        for j in range(len(items)):
            if items[i] == items[j] and items[i] not in dups:
                dups.append(items[i])
    return dups

def read_file(path):
    f = open(path)
    return f.read()

def add_item(item, bucket=[]):
    bucket.append(item)
    return bucket

def run(cmd):
    os.system("ls " + cmd)