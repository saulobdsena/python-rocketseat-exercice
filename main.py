"""
Estou fazendo as variáveis e E/S (Entrada e Saida) em inglês 
pois estou treinando meu inglês apenas isso

Im doing the variables and I/O (Input and Output) in english because 
im treining my english just that

"""


task_list = []

#Method to add new task in the task_list
def add_task (task_list, task):
    tasks = {"task": task, "completed": False}
    task_list.append(task)
    print(f"Task: {task} has been added")
    return

#Method to view the task list
def view_tasks (task_list):
    
    for task in task_list:
        print(f"[] {task}")

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
            new_task = input("Enter the task: ")           
            add_task(task_list, new_task)
        #Case to show the task list
        case 2:
            view_tasks(task_list)
        #Case to update the task
        case 3:
            print()

            
    

