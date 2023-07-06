import json
# import "friends.json"

friends={"Dan":[20,"London, 3234242"], "Maria":[25,"Madrid",4325222]}
         
# with open("friends.json","rt") as f:
#     obj=json.load(f)    #load (turns json into dict) loads turns json string into dict
#     print(type(obj))
#     print(obj)
#     # json.dump(friends,f, indent=4)

json_string = json.dump(friends,)
# print(type(json_string))
# print(json_string["Dan"])