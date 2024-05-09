# class should start with a capital letter
# class Car:
#     def __init__(self, name, engine, wheels, doors, seating):
# instance variables
#         self.name = name
#         self.engine = engine
#         self.wheels = wheels
#         self.doors = doors
#         self.seating = seating


# Innova = Car("Innova", "2399cc", 4, 4, 8)
# Fortuner = Car("Fortuner", "2755cc", 4, 4, 6)
# print(Innova.name, Innova.engine, Innova.wheels, Innova.seating)
# print(Fortuner.name, Fortuner.wheels, Fortuner.engine, Fortuner.seating)

# Task
# Bank account
# 2. Name
# 3. Acc No
# 4. Balance


# class Bank_Account:
#     def __init__(self, Name, Acc_No, Balance):
#         self.Name = Name
#         self.Acc_No = Acc_No
#         self.Balance = Balance

#     def display_balance(self):
#         return f"Your balance is ₹ {self.Balance}"

#     def withdraw(self, amount):
#         if amount <= self.Balance:
#             self.Balance -= amount
#             return f"Success, Your balance is ₹ {self.Balance}"
#         else:
#             return "Insufficient funds"

#     def deposit(self, amount):
#         self.Balance += amount
#         return f"Success, Your balance is ₹ {self.Balance}"


# # Task 1
# person1 = Bank_Account("Sai Ganesh", 39443, 65000)
# person2 = Bank_Account("Mathesh", 12312, 70000)
# person3 = Bank_Account("Amisha", 23434, 50000)
# print(person1.Name, person1.Acc_No, person1.Balance)
# print(person2.Name, person2.Acc_No, person2.Balance)
# print(person3.Name, person3.Acc_No, person3.Balance)
# # Task 2
# print(person1.display_balance())  # your balance is ₹ 65000

# # Task 3
# person2.withdraw(10_000)  # Success your balance is ₹
# print(person2.withdraw())

# # Task 4
# # person1.deposit(20_000)
# print(person1.deposit(20000))


# Encapsulation - properties + actions (logic)
# class Bank_Account2:
#     # class variable | All your instances share the class variable
#     interest_rate = 0.02

#     def __init__(self, Name, Acc_No, Balance):
#         # instance variable
#         self.Name = Name
#         self.Acc_No = Acc_No
#         self.Balance = Balance

#     def display_balance(self):
#         return f"{self.Name}, Your balance is ₹ {self.Balance}"

#     def withdraw(self, amount):
#         pass

#     def deposit(self, amount):
#         pass

#     def apply_interest(self):
#         self.Balance += self.Balance * self.interest_rate
#         return f"{self.Name}, Your balance is ₹ {self.Balance}"


# tonika = Bank_Account2("Tonika", 1211, 1_50_000)
# manasa = Bank_Account2("Manasa", 1212, 80_000)

# # Task 4
# # After 1 year
# tonika.apply_interest()
# print(tonika.display_balance())


# # static method vs class method | Both decorators
# # super charge to the normal method
# # static meth0d
# # Normal function
# # perimeter of circle =  2*phi*r


# class Circle:
#     pi = 3.14

#     def __init__(self, radius):
#         self.radius = radius

#     @staticmethod
#     def perimeter(radius):
#         return 2 * Circle.pi * radius

#     @classmethod
#     def from_diameter(cls, diameter):
#         radius = diameter / 2
#         return cls(radius)

#     def calculate_area(self):
#         return Circle.pi * self.radius**2


# # Normal function but inside class | no access to self
# print(Circle.perimeter(2))

# # Instance method
# circle1 = Circle(4)
# print(circle1.calculate_area())


# # Class method - to construct the object
# circle_from_dia = Circle.from_diameter(10)
# print(circle_from_dia.calculate_area())  # 78.5


# get_total_no_accounts(), update_interest_rate()


