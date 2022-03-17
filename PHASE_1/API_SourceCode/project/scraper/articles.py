import json

# _id: integer (primary key)
# url: string
# date_of_publication: datetime
# headline: string
# main_text: string

class Articles:
    
    def __init__(self,_id,url,date_of_publication,headline,main_text):
        self._id = _id # integer (primary key)
        self.url = url # string
        self.date_of_publication = date_of_publication #datetime
        self.headline = headline # string
        self.main_text = main_text # string

    # If we want to save our api class to a JSON file for other teams to use
    def save_to_json(self,filename):
        api_dict = {'_id':self._id, 'url':self.url, 'date_of_publication':self.date_of_publication, 'headline':self.headline, 'main_text':self.main_text}
        with open(filename, 'w') as f:
            f.write(json.dumps(api_dict, indent=4))

    # Loading our api class from a json file
    def load_from_json(self, filename):
        with open(filename, 'r') as f:
            data = json.loads(f.read())
        #Assigning components
        self._id = data['_id'] # string (primary key)
        self.url = data['url'] # string
        self.date_of_publication = data['date_of_publication'] #datetime
        self.headline = data['headline'] # string
        self.main_text = data['main_text'] # string
