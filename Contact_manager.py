import os
contacts = {}

if os.path.exists('contacts_manager.txt'):
    with open('contacts_manager.txt','r') as manager:
        for line in manager:
            #removes /n and converts 
            #each line into a list
            list=line.strip().split(',')
            #rewriting from the file
            contacts[list[0]]=list[1]
else:
    with open('contacts_manager.txt','w') as manager:
        pass
        
print("Welcome to comtact manager")
print('Type 1 to add contact')
print('Type 2 to view all')
print('Type 3 to search contact')
print('Type 4 to delete contact')
print('Type 5 to exit')

while True:
    try:
        choice = int(input('Enter your choice: '))
    except ValueError:
        print("Type a number")
        continue
        
    if choice == 1:
       name = input('Enter name: ').lower()
       phone = input('Enter number: ')
       
       #check if there is a letter 
       if not phone.isnumeric():
          print('Type a valid phone number')
          continue
          
      #check if contact exists
       if name in contacts.keys():
         print('The name already exists.')
         continue
                    
       contacts[name] = phone
       with open('contacts_manager.txt','a') as manager:
           manager.write(f"{name},{phone}\n")
       print('Contact added')    
       
    elif choice == 2:
        with open('contacts_manager.txt','r') as manager:
            for line in manager:
                print(line.strip())
        
    elif choice == 3:
        search = input('Enter name: ').lower()
        #check if it exists
        if search not in contacts.keys():
           print('This contact does not exist')
        else:
           print(search,contacts[search])
                    
    elif choice == 4:
        delete_contact = input('Enter name: ').lower()     
        try:
            del contacts[delete_contact] 
           #Erase everything rewrite from the updated dict            
            with open('contacts_manager.txt','w') as manager:
                for keys,values in contacts.items():
                    manager.write(f"{keys},{values}\n")       
            print("Contact deleted")           
        except KeyError:
                print('Contact not found')
                
    elif choice == 5:
        print('exited')       
        break     
        
    else:
        print('Type valid number.')
