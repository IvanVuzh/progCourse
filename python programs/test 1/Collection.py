from Employee import Employee
from Validators import Validation


class Collection:
    def __init__(self):
        self.list_of_employees = []

    def add_worker(self, worker):
        self.list_of_employees.append(worker)

    def read(self, file_name):
        if Validation.file_not_empty(file_name):
            f = open(file_name)
            lines = f.readlines()
            # print(to_add.make_str())
            line_number = 0
            # print(len(lines))
            # print(lines)
            for i in range(len(lines)):
                to_add = Employee
                line = lines[i]
                if i != len(lines) - 1:
                    line = line[:-1]
                # print("line is:", line)
                if Employee.str_to_employee(to_add, line) != 1:
                    to_add = Employee.str_to_employee(to_add, line)
                    self.list_of_employees.append(to_add)
                else:
                    print("Data error in line " + str(i + 1))
                line_number += 1

    def print(self):
        for employee in self.list_of_employees:
            print(employee.make_str_for_print())

    def rewrite_file(self, file_name):
        if Validation.file_exists(file_name):
            f = open(file_name, "w")
            for i in range(len(self.list_of_employees)):
                cut = i == len(self.list_of_employees) - 1
                self.list_of_employees[i].append_to_file(file_name, cut)

    def all_salary(self):
        res = 0
        for employee in self.list_of_employees:
            res += employee.salary_summary()
        return res
