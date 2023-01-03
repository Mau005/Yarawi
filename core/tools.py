import pickle
import json
def package(pack):
    return pickle.dumps(pack)

def unpack(pack):
    return pickle.loads(pack)

def loadJson(path):
    archive = open(path, "r")
    json.open(archive)



if __name__ == "__main__":
    test = {"Hola":"Adios"}
    test = package(test)
    print(test)
    
    test = unpack(test)
    print(test)
    