## Perform banking transactions per user
## focus: deposit and withdrawal

###  TODO
# check account exists
# fetch account balance
# check withdrawable amount
# perform withdrawal
# update balance


def check_user_exists(user_account):
    if len(user_account) == 10:
        if user_account.isdigit():
            return True # length matches and no string character found
        else:
            return "\n\n Invalid character found in account number \n"
    return "\n\n User not found! \n"
            


def get_user_bal(user_account):
    if check_user_exists(user_account)== True:
        return True, 2207 * 4
    return False, check_user_exists(user_account)


def withdraw():
    user_account  =  raw_input("Enter account number: ")
    user_name  =   raw_input("Enter your name: ")
    amount_to_withdraw = raw_input("Enter amout to withdraw: ")
    
    if amount_to_withdraw.isdigit():
        user_status, user_bal_or_msg  =  get_user_bal(user_account)
        if user_status: 
            if user_bal_or_msg > float(amount_to_withdraw):  # check withdrawable limit
                new_balance = user_bal_or_msg - float(amount_to_withdraw) # update current balance
                
                print " "
                print "\n\n ============== Transaction Details For %s ===================== \n" %(user_name.title())
                print "Initial balance: #", user_bal_or_msg
                print "Amount withdrawn: #", amount_to_withdraw
                print "Current balance: #", new_balance
            else:
                print "\n\n Maximum withdrawal limit exceeded, enter a lesser amount! \n"
                withdraw()
        else:
            print user_bal_or_msg
            withdraw()
    else:
        print "\n\n Please Enter a valid amount! \n"
        withdraw()

    
def perform_transaction():
    withdraw()






perform_transaction()


    
            
            
