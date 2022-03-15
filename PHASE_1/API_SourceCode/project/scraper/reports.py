import json

# parent_id: string (foreign key reference Article _id)
# report_id: string (primary key)
# event_date: datetime

class Articles:
    
    def __init__(self,id,url,date_of_publication,headline,main_text):
        self.parent_id = parent_id # string (foreign key reference Article _id)
        self.report_id = report_id # string (primary key)
        self.event_date = event_date #datetime

    # If we want to save our api class to a JSON file for other teams to use
    def save_to_json(self,filename):
        api_dict = {'parent_id':self.parent_id, 'report_id':self.report_id, 'event_date':event_date}
        with open(filename, 'w') as f:
            f.write(json.dumps(api_dict, indent=4))

    # Loading our api class from a json file
    def load_from_json(self, filename):
        with open(filename, 'r') as f:
            data = json.loads(f.read())
        #Assigning components
        self.parent_id = data['parent_id'] # string (foreign key reference Article _id)
        self.report_id = data['report_id'] # string (primary key)
        self.event_date = data['event_date'] #datetime