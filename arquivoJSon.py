import json
dic = {

}

objects = json.dumps(dic,indent=2)
with open("arquivo.json", "w") as file:
    file.write(objects)
print(objects)