import json

def jsonToDictionary(textData):
    return json.loads(textData)

def dictionaryToJson(jsonData):
    return json.dumps(jsonData)
