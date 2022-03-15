import json

class Api:
    
    def __init__(self,article,report,log):
        self.article = {
            "url":url,
            "date_of_publication": date,
            "headline": headline,
            "main_text":main_text,
            "reports":reports,
        }
        self.report = {
            "diseases": diseases,
            "syndromes": syndromes,
            "event_date":"", #this needs to be sorted out
            "locations":locs_list,
        }
        self.log = {
            "Team Name": team,
            "Access Time": datetime,
            "Data Source": source_url
        }

    # If we want to save our api class to a JSON file for other teams to use
    def save_to_json(self,filename):
        api_dict = {'article': self.article, 'report': self.report, 'log': self.log}
        with open(filename, 'w') as f:
            f.write(json.dumps(api_dict, indent=4))

    # Loading our api class from a json file
    def load_from_json(self, filename):
        with open(filename, 'r') as f:
            data = json.loads(f.read())
        #Assigning components
        self.article = data['article']
        self.report = data['report']
        self.log = data['log']



article_list = []
with open('PHASE_1/API_SourceCode/project/scraper/data.json', 'r') as json_file:
    # Store the json data as a list
    data = json.load(json_file)

    for item in data:
        url = item['url']
        pub_date = item['date_of_publication']
        headline = item['headline']
        content = item['main_text']
        reports_list = []
        reports = item['reports']
        print(reports)
        for r in reports.split(''):
            print(r)
            diseases = r[0]
            syndromes = r[1]
            event_date = r[2]
            locs_list = r[3]
            report = {
                "diseases": diseases,
                "syndromes": syndromes,
                "event_date":"", #this needs to be sorted out
                "locations":locs_list,  
            }
            reports.append(report)
        
        article = { #making dict of the info.
            "url":url,
            "date_of_publication": date,
            "headline": headline,
            "main_text":main_text,
            "reports":reports,
        }
        article_list.append(article)

    # --- Handling different requests ---
    # Request all reports in a country

print(article_list)