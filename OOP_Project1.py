class BankAccount:
  bank_name = "HBL"

  def __init__(self, account_holder, balance):
    self.account_holder = account_holder
    self.balance = balance

  def deposit(self,amount):
    self.balance += amount
    

  def withdraw(self,amount):
    if self.balance>=amount:
      print(f"Amount {amount} withdrawl successfully!")
      self.balance-=amount
    else:
      print("Insufficient Balnce")

  def show_balance(self):
    print(f"Total Balnce is {self.balance}")

  @classmethod
  def change_bank_name(self,new_name):
    self.bank_name = new_name
   
  def __del__(self):
    print(f"Destructor called: Account of {self.account_holder} deleted")


name = input("Enter your name to create account: ")
acc1 = BankAccount(name,0)
choice = 'N'
while choice!='Y':
  print("Do you want to deposit money press 1")
  print("Do you want to withdraw money press 2")
  print("Do you want to check balance 3")
  print("Do you want to change bank name 4")
  print("Do you want to see bank name 5")

  choice2 = int(input("Enter your Option: "))
  if choice2==1:
    amount = int(input("Enter amount to deposit: "))
    acc1.deposit(amount)

  elif choice2==2:
    amount = int(input("Enter withdrwal to deposit: "))
    acc1.withdraw(amount)
  elif choice2==3:
    acc1.show_balance()
  elif choice2==4:
    name = input("Enter New Bank Name: ")
    BankAccount.change_bank_name(name)
  elif choice2==5:
    print(f"Bank Name is {BankAccount.bank_name}")

  choice = input("Do you wan tto leave (Y/N): ")
  
