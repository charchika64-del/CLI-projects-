#Word counter
print("======WELCOME TO WORD COUNTER======")
print("Type 1 to see status of file")
print("Type 0 for exit")

def count_lines(file):
    count=0
    with open(file,"r") as f:
        for lines in f:
            count+=1
    return count
    
def count_words_chars(file):
      punctuations=['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']
      with open(file,"r") as f:
        content=f.read()
      fresh_content=content  
      for punc_mark in punctuations:
          #Replacing each punctuation mark with " ".
          #So that the punctuation marks will not be counted as words
          fresh_content=fresh_content.replace(punc_mark," ")
      words=fresh_content.split()
      #removes white spaces
      chars=len(content)
      #this counts spaces and everything
      return len(words),chars
                
while True:
    try:
        choice = int(input("Enter your choice: _"))
    except ValueError:
        print("Type a number")
        continue
        
    if choice == 1:
        try:
            filename = input("Enter file name: _")
            lines=count_lines(filename)
            words, chars=count_words_chars(filename)
            print("Results-------")
            print(f"Lines: {lines}")
            print(f"Words: {words}")
            print(f"Characters: {chars}")
        except FileNotFoundError:
           print("This file does not exist.")
           continue
           
    elif choice == 0:
        print("[Exited]")
        break
        
    else:
      print("Type 0 or 1")
