import requests 
url="https://official-joke-api.appspot.com/random_joke"
#it has keys type,setup,punchline,id
permission=input("Wanna laugh(y/n)? ")
while permission=="y":
    joke=requests.get(url)
    joke=joke.json()
    print(f"Computer: {joke["setup"]}")
    reply=input("You: ")
    print(f"Computer: {joke["punchline"]}")
    permission=input("Wanna laugh(y/n)? ")
else:
    print("Computer: Who will listen my jokes? Okay bye.")
