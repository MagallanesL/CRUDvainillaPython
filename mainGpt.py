athletes = ['Luis', 'caro']

def create_athletes(athletes_name):
    global athletes
    
    if athletes_name not in athletes:
        athletes.append(athletes_name)
        _add_comma()
    else:
        print('Athletes already is in the athletes list')
        

def _add_comma():
    global athletes
    
    athletes[-1] += ','
    
    
def list_athletes():
    global athletes
    
    print(athletes)
    
    
def update_athletes(athletes_name, update_athletes_name):
    global athletes
    
    if athletes_name in athletes:
        index = athletes.index(athletes_name)
        athletes[index] = update_athletes_name
        _add_comma()
    else:
        print('Athlete is not in the athletes list')

        

    
def _print_welcome():
    print('Welcome To Villa Mercedes Running Team')
    print('*' *45)
    print('What would you like to do today?')
    print('[C]reate Athletes')
    print('[U]pdate Athletes')
    print('[D]elete Athletes')
    
    
def _get_athletes_name():
    return input('What is the athlete\'s name?')
    
    
def _action():
    global command
    
    command = command.upper()    
    if command == 'C':
        athletes_name = _get_athletes_name()
        create_athletes(athletes_name)
        list_athletes()
    elif command == 'D':
        athletes_name = _get_athletes_name()
        if athletes_name in athletes:
            athletes.remove(athletes_name)
        else:
            print('Athlete is not in the athletes list')
        list_athletes()
    elif command =='U':
        athletes_name = _get_athletes_name()
        if athletes_name in athletes:
            update_athletes_name = input('What is the updated athlete\'s name? ')
            update_athletes(athletes_name, update_athletes_name)
        else:
            print('Athlete is not in the athletes list')
        list_athletes()
    else:
        print('Invalid command')
        

if __name__ == '__main__':
    _print_welcome()
    command = input()
    _action()