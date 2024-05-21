class ACCOUNT:
    def __init__(self, bal, acc_no ):
        self.Balence = bal
        self.Acc_no = acc_no
    
    def Debit(self, ammount):
        self.Balence -= ammount
        print("Rs.",ammount,"debited from your acccount")
        print("Total Balence is:",self.Total_bal())

    def Credit(self, ammount):
        self.Balence += ammount
        print("Rs.",ammount,"credited to your account")
        print("Total Balence is:",self.Total_bal())

    def Total_bal(self):
        return self.Balence
    

acc1 = ACCOUNT(10000, "abcd")
acc1.Debit(500)
acc1.Credit(500)