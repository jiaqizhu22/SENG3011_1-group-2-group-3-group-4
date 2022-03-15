import json

# disease_id: int (foreign key reference diseases disease_id)
# report_id: string (foreign key reference reports report_id)

class Report_diseases:
    
    def __init__(self,id,name):
        self.disease_id = disease_id # int (foreign key reference diseases disease_id)
        self.report_id = report_id # string (foreign key reference reports report_id)

    # If we want to save our api class to a JSON file for other teams to use
    def save_to_json(self,filename):
        api_dict = {'disease_id':self.disease_id, 'report_id':self.report_id}
        with open(filename, 'w') as f:
            f.write(json.dumps(api_dict, indent=4))

    # Loading our api class from a json file
    def load_from_json(self, filename):
        with open(filename, 'r') as f:
            data = json.loads(f.read())
        #Assigning components
        self.disease_id = data['disease_id'] # int (foreign key reference diseases disease_id)
        self.report_id = data['report_id'] # string (foreign key reference reports report_id)