import sys


athletes = 'luis, caro'

def create_athletes(athletes_name):
    global athletes
    
    if athletes_name not in athletes:
        athletes.append(athletes_name)
        _add_comma()
    else:
        print('Athletes already is in the athletes list ')
        

def _add_comma():
    global athletes
    
    athletes += ','
    
    
def list_athletes():
    global athletes
    
    print(athletes)
    
    
def update_athletes(athletes_name, update_athletes_name):
    global athletes
    
    if athletes_name in athletes:
        athletes = athletes.replace(f'{athletes_name},', f'{update_athletes_name},')
    else:
        print('Athlete is not in the athletes list')
        
        
def _delete_athletes (athletes_name):
    global athletes
    
    if athletes_name in athletes:
        athletes = athletes.replace(athletes_name,'') 
        list_athletes() 
        
def search_athletes(athletes_name):
    list_athletes = athletes.split(',')
    
    for athlete in list_athletes:
        if athlete != athletes_name:
            continue
        else:
            print(f'Athlete {athletes_name} is found')
            return True

def _print_welcome():
    print('Welcome To Villa Mercedes Running Team')
    print('*' *45)
    print('What woudld you like to do today?')
    print('[C]reate Athletes')
    print('[U]pdate Athletes')
    print('[D]elete Athletes')
    print('[S]earch Athletes')
    
    
    
    
def _get_athletes_name():
    athletes_name =None
    
    while not athletes_name:
        athletes_name = input('What is the athletes name?')
        if athletes_name == 'exit':
            break
        
    if not athletes_name:
            sys.exit()
        
    return athletes_name
    
    
def _action():
    global command
    
    command = command.upper()    
    if command == 'C':
        athletes_name = _get_athletes_name ()
        list_athletes()
    elif command == 'D':
        athletes_name = _get_athletes_name ()
        _delete_athletes(athletes_name)
        list_athletes()
    elif command =='U':
        list_athletes()
        update_athletes_name = input('What is the update athletes name ?')
        update_athletes(athletes_name, update_athletes_name + ',')
        list_athletes()
    elif command == 'S':
        athletes_name = _get_athletes_name ()
        found = search_athletes(athletes_name)
        if found:
            print(f'Athlete {athletes_name} is found')
        else:
            print(f'Athlete {athletes_name} is not found')
        list_athletes()
    else:
        print('Invalid command')
        

if __name__ == '__main__':
    _print_welcome()
    command =input()
    _action()
    
    