class Bank2:
    # Class variable | All your instance share the class variable
    interest_rate = 0.02
    total_accounts = 0

    def __init__(self, acc_no, name, balance):
        # instance variable
        self.acc_no = acc_no
        self.name = name
        self.__balance = balance
        Bank2.total_accounts += 1

    def display_balance(self):
        return f"Your balance is: ₹{self.__balance:,}"

    def withdraw(self, amount):
        if self.__balance - amount >= 0:
            self.__balance -= amount
            return f"Success. {self.display_balance()}"
        else:
            return f"Insufficient funds. {self.display_balance()}"

    def deposit(self, amount):
        if amount >= 0:
            self.__balance += amount
            return f"Success. {self.display_balance()}"
        else:
            return f"Invalid amount. {self.display_balance()}"

    def apply_interest(self):
        accumulated_interest_amt = self.__balance * Bank2.interest_rate
        self.__balance += accumulated_interest_amt
        return f"Interest received. ₹{accumulated_interest_amt}"

    @classmethod
    def get_total_no_accounts(cls):
        return cls.total_accounts

    @classmethod
    def update_interest_rate(cls, new_rate):
        cls.interest_rate = new_rate
        return f"Interest rate updated to {new_rate * 100}%"


sneha = Bank2(128, "Sneha", 1_00_000)
siva = Bank2(129, "Siva", 90_000)

# Test methods
print(Bank2.get_total_no_accounts())  # Output: 2
print(Bank2.update_interest_rate(0.10))  # Output: Interest rate updated to 10.0%
print(sneha.apply_interest())  # Output: Interest received. ₹2000.0
print(sneha.display_balance())  # Output: Your balance is: ₹102,000.0

# Access specifiers
# 1. private -> __balance(double underscore)
# 2. protected -> _balance(single underscore)
# 3. public -> balance (no underscore)
# Conventions
# 1. privatize all instance & class variables
# 2. Access to instance & class variables - through - public - methods


# class Animal:
#     def __init__(self, name):
#         self.name = name

#     def speak(self):
#         return "Some sound"


# class Dog(Animal):
#     def __init__(self, name, speed):
#         super().__init__(name)
#         self.speed = speed

#     def run(self):
#         return "Dog wails it"

#     def speak(self):
#         return "woof"

#     def speed_bonus(self):
#         return f"{self.name} is running at {self.speed * 20} km/h"


# toby = Animal("toby")
# print(toby.speak())
# maxy = Dog("maxy", 20)
# print(maxy.name)
# print(maxy.run())
# print(maxy.speak())
# print(maxy.speed_bonus())


# Savings Account  -   interest_rate -> 0.05
# Task 5
class Account:
    def __init__(self, acc_number, holder_name, balance):
        self.acc_number = acc_number
        self.holder_name = holder_name
        self.balance = balance

    def get_balance(self):
        return self.balance


class SavingsAccount(Account):
    interest_rate = 0.05

    def apply_interest(self):
        interest_amount = self.balance * self.interest_rate
        self.balance += interest_amount
        return (
            f"balance after interest in {self.holder_name} account is",
            interest_amount,
        )


class Curr_Account(Account):
    transaction_fee = 10

    def withdraw(self, amount):
        if self.balance >= amount + self.transaction_fee:
            self.balance -= amount + self.transaction_fee
            return f"Withdrawal of {amount} successful. Transaction fee: {self.transaction_fee}"
        else:
            return "Insufficient balance for withdrawal"


# Task 5
sabesh = SavingsAccount(131, "Sabesh", 80000)
print(sabesh.apply_interest())  # 5%
print(sabesh.get_balance())

# Task 6 - withdraw - transaction fee - 10 rupee
tanishq = Curr_Account(132, "Tanishq", 90000)
print(tanishq.withdraw(1000))
print(tanishq.withdraw(10000))
print(tanishq.get_balance())

# common across objects - class variable (cls)          - no of eyes
# unique across objects - instance variable (self)      - size of nose


# magic methods __str__ (human readable)
# __repr__ (debugging)
# __init__  --> dunder methods
class Cat:
    def __init__(self, name, speed):
        self.__name = name
        self.__speed = speed

    # Override - (human readable)
    def __str__(self):
        # Human readable
        return f"Hi, I am {self.__name} with speed {self.__speed}"

    # Override -  (debugging)
    def __repr__(self):
        # Human readable
        return f"Cat('{self.__name}', {self.__speed})"

    def __add__(self, other):
        return self.__speed + other.__speed

    # Polymorphism:  Method overriding
    def speak(self):
        return "Meow!! 🐈"


pichu = Cat("pichu", 30)
snowbell = Cat("snowbell", 10)

print(pichu)
print(repr(pichu))
print(repr(snowbell))

print(pichu + snowbell)


# x = [5, 6, 7]
# print(dir(x))
def to_upper_case(text="Sanju Samson"):
    return text.upper() + "🎉"


print(to_upper_case())
