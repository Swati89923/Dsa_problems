class Employee:
    company= 'TATA'

    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

    def increasesalary(self):
        print ('current salary:',self.salary ,'increased salary:', self.salary+self.salary*0.1)


    def give_bonus(self,amount):
        print('current salary',self.salary,'after', self.salary+amount)

    def show_detail(self):
        print(self.name,self.salary)
e1 = Employee('ram',50000)
e1.give_bonus(1000)
print(e1.salary)


class student:

    def __init__(self,name,city):
        self.name=name
        self.city=city
        print(f'self is{self}')
s1=student('surbhi','madhuban')
s2=student('shreya','muzaffarpur')
print(f'(s1)is {s1}')
print(f'(s2) is {s2}')
print(s1.name)
print(s2.name)

#write a progrmme tto find out the area and perimeter of  a rectangle.

class rectangle:

    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth

    def perimeter(self):
        print(f"perimeter is {2*(self.length+self.breadth)}")

    def area(self):
        print(f"area is {self.length*self.breadth}")

r1=rectangle(9,7)
r1.perimeter()
r1.area()

# write a program to consider two people . both of them have accounts in SBI . Show their names, branch(sbi),account number  and balance in their account, perform credit and debit oprn and show the balance in their account after the operation.

class account:

    branch ='sbi'


    def __init__(self,name,account_number,balance):
        self.name=name
        self.account_number=account_number
        self.balance=balance

    

    def check_balance(self,balance):
        print (f"amount is {balance}")

    def deposite(self,amount):
        print(f"new amount is {self.balance+amount}")

    def withdraw(self,amount):
        self.check_balance(self.balance)
        print(f'new_amount is{self.balance-amount}')

p1= account('sita',124456,10000)
p1.withdraw(7000)
print(p1.balance)
           