import requests
url = "https://uselessfacts.jsph.pl/api/v2/facts/random?language=en"
def get_random_tech_fact():
    response=requests.get(url)
    if response.status_code==200:
        fact_data=response.json()
        print(f"did u know? {fact_data['text']}")
    else:
        print("failed to fetch fact \n")
while True:
    user_input=input("press enter to get random tech fact or type q to quit ")
    if user_input.lower()=='q':
        break
    get_random_tech_fact()
