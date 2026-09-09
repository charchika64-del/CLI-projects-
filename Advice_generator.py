import requests
print("Please take some advice.")
take_advice=input("Take advice (y/n)? ")
while take_advice=="y":
    response = requests.get("https://api.adviceslip.com/advice")
    data = response.json() 
    give_advice=data["slip"] ["advice"]
    print(give_advice)
    take_advice=input("Take advice (y/n)? ")
else:
    print("Bye, but just see the last advice.")
    print("Remember them.")
    print("Do your work.")
