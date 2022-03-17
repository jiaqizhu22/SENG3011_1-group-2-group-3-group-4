import json

# report_id: string (foreign key reference reports report_id)
# place_id: int (foreign key reference places place_id)

class Locations:
    
    def __init__(self,id,country,location):
        self.id = id # id: int (primary key)
        self.country = country # string
        self.location = location # string

    # If we want to save our api class to a JSON file for other teams to use
    def save_to_json(self,filename):
        api_dict = {'report_id':self.report_id, 'place_id':self.place_id}
        with open(filename, 'w') as f:
            f.write(json.dumps(api_dict, indent=4))

    # Loading our api class from a json file
    def load_from_json(self, filename):
        with open(filename, 'r') as f:
            data = json.loads(f.read())
        #Assigning components
        self.report_id = data['report_id'] # report_id: string (foreign key reference reports report_id)
        self.place_id = data['place_id'] # place_id: int (foreign key reference places place_id)