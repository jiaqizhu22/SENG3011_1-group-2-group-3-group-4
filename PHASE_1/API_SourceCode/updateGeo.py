import http.client, urllib.parse
import json
import sys

def getGeoid(country, location):
    conn = http.client.HTTPConnection('api.positionstack.com')
    params = urllib.parse.urlencode({
        'access_key': 'cdb1fec8855543a36e8274d9fcb04232',
        'query': country + " " + location,
        'limit': 1
        })

    conn.request('GET', '/v1/forward?{}'.format(params))

    res = conn.getresponse()
    data = res.read().decode('utf-8')
    obj = json.loads(data)
    lat = obj['data'][0]['latitude']
    lng = obj['data'][0]['longitude']
    return {
        "lat": lat,
        "lng": lng
    }

if __name__ == '__main__': 
    print(sys.argv[1])
    print(sys.argv[2])
    g = getGeoid(sys.argv[1], sys.argv[2])
    print(g)