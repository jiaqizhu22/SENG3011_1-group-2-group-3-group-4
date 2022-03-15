import json

# syndrome_id: int (foreign key reference syndromes syndrome_id)
# report_id: string (foreign key reference reports report_id)

class Report_syndromes:
    
    def __init__(self,id,name):
        self.syndrome_id = syndrome_id # int (foreign key reference syndromes syndrome_id)
        self.report_id = report_id # report_id: string (foreign key reference reports report_id)

    # If we want to save our api class to a JSON file for other teams to use
    def save_to_json(self,filename):
        api_dict = {'syndrome_id':self.syndrome_id, 'report_id':self.report_id}
        with open(filename, 'w') as f:
            f.write(json.dumps(api_dict, indent=4))

    # Loading our api class from a json file
    def load_from_json(self, filename):
        with open(filename, 'r') as f:
            data = json.loads(f.read())
        #Assigning components
        self.syndrome_id = data['syndrome_id'] # int (foreign key reference syndromes syndrome_id)
        self.report_id = data['report_id'] # report_id: string (foreign key reference reports report_id)