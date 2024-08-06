import requests

#   response = requests.get("https://api.pathofexile.com/leagues", headers={"User-Agent": "Oauth mylearningapp/0.0 ("
#                                                                                           "contact: "
#                                                                                           "danielwarkus@hotmail.com)"})

api_url =  "https://api.pathofexile.com"
header = "User-Agent: Oauth mylearningapp/0.0 (contact: danielwarkus@hotmail.com"

def get_leagues():
    response = requests.get(api_url + "/leagues",
                            headers={"User-Agent": "Oauth mylearningapp/0.0 (contact: ""danielwarkus@hotmail.com)"})
    return response.json()

if __name__ == '__main__':
    leagues = get_leagues()
    print(leagues)