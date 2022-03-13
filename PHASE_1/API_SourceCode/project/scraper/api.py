import json

article_list = []

with open('PHASE_1/API_SourceCode/project/scraper/data.json') as json_file:
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
        for r in reports:
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