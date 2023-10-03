from banking.bank import Bank
from banking.atm import ATM
def main():
    print('Hello Banking App')
    hdfc = Bank('ICICI', 12)
    atm = ATM(hdfc)
    hdfc.create_account('Pradumn' ,'pass', 50000)
    hdfc.create_account('Akshit' ,'pass', 68000)
    hdfc.create_account('Madhav' ,'pass', 79000)
    hdfc.create_account('Harshit' ,'pass', 81000)
    hdfc.info_all__accounts()
    while True:
        if atm.start():
            continue



if __name__=='__main__':
    main()