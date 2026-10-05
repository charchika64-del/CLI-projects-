#To do list
print("===== MY TO-DO LIST =====")
print("1. Add task")
print("2. View tasks")
print("3. Delete task")
print("4. Exit")

work=[]
#loading old tasks from file in list work
try:
    with open("to-do_list.txt","r") as tasks:
        for line in tasks:
            work.append(line.strip())
except FileNotFoundError:
    print("The file is not in the system")
    print("It's created now")
    with open("to-do_list.txt","w") as tasks:
        tasks.write("")
        
def show_tasks():
    for index, item in enumerate(work):
        print(index+1, item)

while True:
    try:
        choice=int(input("Enter your choice: _"))
    except ValueError:
         print("Type a number")
         continue
    
    if choice == 1:
        task=input("Enter task: _")                     
        work.append(task)
        with open("to-do_list.txt","a") as tasks:
            tasks.write(f"{task}\n")
            
    elif choice == 2:
        if len(work) == 0:
            print("There are no tasks")
        else:
            show_tasks()
                            
    elif choice == 3:
        show_tasks()
        try:
            task_num=int(input("Enter task number: _"))
            remove_item=work[task_num-1]
            work.remove(remove_item)
        except ValueError:
            print("Type the task number.")
            continue
        except IndexError:
            if len(work)==0:
                print("No items to delete")
            else:
                print(f"Task number {task_num} does not exist.")
            continue
            
        #Rewrites the file from the updated list
        with open("to-do_list.txt","w") as tasks:
            for item in work:
                tasks.write(f"{item}\n")
        print("[Item deleted]")
        
    elif choice == 4:
        print("Exited")
        break

    else:    
       print("Type 1,2,3 or 4")
       continue
    
