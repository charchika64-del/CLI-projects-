import requests

take_affirmation = input("Want to take affirmation? (y/n): ").strip().lower()

while take_affirmation == "y":
    try:
        # Free public API returning inspirational quotes/affirmations
        response = requests.get("https://zenquotes.io/api/random")
        response.raise_for_status()
        
        data = response.json()
        quote = data[0]['q']
        author = data[0]['a']
        
        print(f"\n\"{quote}\" - {author}\n")
    except Exception as e:
        print(f"Error fetching affirmation: {e}")
        
    take_affirmation = input("Want to take affirmation? (y/n): ").strip().lower()
else:
    print("Bye but stay positive")
  
