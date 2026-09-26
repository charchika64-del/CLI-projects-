import requests
url="https://randomuser.me/api/"
class Name:
    def __init__(self,title,first,last):
        self.title=title
        self.first=first
        self.last=last
        self.name=title+" "+first+" "+last
        
class Location:
   def __init__(self,city,state,country):
        self.city=city
        self.state=state
        self.country=country
        self.full_address=self.city+", "+self.state+", "+self.country
        
class User:
   def __init__(self,name,location,gender,age,birth_date,email):
        self.name=name
        self.gender=gender 
        self.age=age
        self.birth_date=birth_date
        self.location=location
        self.email=email
        
   def __str__(self):
         return (
          f"Name: {self.name.name}\n"
          f"Address: {self.location.full_address}\n"
          f"Gender: {self.gender}\n"
          f"Age: {self.age}\n"
          f"DOB: {self.birth_date}\n"
          f"Email: {self.email}"
            )
      
all_users=[]
print("Welcome to fake user generator")
print("Type 1 to generate a user")
print("Type 2 to view the list")
print("Type 3 to see a user's detail")
print("Type 4 to exit this loop")

while True:
    try:
        user_input=int(input("Enter a number: "))
        
        if user_input==1:
            data=requests.get(url).json()
            basic_info=data["results"] [0]
            fake_name=Name(basic_info["name"]["title"],basic_info["name"]["first"],basic_info["name"]["last"])
            fake_location=Location(basic_info["location"]["city"],basic_info["location"]["state"],basic_info["location"]["country"])
            fake_user=User(fake_name,fake_location,basic_info["gender"],basic_info["dob"]["age"],basic_info["dob"]["date"],basic_info["email"])
            all_users.append(fake_user)
            print(fake_user)
            
        elif user_input==2:
            for user in all_users:
                print(user.name.name)
                
        elif user_input==3:
            name=input("Enter first name: ").lower()
            found = False
            for user in all_users:
                if user.name.first.lower() == name:
                    print(user)
                    found = True
            if not found:
                print("This user does not exist")
                
        elif user_input==4:
             break
             
        else:
             print("Type a valid number.")
             
    except ValueError:
       print("Type a number from 1 to 4")
       continue
          
