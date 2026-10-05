import os
os.makedirs("My_notes",exist_ok=True)
#if the folder already exists dont crash the program
os.chdir("My_notes")
#now the cwd is the folder
print("<----------Welcome to notes--------->")
print("Type 1 to create note")
print("Type 2 to view note")
print("Type 3 to see all")
print("Type 4 to delete note")
print("Type 5 to exit")
print("[Don't add .txt extension. It will be added automatically while writing filename]")
print("[Your file will be saved in lower case]")

while True:
    try:
        choice=int(input("Enter number according to your choice _"))
    except ValueError:
         print("Enter a number")
         continue
    
    if choice == 1:
        note_name = input("Enter the file name _").lower()
        
        #checks if filename is empty or not
        if not note_name.strip():
            #removes spaces
            #if not ""=True
            print("Please enter a name.")
            continue
        note_name = note_name + ".txt"
        
        #checks if file is being overwritten
        if os.path.exists(note_name):
            confirm = input("Note exists. Overwrite? (y/n): ")
            if confirm.lower() != "y":
                continue 
         #if file name is not empty abd if confirm is other than y       
        write_content = input("Write the note _")      
        with open(note_name,"w") as note:
            note.write(write_content)
     
    elif choice == 2:
         try:
             filename = input("Enter file name _").lower()+".txt"
             with open(filename,"r") as view_file:
                 read_content = view_file.read()
         except FileNotFoundError:
             print("This file does not exist.")
             continue
         print(read_content)    
         
    elif choice == 3:
         print("Here is the list---")
         notes_list = os.listdir()
         #No path needed because 
         #the cwd is already My_notes
         for each_note in notes_list:
            print(each_note)
            
    elif choice == 4:
         remove_file = input("Enter the file name _").lower()+".txt"
         if os.path.exists(remove_file):
            os.remove(remove_file)
            print("[File deleted]")
         else:
            print("That file does not exist")
            continue
            
    elif choice == 5:
            print("[Finished]") 
            break
            
    else:
            print("Type a valid number")     
            continue    
                              
