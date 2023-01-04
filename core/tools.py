import pickle
import json
def package(pack):
    return pickle.dumps(pack)

def unpack(pack):
    if pack == b'':
        return None #return None if nothin bytes received package
    return pickle.loads(pack) #return contents for received package

def loadJson(path):
    archive = open(path, "r")
    json.open(archive)



if __name__ == "__main__":
    test = {"Hola":"Adios"}
    test = package(test)
    print(test)
    
    test = unpack(test)
    print(test)
    