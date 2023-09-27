class Bank:
    pass

def interest_paid(c):
    c.acc_balance+=((c.acc_balance*c.interest_rate)/1200)

def deposit(c):
    if c.acc_deposit>0:
        c.acc_balance += c.acc_deposit
        print("Deposit successful!",end="\n\n")
    else:
        print("Deposit not successful!",end="\n\n")

def withdraw(c,password):
    if c.acc_amt_withdraw>0 and c.acc_amt_withdraw < c.acc_balance and c.acc_password==password:
        c.acc_balance-= c.acc_amt_withdraw
        print("Withdraw successful!",end="\n\n")

    else:
        print("Withdraw not successful!",end="\n\n")

def account_info(c):
    return f"Account number : {c.acc_number}\nName : {c.acc_holder_name}\nPassword : {c.acc_password}\nAccount Balance: Rs.{c.acc_balance}\nInterest Rate : {c.interest_rate}%"

def create(account_number,name,password,balance,interest,deposit,withdraw):    
    bank=Bank()
    bank.acc_number=account_number
    bank.acc_holder_name=name
    bank.acc_password=password
    bank.acc_balance=balance
    bank.interest_rate=interest
    bank.acc_deposit=deposit
    bank.acc_amt_withdraw=withdraw
    return bank

def main():
    c = create(5008700045,"Pradumn","Pradumn@123",10000,8,3000,2000)
    if isinstance(c,Bank):
        interest_paid(c)
        deposit(c)
        withdraw(c,"Pradumn@123")
        print(account_info(c))
    else:
        print("Enter valid object")

if __name__ == "__main__":
    main()
    