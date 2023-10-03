class BankAccount:
    def __init__(self, account_holder, password, account_type, initial_balance, interest_rate):
        self.account_holder = account_holder
        self.account_type = account_type
        self.balance = initial_balance
        self.password = password
        self.min_balance_required = 5000
        self.od_limit = 0
        self.od_fee = 0
        self.interest_rate=interest_rate

    def deposit(self, amount, password):
        if self.password == password:
            self.balance += amount
        else:
            print("Withdrawal not successful.")
        

    def withdraw(self, amount ,password):
        if self.account_type == "Savings" and self.balance - amount >= self.min_balance_required and self.password == password:
                self.balance -= amount
        elif self.account_type == "Current" and self.balance >= amount and self.password == password:
            self.balance -= amount
        elif self.account_type == "Overdraft" and self.password == password:
            self.od_limit = 0.1 * self.balance
            max_withdrawal = self.balance + self.od_limit
            if amount <= max_withdrawal:
                self.od_fee = 0.01 * amount - self.balance
                self.balance -= amount - self.od_fee
            else:
                print("Withdrawal not allowed.")
        else :
            print("Withdrawal not successful.")



    def credit_interest(self):
        if not self.balance<=0:
            interest = self.balance * self.interest_rate/1200
        if self.account_type == "Savings" or self.account_type == "OverDraft" :
            self.balance += interest
        
       

class Bank():
    def __init__(self):
        self.accounts = []

    def open_account(self, account_holder, password, account_type, initial_balance, interest_rate):
        account = BankAccount(account_holder, password, account_type, initial_balance,interest_rate)
        self.accounts.append(account)
        return account

    def transfer(self, sender, receiver, amount, password):
        if sender in self.accounts and receiver in self.accounts and sender.password == password:
            sender.withdraw(amount)
            receiver.deposit(amount)
        else:
            print("Invalid account.")


class ATM:
    def __init__(self, bank):
        self.bank = bank

    def interact(self):
        while True:
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Transfer")
            print("4. Check Balance")
            print("5. Credit Interest")
            print("6. Exit")


            choice = input("Enter your choice: ")

            if choice == "1":
                account = input("Enter your account holder's name: ")
                amount = float(input("Enter the deposit amount: "))
                passwrd_attempt = input("Enter your account password : ")
                for acc in self.bank.accounts:
                    if acc.account_holder == account and acc.password == passwrd_attempt:
                        acc.deposit(amount,acc.password)
                        print("Deposit successful.")
                        break
                else:
                    print("Account not found.")

            elif choice == "2":
                account = input("Enter your account holder's name: ")
                amount = float(input("Enter the withdrawal amount: "))
                passwrd_attempt = input("Enter your account password : ")

                for acc in self.bank.accounts:
                    if acc.account_holder == account and acc.password == passwrd_attempt:
                        acc.withdraw(amount,acc.password)
                        print("Withdrawal successful.")
                        break
                else:
                    print("Account not found.")

            elif choice == "3":
                sender = input("Enter the sender's account holder's name: ")
                receiver = input("Enter the receiver's account holder's name: ")
                amount = float(input("Enter the transfer amount: "))
                passwrd_attempt = input("Enter your account password : ")

                sender_acc = None
                receiver_acc = None
                for acc in self.bank.accounts:
                    if acc.account_holder == sender:
                        sender_acc = acc
                    if acc.account_holder == receiver:
                        receiver_acc = acc
                if sender_acc and receiver_acc and sender_acc.password == passwrd_attempt :
                    self.bank.transfer(sender_acc, receiver_acc, amount)
                    print("Transfer successful.")
                else:
                    print("Sender or receiver account not found.")

            elif choice == "4":
                 account = input("Enter your account holder's name: ")
                 passwrd_attempt = input("Enter your account password : ")

                 for acc in self.bank.accounts:
                    if acc.account_holder == account and acc.password == passwrd_attempt:
                        print(f'Account Balance is : {acc.balance}')

            elif choice == "5":
                account = input("Enter your account holder's name: ")
                passwrd_attempt = input("Enter your account password : ")
                for acc in self.bank.accounts:
                    if acc.account_holder == account and acc.password == passwrd_attempt:
                        acc.credit_interest()
                        print("Interest Credited")

            elif choice == "6":
                break
  
            else:
                print("Invalid choice. Try again.")

if __name__ == "__main__":
    icici = Bank()
    hdfc = Bank()
    a1 = icici.open_account('Vivek', '123', 'Savings', 50000,5)
    a2 = icici.open_account('Sanjay','321', 'Overdraft', 50000,5)
    a3 = hdfc.open_account('Vivek','432', 'Savings', 60000,6)
    atm = ATM(hdfc)
    atm.interact()
