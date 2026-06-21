"""
Estou fazendo as variáveis e E/S (Entrada e Saida) em inglês 
pois estou treinando meu inglês apenas isso

Im doing the variables and I/O (Input and Output) in english because 
im treining my english just that

"""


task_list = []

#Method to add new task in the task_list
def add_task (task_list, task_name):
    task = {"task": task_name, "completed": False}
    task_list.append(task)
    print(f"Task: {task_name} has been added")
    return

#Method to view the task list
def view_tasks (task_list):

    print("\n Task List")

    for i, task in enumerate(task_list, start=1):
        status = "✓" if task["completed"] else " "
        print(f"{i}. [{status}] {task["task"]}")

    return
        
#Method to update the task status
def update_task(task_list, task_index, new_task_name):

    try:
        task_list[(int(task_index) - 1)]["task"] = new_task_name
        print(f"Task {task_index} updated to {new_task_name}")
    
    except IndexError as e:
        print("Error: your index is out of range")

    return

#Method to complete a task
def complete_task(task_list, task_index):

    try:
        task_list[(int(task_index) - 1)]["completed"] = True    
        print(f"Task {task_index} completed")

    except IndexError as e:
        print("Error: your index is out of range")

    return

def detele_completed_tasks(task_list):

    for task in task_list:
        if task["completed"] == True:
            task_list.remove(task)

    print("Completed tasks has been deleted")
    
    return


while True:

    print("\nTask List Menager Menu:")
    print("1. Add Task")
    print("2. Show the task list")
    print("3. Update task")
    print("4. Complete task")
    print("5. Delete a completed task")
    print("6. End the program")

    response =  int(input("Enter your choise "))

    match response:

        #Case to add new task to the list 
        case 1:
            task = input("Enter the task: ")           
            add_task(task_list, task)

        #Case to show the task list
        case 2:
            view_tasks(task_list)

        #Case to update the task
        case 3:
            view_tasks(task_list)
            task_index = input("Enter the task number do you want update: ")
            new_task = input("Enter the new task name ")
            update_task(task_list,task_index,new_task)

        #Case to complete the task
        case 4:
           view_tasks(task_list) 
           task_index = input("Select the task number do you want complete: ")
           complete_task(task_list, task_index)

        case 5:
            detele_completed_tasks(task_list)
            view_tasks(task_list)

        case 6:
            break
