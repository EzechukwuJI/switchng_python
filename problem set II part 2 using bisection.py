# problem set 1 part 2
# a program that Computes required minimum monthly deposit to pay off
# a credit card deposit in 12 months or less
#
# Ezechukwu James I - 12/11/2014

#get input from user - integer values
curr_card_bal = float(raw_input("Enter the outstanding balance on your card: "))
annual_intr_rate = float(raw_input("Enter annual interest rate: "))/100 #converts percent to decimal



monthly_intr_rate = annual_intr_rate/12 # calculates required variables

# initializes variables

min_dep = curr_card_bal/12  # let lower bound be one-twelth of the card bal without interest
max_dep = (curr_card_bal * (1 + (annual_intr_rate/12.0))**12.0)/12  # one-twelfth of the cardbal with compounded interest


req_min_dep = (max_dep + min_dep)/2
req_num_months = 0
outstanding_bal = curr_card_bal
num_iter = 0


while (curr_card_bal > 0):
	req_min_dep += 0.001 		# increase initial deposit by $10
	num_iter += 1              
	curr_card_bal = outstanding_bal # reset card balance to initial balance
	req_num_months = 0              # reset the number of months to zero

	
	for i in range(12):
		curr_card_bal = (curr_card_bal * (1 + monthly_intr_rate)) - req_min_dep
		req_num_months += 1	
		if curr_card_bal < 0: # stop execution when card balance drops below zero
			break
print " >>> RESULT <<<"
print "-----------------"
print "\n Monthly payment to pay off debt in 1 year: ", round(req_min_dep,2)	
print " Number of months needed: ", req_num_months
print " Balance: ", round(curr_card_bal,2)
print "Number of iterations: ", num_iter
raw_input("\npress enter to exit")
