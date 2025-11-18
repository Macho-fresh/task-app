"""
a task tracking app

"""

# necessary imports for task app
import json
from datetime import datetime
import sys

 
 

# increments id function to increment the id after each task is created and its stores in a txt file
def incrementId():
    
    with open('id.txt', 'r') as f:
        id = int(f.read())
        id+=1
        with open('id.txt', 'w')as f:
            f.write(str(id))
        return id

with open('id.txt', 'r') as f:
        id = int(f.read())
        id+=1


# addtask function to add each
def addtask ():
    add = input("kindly add a task: ")
    
    try: 
        with open("task.json", "r") as f:
            tasks = json.load(f) 
    except json.decoder.JSONDecodeError or TypeError: 
        tasks = []         
    task = {
        'id': incrementId(),
        'task': add, 
        'createdAt': datetime.now().strftime('%Y-%m-%d, %I:%M %p'),
        'updatedAt': 'No updates yet',
        'status': 'to-do'
    }
    try:    
        tasks.append(task)
        print(f'task added successfuly ID:{id }')

    except:
        print('something went wrong, try again')
   
    with open('task.json', 'w') as f:
        
        json.dump(tasks, f, indent=2)

def update():
    updateTask = int(input('Enter the ID: '))
    changed = input('Enter updated task: ')
    with open('task.json', 'r') as f:
        tasks = json.load(f)
        tasks[updateTask]['task'] = changed
        tasks[updateTask]['updatedAt'] = datetime.now().strftime('%Y-%m-%d, %I:%M %p')
        with open('task.json', 'w') as f:
            json.dump(tasks, f, indent=2)

def progress():
    updateTask = int(input('Enter the ID: '))
    changed = input('Enter Progress: ')
    with open('task.json', 'r') as f:
        tasks = json.load(f)
        tasks[updateTask]['status'] = changed
        with open('task.json', 'w') as f:
            json.dump(tasks, f, indent=2)


if 'list' == sys.argv[1] and 'done' in sys.argv[2]:
    with open('task.json', 'r') as f:
        tasks = json.load(f)
        for task in tasks:
            if task['status'] == 'done':
                print(f'{task} \n')  
            

elif 'list' == sys.argv[1] and 'to-do' in sys.argv[2]:
    with open('task.json', 'r') as f:
        tasks = json.load(f)
        for task in tasks:
            if task['status'] == 'to-do':
                print(f'{task} \n')  
            else:
                print('No tasks to-do')

elif 'list' == sys.argv[1] and 'progress' in sys.argv[2]:
    with open('task.json', 'r') as f:
        tasks = json.load(f)
        for task in tasks:
            if task['status'] == 'in-progress':
                print(f'{task} \n')  
        else:
            print('No tasks in progress')

elif 'add' in sys.argv[1]:
    sys.argv[1] = addtask()

elif 'update' in sys.argv[1]:
    sys.argv[1] = update() 

elif 'progress' in sys.argv[1]:
    sys.argv[1] = progress()    

elif 'list-tasks' == sys.argv[1]:
    with open('task.json', 'r') as f:
        tasks = json.load(f)
    for task in tasks:
        print(f'{task} \n')  