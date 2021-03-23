from datetime import datetime

employees = {
    'Adam' : '001',
    'Brian' : '002',
    'Carl' : '003',
    'David' : '004',
    'Earl' : '005',
    'Frank' : '006'
    }
reversed_roster = dict(map(reversed, employees.items())) # reverses order
# so ID number becomes keys
now = datetime.now()
current_time = now.strftime("%I:%M %p")

def emp_or_owner():
    emp_or_owner = input("Are you an employee or the owner? ")
    if emp_or_owner == 'employee':
        emp_functions()
    elif emp_or_owner == 'owner':
        owner_functions()
    elif emp_or_owner == 'end':
        quit(emp_or_owner)
        
def emp_functions():
    emp_id = input('Enter employee ID: ')
    res = dict((v,k) for k,v in employees.items())
    if emp_id not in res:
        print("Employee ID not found. Please re-enter your employee ID.")
        return emp_functions()
    else:
        print(f"Hello {emp_id}, what would you like to do? ")
        choices = ['Clock In', 'Clock Out', 'View My Pay']
        print('Options:')
        print('Press the corresponding number.')
        for index, item in enumerate(choices):
            print(f"{index + 1}.", item)
        
        emp_task = input("I want to: ")
        
        if emp_task == '1':
            clock_in = input("Are you ready to clock in now? ")
            if clock_in == 'yes' or 'y':
                print(f"Ok {emp_id}. You clocked in at {current_time}."
                      "Have a good day!")
                return emp_or_owner()
            elif clock_in == 'no' or 'n':
                print(f"Ok {emp_id}. You are still clocked in.")
                return emp_or_owner()
        
        elif emp_task == '2':
            clock_out = input("Are you ready to clock out now? ")
            if clock_out == 'yes' or 'y':
                print(f"Ok {emp_id}, you clocked out at {current_time}.")
                new_task = input("Would you like to do anything else? ")
                if new_task == 'yes' or 'y':
                    return emp_functions()
                elif new_task == 'no' or 'n':
                    print(f"Ok {emp_id}, have a good day!")
                    return emp_or_owner()
        
        elif emp_task == '3':
            hours = int(input('How many hours did you work? '))
            rate = int(input('How much do you earn per hour? $'))
            if hours < 40:
                pay1 = hours * rate
                print(f'Your pay will be ${pay1} before taxes.')
                return emp_or_owner()
            else:
                overtime_hours = hours - 40
                new_rate = rate * 1.5
                pay2 = float(40 * rate) + float(overtime_hours * new_rate)
                print(f'Your pay will be ${pay2} before taxes.')
                return emp_or_owner()

def owner_functions():
    owner_password = input("Enter owner's password: ")
    if owner_password != '1234':
        print("Incorrect password. Please re-enter your password.")
        return owner_functions()
    else:
        print("Hello, what would you like to do? ")
        choices = ['Calculate Paychecks', 'Schedule Employees',
                   'View Time Cards', 'Employee Roster Options']
        print('Options:')
        print('Press the corresponding number.')
        for index, item in enumerate(choices):
            print(f"{index + 1}.", item)
            
        owner_task = input("I want to: ")
        if owner_task == '1':
            emp = input("Enter the employee's ID: ")
            res = dict((v,k) for k,v in employees.items())
            if emp not in res:
                print("Employee ID not found. Please re-enter"
                      " the employee ID.")
                return owner_functions()
            else:
                hours = int(input(f'How many hours did {emp} work? '))
                rate = int(input(f'How much does {emp} earn per hour? $'))
                if hours < 40:
                    pay1 = hours * rate
                    print(f"{emp}'s pay will be ${pay1} before taxes.")
                    next_emp = input("Would you like to calculate pay"
                    " for another employee? ")
                    if next_emp == 'yes' or 'y':
                        return owner_functions()
                    elif next_emp == 'no' or 'n':
                        return emp_or_owner()
                else:
                    overtime_hours = hours - 40
                    new_rate = rate * 1.5
                    pay2 = float(40 * rate) + float(overtime_hours 
                                                    * new_rate)
                    print(f"{emp}'s pay will be ${pay2} before taxes.")
                    next_emp = input("Would you like to calculate pay"
                    " for another employee? ")
                    if next_emp == 'yes' or 'y':
                        return owner_functions()
                    else:
                        return emp_or_owner()
emp_or_owner()
