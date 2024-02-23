# BÀI 50 
# function that can add new employee with ID, name, age, phone, email, salary, date of birth and write to a text file
def addemployee():
    numofemployee = int(input('number of employee: '))
    for i in range(numofemployee):
        IDem = input('ID (8 digits long): ')
        name = input('name: ')
        age = input('age: ')
        phone = input('phone: ')
        email = input('email: ')
        salary = input('salary: ')
        dob = input('date of birth (dd/mm/yyyy): ')
        with open("data.txt", "a") as f:
            f.write("ID:"+ IDem + " " + "Name:" + name + " " + "Age:" + age + " " + "Phone:" + phone + " " + "Email:" + email + " " + "Salary:" + salary + " " + "DateOFBirth:" + dob + "\n")
#  function that can search for employee by name 
def searcheremployee():
    search = input('Enter name: ')
    with open("data.txt", "r") as f:
        for line in f:
            if search in line:
                print(line)
                return True
# function to delete a employee 
def deleteemployee():
    search = input('Enter name: ')
    delete = input('Do you want to delete this employee? (yes/no): ')
    with open("data.txt", 'r') as f:
    # read an store all lines into list
        lines = f.readlines()
    with open("data.txt", "w") as f:
        for line in lines:
            if search in lines:
                print(line)
                if delete == 'yes':
                    f.write(line)
                else:
                    print('invalid input')
# update employee use the result from search function
def updateemployee():
    if searcheremployee() == True:
        with open("data.txt", 'w') as f:
            IDem = input('ID (8 digits long): ')
            name = input('name: ')
            age = input('age: ')
            phone = input('phone: ')
            email = input('email: ')
            salary = input('salary: ')
            dob = input('date of birth (dd/mm/yyyy): ')
            f.write("ID:"+ IDem + " " + "Name:" + name + " " + "Age:" + age + " " + "Phone:" + phone + " " + "Email:" + email + " " + "Salary:" + salary + " " + "DateOFBirth:" + dob + "\n")
# sort employee by salary
def sortemployee():
    with open("data.txt", 'r') as f:
        lines = f.readlines()
    with open("data.txt", "w") as f:
        lines.sort(key=lambda x: x.split()[-2])
        for line in lines:
            print(line)

def main():
    while True:
        choice = input(' what do you want to do (type "exit" to quit) : add, search, delete, update, sort:')
        if choice == 'add':
            addemployee()
        elif choice == 'search':
            searcheremployee()
        elif choice == 'delete':
            deleteemployee()
        elif choice == 'update':
            updateemployee()
        elif choice == 'sort':
            sortemployee()
        elif choice == 'exit':
            print('goodbye')
            break
main()