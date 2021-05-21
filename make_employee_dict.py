# Name: Conor Smith
# Date 5/19/21
# Description: A class called employee, that creates an object with four values. Name, ID number, salary, and email address.
# Then has a separate function that takes a list of all those same values and creates employee objects based on the positional order
# of the lists. From the lists, the first name, ID number, salary and email all together become the first employee object, the second name,
# ID number, salary, and email become the second object, etc.

class Employee:
    """the private data members that describe what an employee is to this program, get methods for each"""
    def __init__(self, name, ID_number, salary, email_address):
        self._name = name
        self._ID_number = ID_number
        self._salary = salary
        self._email_address = email_address

    def get_name(self):
        return self._name

    def get_ID_number(self):
        return self._ID_number

    def get_salary(self):
        return self._salary

    def get_email_address(self):
        return self._email_address

def make_employee_dict(list_names, list_ID_number, list_salary, list_email_address):
    """the function that takes lists of names, ID's salaries and emails and creates an object based on those values"""
    employee_dict = {}

    list_len = len(list_ID_number)

    for i in range(list_len):
            name = list_names[i]
            ID_number = list_ID_number[i]
            salary = list_salary[i]
            email = list_email_address[i]

            employee_dict[ID_number] = Employee(name, ID_number, salary, email)
    return employee_dict

#employee_names = ["Jean", "Kat", "Pomona"]
#employee_ID_number = ["100", "101", "102"]
#employee_salary = [30, 35, 28]
#emp_email_address = ["Jean@aol.com", "Kat@aol.com", "Pomona@aol.com"]
#result = make_employee_dict(employee_names, employee_ID_number, employee_salary, emp_email_address)
#print(result["101"].get_salary())
