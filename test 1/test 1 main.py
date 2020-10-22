from Date import Date
from Validators import Validation
from Employee import Employee
from Collection import Collection


def main():
    file_name = input("Enter file name: ")
    while not Validation.file_exists(file_name):
        file_name = input("Reenter file name: ")
    employees = Collection()
    employees.read(file_name)
    menu_choice = 0
    while menu_choice != 4:
        print("You are in main menu. Possible options:\n"
              "1 - add an employee\n"
              "2 - show all salary\n"
              "3 - show all employees\n"
              "4 - exit program\n"
              "Choose your option: ")
        menu_choice = input()
        if menu_choice == 1:
            data = input("Enter a LINE which is similar to (with a ', ' as a delimiter or enter 0 to skip)\n")
            if data == 0:
                pass
            new_empolyee = Employee(data)
            employees.add_worker(new_empolyee)
        elif menu_choice == 2:
            print(employees.all_salary())
        elif menu_choice == 3:
            employees.print()
        elif menu_choice == 4:
            print("Have a nice day! Goodbye!")


main()
