import datetime
from Validators import Validation


class Employee:
    attr_dict = {'name': 'name',
                 'salary': 'salary',
                 'first_working_date': 'first_working_date',
                 'last_working_date': 'last_working_date'}
    error_messages = ["Error in line (wrong name in line)",
                      "Error in line (wrong first working date in line)",
                      "Error in line (wrong last working date in line)"]

    def __init__(self, dict_of_data):
        for key in dict_of_data:
            # print("key is", key, "\t value is", dict_of_data[key])
            setattr(self, key, dict_of_data[key])

    def get_last(self):
        return getattr(self, 'last_working_date')

    def get_first(self):
        return getattr(self, 'first_working_date')

    def get_based_salary(self):
        return getattr(self, 'salary')

    def worked_month(self):
        last = self.get_last().split("-")
        first = self.get_first().split("-")
        res = (last[3] - first[3]) * 12 + (last[1] - first[1])
        return res

    def salary_summary(self):
        res = 0
        worked = self.worked_month()
        adder = 0
        while worked != 0:
            if worked >= 6:
                worked -= 6
                res += 6 * self.get_based_salary() * adder
                adder += 0.15
            else:
                res += worked * self.get_based_salary() * adder
                worked = 0
                adder += 0.15
                print (res)
        return res

    def str_to_employee(self, string):
        line = string.split(", ")
        all_is_validated = True
        error_list = []
        line_iter = 0
        # print(line)
        for field in self.attr_dict:
            # print("Iter =", line_iter)
            validator_name = Validation.validators_of_employee_fields[field]
            if not getattr(Validation, validator_name)(line[line_iter]):
                error_list.append(line_iter)
                all_is_validated = False
            if line_iter != len(line):
                line_iter += 1
        if not Validation.worked_time_validation(line[2], line[3]):
            all_is_validated = False
        if all_is_validated:
            dictionary = self.attr_dict.copy()
            i = 0
            for name in self.attr_dict:
                # print(dictionary[name] + "=" + line[i])
                dictionary[name] = line[i].lower()
                # print(dictionary[name])
                i += 1
            # print("Created dictionary is", dictionary)
            res = Employee(dictionary)
            # ("Employee added")
            return res
        else:
            for error in error_list:
                print(self.error_messages[error])
            # print("######## Caught an error in data file in line", line_number + 1, "########")
            return 1

    def make_str_for_print(self):
        to_print = "#################################################################\n" \
                   "Employee info: \n"
        for name in self.attr_dict:
            to_print += name + ': ' + str(getattr(self, self.attr_dict[name])) + '\n'
        to_print += "#################################################################"
        return to_print

    def make_str_for_file(self):
        to_write = ''
        for q in self.attr_dict:
            to_write += str(getattr(self, self.attr_dict[q])) + ', '
        to_write = to_write[:-2]
        to_write += '\n'
        return to_write

    def append_to_file(self, file_name, cut):
        if Validation.file_exists(file_name):
            file = open(file_name, "a")
            line = self.make_str_for_file()
            if cut:
                line = line[:-1]
            file.write(line)
        else:
            print("Error occurred while trying to append to file. File does no exists")
