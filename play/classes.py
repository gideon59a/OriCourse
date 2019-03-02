## Ori's Python course
# import sys
# sys.path.append('../') #this has been added so can be found in cmd window

class Triangle:
    '''
    Exercise 1
    •	Create a class, Triangle. It should have attributes which represent it's angles.
    •	Create a variable named number_of_sides and set it equal to 3.
    •	Create a method named check_angles. It should return True if the sum of all it's angles equals 180, and False otherwise.
    •	Create a Triangle type object which has three angles that sum to 180 (e.g. 90, 30, 60).
    •	Print my_triangle.check_angles().
    •	Create a Triangle type object which has three angles that sum to 190 (e.g. 90, 40, 60).
    •	Print my_triangle.check_angles().
    '''
    def __init__(self,angle_a,angle_b,angle_c):
        self.angles=[]
        self.angles.append(angle_a)
        self.angles.append(angle_b)
        self.angles.append(angle_c)
        print ('Triangle with angles {angles} has been created'.format(angles=self.angles))
        print ('my triangle is', self.check_angles())
        pass

    def check_angles(self):
        if (sum(self.angles) == 180):
            return True
        else:
            return False

class Employee:
    '''
    Exercise 2
    •	Create an Employee class.
    •	Each Employee has a name, id, and department name he belongs to
    •	Create a Department class.
    •	Each Department has a name and the list of its Employees.
    •	Create a Department method which returns the number of employees in the department.
    •	Create Department methods that allow to add and remove an Employee.
    •	Create a Department and add 3 Employees.
    •	Print the number of Employees Department holds.
    •	Remove one Employee from the Department
    •	Print the number of Employees Department holds.
    '''
    def __init__(self, name, eid, department):
        self.employee = {}
        self.employee[eid] = [name,department]
        #self.employee ['name'] =
        #self.id = eid
        #self.department = department
        print  ('Employee ',self.employee.keys(), self.employee[eid])

class Department:
    def __init__(self, name):
        self.name = name
        self.employees_list = []
        pass

    def add_employee(self,**employee):
        print ('e',employee.keys())
        self.employees_list.append(employee)
        pass

    def add_employee2(self,employee_dict):
        print ('e',employee_dict.keys())
        self.employees_list.append(employee_dict)
        pass

    def remove_employee(self,eid):
        found=False
        for item in self.employees_list:
            print('item list is: ',item)

            for key, value in item.items():
                print ('kv =', key, value)
                if key==eid:
                    found=True
                    print (eid,'found')
                    self.employees_list.remove(item)
        if found==False:
            print (eid, 'not found')

    def num_of_employees(self):
        return len(self.employees_list)


if __name__ == '__main__':

    #print ("Exercise 1")
    #my_triangle = Triangle(10,20,150)
    ##print ('my triangle is',my_triangle.check_angles())
    #my_triangle2 = Triangle(10, 20, 160)

    print("\nExercise 2\n")
    my_depart = Department('rnd')
    print ('number of employees',my_depart.num_of_employees())

    new_employee_c = Employee('Jhon','2001','rnd')
    #print ('printing class dict: ',new_employee_c.employee)
    my_depart.add_employee(**new_employee_c.employee)

    new_employee_c = Employee('Naama','4004','rnd')
    my_depart.add_employee(**new_employee_c.employee)

    new_employee = Employee('mama','9009','home')
    my_depart.add_employee2(new_employee.employee)

    my_depart.remove_employee('9009')
    print('number of employees', my_depart.num_of_employees())
