from pymongo import MongoClient
import hashlib


def get_db_handle(db_name, host, port, username, password):
    client = MongoClient(host=host,
                         port=int(port),
                         username=username,
                         password=password
                        )
    db_handle = client[db_name]
    return db_handle, client

def get_collection_handle(db_handle,collection_name):
    return db_handle[collection_name]

def validatePassword(db_handle,username,password):
    user_creds = get_collection_handle(db_handle, "user_creds")
    # currentUser = user_creds.find({"username":username})
    query = {"username":username}
    currentUser = user_creds.find(query)
    # for x in mydoc:
    #     print (x["password"])
    # for x in user_creds.find({},{"username":username}):
    #     print(x)
    if (hashlib.md5(password.encode()).hexdigest() == currentUser[0]["password"]):
        return True
    return False