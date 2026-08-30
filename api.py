import requests
def randomjoke():
    url="https://official-joke-api.appspot.com/random_joke"
    response =requests.get(url) 
    if response.status_code==200:
        joke=response.json()
        return f"{joke['setup']} {joke['punchline']}"
    else:
        return "Failed to fetch a joke."
def main ():
    print("welcome to the random joke generator")
    while True:
        user_input=input("Press Enter to get a joke or type 'exit' to quit: ")
        if user_input.lower()=='exit':
            print("Goodbye!")
            break
        joke =randomjoke()
        print(joke)
if __name__=="__main__":
    main()