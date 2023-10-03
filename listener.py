import os
import pymongo
import startSearching
from bson.json_util import dumps
from bson.objectid import ObjectId
import json

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

def items_to_search(items):
    print(items)
    for x in items:
        print(startSearching.make_request(items))

connection_string = "mongodb+srv://ietproject17238:52262Jah99.@iet.eiurhrz.mongodb.net/?retryWrites=true&w=majority/"
def watch_for_changes():
    client = pymongo.MongoClient(connection_string)
    test = client.watch()

    itemsToSearch = []

    for x in test:
        object = json.loads(dumps(x))
        database_change = object['updateDescription']
        # print(database_change["updatedFields"])
        changed_fields = database_change["updatedFields"]
        if("finsihedEstimate" in changed_fields):
            if(changed_fields["finsihedEstimate"] == True):
                print("Finished Estimate")
                # TODO: below will give you the finished estimates Document
                test_id = object["documentKey"]
                db = client["test"]
                col = db["itemsearches"]
                for x in col.find():
                    # print(x['itemList'])

                    for y in x['itemList']:
                        itemsToSearch.append(y['itemName'])

                items_to_search(itemsToSearch)
            else:
                print("Nah the estimate isnt finished Bro")
        else:
            print("Not her")
        # if("finishedEstimate" in database_change["updatedFields"]):
        #     print("they finished their estimate")
        # else:
        #     print("They havent finished their estimate")


    # for change in test:
    #     updated_data = dumps(change)
    #     print("UPDATED DATA--------", updated_data)
    #     object = json.loads(updated_data)
    #     db_info = object["ns"]
    #     new_collection_data = db_info["coll"]
    #     # Gets inserted Item
    #     object_id = (object["documentKey"])
    #     key_dict = object_id['_id']
    #     final_key = key_dict["$oid"]
    #     object_event = (object["updateDescription"])
    #     grab_field = object_event['updatedFields']
    #     updated_field = grab_field.get("finishedEstimate")
    #     print("GRAB FIELD-------", grab_field)

        # if("finishedEstimate" in grab_field):
        # if (grab_field["finishedEstimate"] == True):
        #     test = client['test']
        #     print("They finished their estimate")
        #     col = test['itemsearches']
        #     document = col.find_one({"_id": ObjectId(final_key)})
        #     all_items = startSearching.search_for_items_starting_point(document)
        #     print(startSearching.make_request())
        # else:
        #     print("not finished, different event, check watch_for_changes() to find this message")



# def watch_for_updates():
#     client = pymongo.MongoClient(connection_string)
#     test = client.watch([{
#         '$match': {
#             'operationType': {'$in': ['update']}
#         }
#     }])
#     for change in test:
#         updated_data = dumps(change)
#         # print(updated_data)
#         object = json.loads(updated_data)
#         print(object)

# test = get_database()
# print(test['test'])
# export CHANGE_STREAM_DB="mongodb+srv://ietproject17238:52262Jah99.@iet.eiurhrz.mongodb.net/?retryWrites=true&w=majority"

# while True:
# watch_for_changes()
# watch_for_updates()
