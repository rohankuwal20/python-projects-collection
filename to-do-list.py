#TO-DO-LIST
def add_task(task):
    tasks.append(task)

def remove_task(task):
    tasks.remove(task)

tasks = []
choice = 0

while True :
    print("\n---------TO_DO_LIST------------")
    print("1. ADD TASK")
    print("2. VIEW TASK")
    print("3. REMOVE TASK")
    print("4. EXIT")
  
    choice = int(input("enter choice ! : "))
    if choice ==1:
        task = input("enter task !: ")
        add_task(task)
    elif choice ==2:
          for task in tasks:
           print(task,end="")
           print()
    elif choice ==3:
        task=input("enter the task to remove !: ")
        remove_task(task)
    elif choice==4:
        break
    else :
        print("your choice is invalid")

