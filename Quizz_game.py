import requests
import random
url = "https://opentdb.com/api.php"


def start_quizz(data):
     results = data["results"]
     score = 0
     option_letters = ["A","B","C","D"]
     solution = []
     all_user_answers = []
     
     for each_quizz in results:         
         question = each_quizz["question"]
         correct_answer  = each_quizz["correct_answer"]
         options = [correct_answer]+each_quizz["incorrect_answers"]
         solution.append(correct_answer)
         random.shuffle(options)
         display_options = dict(zip(option_letters,options))#makes two list items in key and value pairs
         print(question)
         for key,value in display_options.items():
             print(key,value,end=" "*5)
         user_answer = input("\nEnter your answer: ").upper()
         
         #check if user types an invalid option
         while user_answer not in option_letters:
             print("The option does not exist")
             print(question)
             print(display_options)
             user_answer = input("Enter your answer: ")
             
          #add if correct answer was given
         if display_options[user_answer] == correct_answer:
              score+=1
         all_user_answers.append(display_options[user_answer])
         options.clear()
     return score,solution,all_user_answers

        
print("Type 'e' if u want to exit or 'c' to start")
while True:
     start = input("Enter e or c: ").lower()
     if start in ('c','e'):
        if start == 'e':
            break
     else:
        print("Type a valid letter")
        continue
     print("Customize –")
     try:
         category = int(input("Enter  category number: "))
         amount = int(input("Enter the number of questions: "))
         difficulty = input("Set difficulty(easy/medium/hard): ")
         params = {"amount": amount,"category": category,  "difficulty": difficulty,"type": "multiple"}
         response = requests.get(url,params=params)
         response.raise_for_status()
         score ,correct_answers ,user_answers = start_quizz(response.json())
         print("SUMMARY—")
         print("Score",score)
         print("Correct Answers",correct_answers)
         print("Your answers",user_answers)
     except requests.exceptions.HTTPError as e:
         print("Error occured:",e)
     except ValueError:
         print("Type an id number.")
     except requests.exceptions.Timeout:
         print("Request timed out!!!")
     except requests.exceptions.ConnectionError:
         print("Please check your connection.")
