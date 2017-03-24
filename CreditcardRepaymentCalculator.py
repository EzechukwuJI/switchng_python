 #problem set #1 part one
#
#A program that computes the credit card balance for one year
#Ezechukwu James I. - 10/11/2014
#Duration: about 3hours

#get variables from user
Card_Bal = float(raw_input("Enter the outstanding balance on your credit card: "))

Annual_Int_Rate = ((float(raw_input("Enter annual interest rate: ")))/100)/12
Pay_Back_Rate = (float(raw_input("Enter monthly repayment rate: ")))/100

Total_Intr_Paid = 0
Total_Amount_Paid = 0


#calculate and Print details for the months  
for i in range(1,13,1):
    
    Min_Month_Pay = float(Pay_Back_Rate * Card_Bal)
    Intr_Paid = float(Annual_Int_Rate * Card_Bal)
    Amount_Paid = float(Min_Month_Pay - Intr_Paid)
    Card_Bal = float(Card_Bal - Amount_Paid)
    
    
#Compute total amount and interest  paid for the other months
    Total_Intr_Paid += Intr_Paid
    Total_Amount_Paid += Min_Month_Pay

    
    print "\nFor Month: ", i
    print "=========================="
    print "\n Minimum monthly payment: ", "$",round(Min_Month_Pay,2)
    print " Principal paid: ", "$",round(Amount_Paid,2)

##print " Interest paid: ", "$",round(Intr_Paid,2)
    print " Remaining balance: ", "$",round(Card_Bal,2)

   
  
#print the total values for interest and amount paid
print "\nRESULT:"

print "\n Total amount paid: ", "$",round(Total_Amount_Paid,2)
print " Remaining balance: ","$",round(Card_Bal,2)

raw_input("\n\nPress enter to exit... ")










