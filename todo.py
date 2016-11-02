import pprint #like var_dump
import sys
import os #files
import csv 


DATABASEFILE="database.csv"
CHECKBOX_COLUMN_NAME='Done'
TODO_COLUMN_NAME='To do'

class bcolors:
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    Default = '\033[99m'


def clear_console():
    """Clearing console"""
    os.system('cls' if os.name=='nt' else 'clear')


def print_warning(warning, type='yellow'):
    """Information print"""
    if type=='yellow':
        print(bcolors.WARNING+"------------------------------\n"
        + warning
        +" \n------------------------------"+bcolors.ENDC)
    
    if type=='red':
        print(bcolors.FAIL+"------------------------------\n"
        + warning
        +" \n------------------------------\n"+bcolors.ENDC)
    if type=='green':
        print(bcolors.OKGREEN+"------------------------------\n"
        + warning
        +" \n------------------------------\n"+bcolors.ENDC)    



def add(item_to_add):
    """Add item to list in file"""

    with open(DATABASEFILE, 'a' ) as csvfile:
        fieldnames = [CHECKBOX_COLUMN_NAME, TODO_COLUMN_NAME]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writerow({CHECKBOX_COLUMN_NAME: ' ', TODO_COLUMN_NAME: item_to_add})
    clear_console()
    print_warning("Item added.", 'green')  
    todo_list(write=True)
    

def save_to_file(data):
     """Save data to file"""

     with open(DATABASEFILE, 'w') as csvfile:
        fieldnames = [CHECKBOX_COLUMN_NAME, TODO_COLUMN_NAME]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        for item in data:
            writer.writerow({CHECKBOX_COLUMN_NAME: item[1], TODO_COLUMN_NAME: item[2]})


def todo_list(write=0):
    """List of todo"""
    
    with open(DATABASEFILE, newline='') as f:
        reader = csv.reader(f)
        list_todo = []
        if write is True:
            print("You saved the following to-do items: \n ")
            i=0
            for row in reader:
                if i != 0:
                    print(" %3d." % (i) + " [" + str(row[0]) + "]  " + str(row[1]))
                list_todo.append([i, row[0], row[1]])
                i+=1
            print()
        i=0 
            
        for row in reader:
            list_todo.append([i, row[0], row[1]])
            i+=1

        return list_todo    


def mark_todo(mark=True):
    """marking items"""    
    
    td_list=todo_list(True) #write todo list
    while True:
        try:        
                if (mark==False):
                    mark_number=input('Which one you want to unmark (or Press Enter to leave): ')
                    if mark_number=='x' or mark_number=='':
                        clear_console()
                        todo_list(write=True)
                        break
                    td_list[int(mark_number)][1]=str(' ')
                    clear_console()
                    print_warning("Item unmarked.") 
                else:
                    mark_number=input('Which one you want to mark as completed (or Press Enter to leave): ')
                    if mark_number=='x' or mark_number=='':
                        clear_console()
                        todo_list(write=True)
                        break
                    td_list[int(mark_number)][1]='x'  
                    clear_console()
                    print_warning("Item marked.")   
                save_to_file(td_list) 
                todo_list(write=True)

        except ValueError:
                
                clear_console()
                print_warning("It is not a number.",'red') 
                mark_todo()
        except IndexError:
                clear_console()
                print_warning("There is no item with this ID",'red') 
                mark_todo()

        
  
def archive():
    """delete marked items from list"""

    to_do_list=todo_list(0)
    newtodolist=[]
    for item in to_do_list:
        if item[1] != 'x':
            newtodolist.append([' ', item[1], item[2]]) 
               
    save_to_file(newtodolist)
    print_warning("Deleted marked items", 'red')
    todo_list(write=True)


def checkdatabase():
    """checking database file, if !exist than create it""" 

    if not os.path.exists(DATABASEFILE):
        with open(DATABASEFILE, 'w') as csvfile:
            fieldnames = [CHECKBOX_COLUMN_NAME, TODO_COLUMN_NAME]
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
    

def main():
    clear_console()
    todo_list(write=True)

    while True:
       
        action=input( "Please specify a command [add, mark, unmark, archive, x to exit]: ")
        clear_console()

        if action == "add": #loop: adding todo items
            item_to_add=' '
            todo_list(write=True)
            while item_to_add!='':
                item_to_add=input('Add an item (or press enter to leave): ')
                if (item_to_add!=''):
                    add(item_to_add)
                else:
                    clear_console()
                    todo_list(write=True)
                        

        elif action == "list": #this is not used, list is always visible
            clear_console()
            todo_list(write=True)

        elif action == "mark":
            mark_todo()
            

        elif action == "unmark":
            mark_todo(False)
             

        elif action == "archive":
            archive()
            

        elif action=="x": #exit program
            break    
        
        else:
            print_warning("Error: wrong command!", 'red') 
            todo_list(write=True)
            



checkdatabase() #if file doesn't exist than create it'
main()