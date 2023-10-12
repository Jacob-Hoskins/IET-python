import os
import pymongo
import startSearching
from bson.json_util import dumps
from bson.objectid import ObjectId
import json

connection_string = "mongodb+srv://ietproject17238:52262Jah99.@iet.eiurhrz.mongodb.net/?retryWrites=true&w=majority/"
client = pymongo.MongoClient(connection_string)

#     test = client.watch([{
#     '$match': {
#         'operationType': { '$in': ['insert'] }
#     }
# }])
#     test = pymongo.MongoClient(os.environ['CHANGE_STREAM_DB'])
#     change_stream = test.watch()
#    "ietproject17238", "52262Jah99", "items"))

# TODO: grab document from collection
def find_finished_document(id):
    pass

#function below gets rid of spaces in the list of items to search and start searching on each one
def reformat_itemList_dictionary(user_info):
    for y in user_info["items_to_find"]:
        # x = user_info['items_to_find'][y]

        #TODO: turn into for loop to loop through all the items in the list
        #Below gives you a string of the item to search
        preFormat = y["itemName"].split(" ")
        final_str = ""
        l = 0
        while l < len(preFormat) - 1:
            final_str = final_str + preFormat[l] + "%20"
            l += 1
        final = final_str + preFormat[-1]

        #sends item to make_request to start the searching process
        startSearching.make_request_menards(final)


def gather_items_to_search(user_info):
    # grabs all the users data to pull the info from the db
    usersInfo = client.get_database("test").get_collection("itemsearches").find_one({'_id': ObjectId(user_info['user_id'])})
    # adds their search list to our dictionary
    user_info["items_to_find"] = usersInfo["itemList"]
    reformat_itemList_dictionary(user_info)


def items_to_search(items):
    print(items)

def watch_for_changes():
    test = client.watch()

    searchingInformatoin = {}

    for x in test:
        object = json.loads(dumps(x))
        database_change = object['updateDescription']
        changed_fields = database_change["updatedFields"]
        if("finsihedEstimate" in changed_fields):
            # Below gives you ALL the itemList key value pairs, need to find the one by the user who clicked the finished button
            if(changed_fields["finsihedEstimate"] == True):
                print("Finished Estimate")
                userIdStepOne = object['documentKey']
                # Sets user id of finished estimate below
                searchingInformatoin["user_id"] = userIdStepOne['_id']['$oid']
                gather_items_to_search(searchingInformatoin)
            else:
                print("Nah the estimate isnt finished Bro")
        else:
            print("Not her")



# test = get_database()
# print(test['test'])
# export CHANGE_STREAM_DB="mongodb+srv://ietproject17238:52262Jah99.@iet.eiurhrz.mongodb.net/?retryWrites=true&w=majority"

# while True:
# watch_for_changes()
# watch_for_updates()
