import json
import os
# = open("list_of_responses.json", "w") # create a file called list_of_responses.json, with the write permission


questions = ["What is your favuwuite animal? ", "What app do you use the most? ", "What is your favuwuite color? ", "Who is your favuwuite celebrity? ", "What is your favuwuite TV show? "]
cont = True

list_of_responses = [] # empty list for answers

while cont:
    answer = {}
    for q in questions:
        answer[q] = input(q)
    to_cont = input("Continuwu? Y/N ")
    if to_cont == "Y":
        cont = True
    else:
        cont= False
    list_of_responses.append(answer)

if os.path.isfile("list_of_responses.json"):
    file = open("list_of_responses.json", "r+")
    old_data = json.load(file)
    old_data.extend(list_of_responses)
    file.write(json.dumps(old_data))
    file.close()
else:
    file = open("list_of_responses.json", "w")
    file.write(json.dumps(list_of_responses))
    file.close()
