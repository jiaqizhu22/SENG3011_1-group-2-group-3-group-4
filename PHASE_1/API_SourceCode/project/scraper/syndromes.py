import json

# id: serial
# name: string

class Locations:
    
    def __init__(self,id,name):
        self.id = id # serial
        self.name = name # string

    # If we want to save our api class to a JSON file for other teams to use
    def save_to_json(self,filename):
        api_dict = {'id':self.id, 'name':self.name}
        with open(filename, 'w') as f:
            f.write(json.dumps(api_dict, indent=4))

    # Loading our api class from a json file
    def load_from_json(self, filename):
        with open(filename, 'r') as f:
            data = json.loads(f.read())
        #Assigning components
        self.id = data['id'] # serial
        self.name = data['name'] # string