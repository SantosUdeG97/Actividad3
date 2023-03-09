# Creado el 09 de Marzo de 2023 por José Luis Santos Mendoza
# Actividad 1: procesamiento por lotes
# Universidad de Guadalajara, Seminario de Solución de Problemas de Sistemas Operativos
# Profesor Javier Rosales Martínez, Sección D06

import os
from os import system
from sys import exit


# Function to read the file that we are going to use.
def readFile():
    processes = []  # Creating an array for all the processes in the file
    with open("procesos.txt", 'r') as f:
        lines = f.readlines()
        for line in lines:  # Scrolling through the file
            process, cicles, priority = line.strip().split(',')
            processes.append((process, int(cicles), int(priority)))
    return processes


# Round Robin algorithm function
def roundRobin(processes, Q):
    os.system('cls' if os.name == 'nt' else 'clear')
    # Using a list to put all the processes on the algorithm
    newList = list(processes)
    while newList:
        actualProcess = newList.pop(0)
        name, quantum, p = actualProcess
        # Printing the process that is running
        print(f"Running: {name}, with {quantum} Q.")
        quantum -= Q
        if quantum > 0:  # If the number of quantums is more than 0, append the process to the list
            newList.append((name, quantum, p))
            print(
                f"The process: {name} is back on the list with {quantum} Q.\n")
        else:
            print(f"Finishing {name} process.\n")
    input("\nPress enter to continue...")
    optionSelect()  # Back to the menu


# Shortest job first algorithm function
def shortestJobFirst(processes):
    os.system('cls' if os.name == 'nt' else 'clear')
    # Creating a list to put the processes.
    newList = sorted(processes, key=lambda x: x[1])
    while newList:  # While there's processes to run, is going to show the process that is running
        actualProcess = newList.pop(0)
        name, size, p = actualProcess
        # Printing the process with the number of cicles that was needed
        print(f"Process executed: {name} with {size} cicles.\n")
    input("\nPress enter to continue...")
    optionSelect()  # Back to the menu


# First in, first out algorithm function
def firstInfirstOut(processes):
    os.system('cls' if os.name == 'nt' else 'clear')
    newList = list(processes)  # Putting the processes on a list
    while newList:  # While there's processes to run, is going to show the process that is running
        actualProcess = newList.pop(0)
        name, q, p = actualProcess
        # Printing the process that is running
        print(f"Process executed: {name}.\n")
    input("\nPress enter to continue...")
    optionSelect()  # Back to the menu


# Priorities algorithm function
def priorities(processes):
    os.system('cls' if os.name == 'nt' else 'clear')
    # Putting the processes on a list
    newList = sorted(processes, key=lambda x: x[2])
    # While there's processes to run, is going to show the process that is running with the priority that it has
    while newList:
        actualProcess = newList.pop(0)
        name, q, priority = actualProcess
        # Printing the process that is running
        print(f"Process executed: {name}, with priority {priority}.\n")
    input("\nPress enter to continue...")
    optionSelect()  # Back to the menu


# Function for clearing the terminal while returning to the menu
def clearScreen():
    os.system('cls' if os.name == 'nt' else 'clear')


# Option select function
def optionSelect():
    clearScreen()
    processes = readFile()
    Q = 3
    # Putting all the option on an array
    options = {
        1: ('Round Robin.', roundRobin),
        2: ('Shortest Job First.', shortestJobFirst),
        3: ('First In - First Out.', firstInfirstOut),
        4: ('Priorities.', priorities),
        5: ('End program.', exit),
    }

    print("Planning algorithms.\n")
    for key, value in options.items():
        print(f"{key}. {value[0]}")
    try:  # With the in data for the option, program is going to try to enter in an algorithm function
        choice = int(input("\nChoose an option: "))
        clearScreen()
        if choice in options:
            if choice == 1:
                options[choice][1](processes, Q)
            elif choice == 2:
                options[choice][1](processes)
            elif choice == 3:
                options[choice][1](processes)
            elif choice == 4:
                options[choice][1](processes)
            else:
                options[choice][1]()
        else:
            print("No valid option.")
            input("\nPress enter to continue...")
            optionSelect()
    except ValueError:
        print("Invalid data..")
        input("\nPress enter to continue...")
        optionSelect()


if __name__ == "__main__":
    optionSelect()
