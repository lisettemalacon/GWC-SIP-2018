import json
file = open("list_of_responses.json", "r")
data = json.load(file)

for response in list_of_responses:
    print (response)

for response in list_of_responses:
    print(response["What is your favuwuite animal? "])
