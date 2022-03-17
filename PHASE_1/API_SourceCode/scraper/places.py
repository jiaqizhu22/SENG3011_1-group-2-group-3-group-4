import json

# place_id: serial
# place_name: string

class Places:
    
    def __init__(self,place_id,place_name):
        self.place_id = place_id # serial
        self.place_name = place_name # string

    # If we want to save our api class to a JSON file for other teams to use
    def save_to_json(self,filename):
        api_dict = {'place_id':self.place_id, 'place_name':self.place_name}
        with open(filename, 'w') as f:
            f.write(json.dumps(api_dict, indent=4))

    # Loading our api class from a json file
    def load_from_json(self, filename):
        with open(filename, 'r') as f:
            data = json.loads(f.read())
        #Assigning components
        self.place_id = data['place_id'] # serial
        self.place_name = data['place_name'] # string
