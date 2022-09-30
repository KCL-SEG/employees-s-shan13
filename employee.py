"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, commissionAmount=0, hrs=0, payPerHr=0, numContract=0, salary=0):
        self.name = name
        self.commissionAmount = commissionAmount
        self.hrs = hrs
        self.payPerHr = payPerHr
        self.numContract = numContract
        self.salary = salary
        self.desc = f"{name} works on"

    def get_pay(self):
        pay = 0
        print(1)
        if self.salary:
            self.desc += f" a monthly salary of {self.salary}. "
            pay += self.salary
        else:
            self.desc += f" a contract of {self.hrs} hours at {self.payPerHr}/hour. "
            pay += self.hrs * self.payPerHr
        if self.numContract:
            self.desc = self.desc[:len(self.desc)-2] + f" and receives a commission for {self.numContract} contract(s) at {self.commissionAmount}/contract. "
            pay += self.numContract*self.commissionAmount
        elif self.commissionAmount:
            self.desc = self.desc[:len(self.desc)-2] + f" and receives a bonus commission of {self.commissionAmount}. "
            pay += self.commissionAmount
        self.desc += f" Their total pay is {pay}."
        return pay

    def __str__(self):
        return self.desc


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', salary=4000)


# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', hrs=100, payPerHr=25)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', salary=3000, numContract=4, commissionAmount=200)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan', hrs=150, payPerHr=25, numContract=3, commissionAmount=220)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', salary=2000, commissionAmount=1500)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', hrs=120, payPerHr=30, commissionAmount=600)

