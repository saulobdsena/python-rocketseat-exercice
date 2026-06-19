"""
Estou fazendo as variáveis em inglês e E/S (Entrada e Saida) em inglês 
pois estou treinando meu inglês apenas isso

Im doing the variables and the I/O (Input and Output) in english because 
im treining my english just that

"""


task_list = []

while True:

    print("Task List Menager Menu:")
    print("1. Add Task")
    print("2. Show the task list")
    print("3. Update task")
    print("4. Complete task")
    print("5. Delete a completed task")
    print("6. End the program")

    response =  int(input("Digite sua escolha "))

    match response:

        #Case to add new task to the list 
        case 1:
            new_task = input("Digite a tarefa: ")
            task_list.append(new_task)
            print(f"Tarefa adicionada: {new_task}")

        #Case to show the task list
        case 2:
            print(task_list)

        #Case to update the task
        case 3:
            print()

            
    

