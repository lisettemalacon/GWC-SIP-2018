import json

file = open("list_of_responses.json", "r")
a = "".join(file.readlines())
new_data = ",".join(a.split(']['))
file.close()

file = open("list_of_responses.json", "w")
file.write(json.dumps(new_data))
file.close()
