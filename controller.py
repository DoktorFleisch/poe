import requests

api_url =  "https://api.pathofexile.com"
header = {"User-Agent": "Oauth mylearningapp/0.0 (contact: ""danielwarkus@hotmail.com)"}

def get_leagues():
    response = requests.get(api_url + "/leagues", headers=header)

    return response.json()

if __name__ == '__main__':
    leagues = get_leagues()
    print(leagues)