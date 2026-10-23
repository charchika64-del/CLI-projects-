import requests
from config.py import astro_key
from datetime import datetime
url = "https://api.freeastroapi.com/api/v2/horoscope/daily/sign"
headers = {"x-api-key": astro_key }

print("-----Horoscope teller 🔮------")
print("Type 1 to get today's horoscope.")
print("Type 2 to get a specific date's horoscope.")
print("Type 3 to exit.")

while True:
    try:
        choice = int(input("Enter a number: "))
        sign = input("Enter your sign: ")
        
        if choice == 1:
            params = {"sign": sign,"date": "today","tz_str": "Asia/Kolkata"}
            response = requests.get(url, params=params, headers=headers,timeout=10)
            response.raise_for_status()
            
        elif choice == 2:
            print("Enter month in short or long form.")
            year = int(input("Enter year: "))
            month = input("Enter month: ")
            day = int(input("Enter day: "))
            
            if month.isnumeric():
                print("No numbers are allowed for months.")
                print("Please type a short or a long month name.")
                continue
            if len(month)>3:
                 month = month[0:3]
            if len(str(day))>1:
                day="0"+str(day)
                
            try:
                month_num = datetime.strptime(month,"%b")
            except ValueError:
                print("That's invalid month.")
                continue
                
            date = f"{year}-{month}-{day}"
            params = {"sign": sign,"date": date,"tz_str": "Asia/Kolkata"}
            response = requests.get(url, params=params, headers=headers,timeout=10)
            response.raise_for_status()
            
        elif choice==3:
            print("Exited")
            break
        else:
           print('Type a valid number')
           continue
    except ValueError:
       print("Type a number !!!")
       continue
    except requests.exceptions.Timeout:
       print("The request is taking time.")
       continue
    except requests.exceptions.ConnectionError:
       print("Please check your network.")
       continue
    except requests.exceptions.HTTPError:
        print(response.status_code,"Error")
        print("Request failed")
        if response.status_code == 400:
            print("Check if there is a invalid month name or if a wrong sign name")
        else:
            print("Retry")
        continue
    data = response.json()
    colour = data["data"]["lucky"]["color"]["key"]
    print("Hello ",sign)
    print("Here is your horoscope🔮--")
    print("Lucky colour 🎨 ",colour)
    print("Lucky number 0️⃣ ",data["data"]["lucky"]["number"])
    print(f"Theme if the day🏷️- {data['data'] ['content'] ['theme']}")
    
    print("\nYour day 🌞---")
    print(data["data"]["content"]["text"])
    
    scores = data["data"]["scores"]
    print("\nYour scores 💯 ---")
    for key,value in scores.items():
           print(key , value)
