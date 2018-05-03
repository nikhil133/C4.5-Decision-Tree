import numpy as np
import pandas as pd
import sys
from sklearn.model_selection import train_test_split

def predict(loan_amount,repaid_amount,days,number_of_loans,lenoffunc,i):
		
	
	if lenoffunc==i:
		return 0
	else:	
		if days.item(i)<=31.5:
		#print("days:{}<=31.5 -> Active".format(days))
			print("Active")
		elif days.item(i)>31.5:
			if loan_amount.item(i)<=1617.5:
				if number_of_loans.item(i)<=3.5:
					if repaid_amount.item(i)<=2179.5:
						#print("days :{} > 31.5 --> loan ammount :{} <=1617.5 --> number of loans{} <= 3.5 --> repaid amount{} <= 2179.5 -> Default".format(days,loan_amount,number_of_loans,repaid_amount))
						print("Default")				
					elif repaid_amount.item(i)>2179.5:
						#print("days :{} > 31.5 --> loan_amount :{} <=1617.5 --> number of loans{} <= 3.5 --> repaid amount {} > 2179.5 -> Write Off".format(days,loan_amount,number_of_loans,repaid_amount))
						print("Write Off")
				if number_of_loans.item(i)>3.5:
					if repaid_amount.item(i)<=992.5 or repaid_amount.item(i)>992.5:
						#print("days :{} > 31.5 --> loan amount:{} <=1617.5 -->number of loans :{} <= 3.5 -->repaid amount {} greater or less than or equal to 992.5 -> Default".format(days,loan_amount,number_of_loans,repaid_amount))
						print("Default")
			if loan_amount.item(i)>1617.5:
				if number_of_loans.item(i)<=6.5:
					if repaid_amount.item(i)<=1878.0 or repaid_amount.item(i)>1878.0:
						#print("days :{} > 31.5 --> loan amount :{} >1617.5--> number of loans :{} <= 6.5 --> repaid amount{} greater than or less than or equal to 1878 --> Write Off".format(days,loan_amount,number_of_loans,repaid_amount))
						print("Write Off")
				if number_of_loans.item(i)>6.5:
					if repaid_amount.item(i)<= 5317.0:
						#print("days :{} > 31.5 --> loan amount :{} >1617.5-->number of loans :{} > 6.5 --> repaid amount:{} <= 53170 --> Write Off".format(days,loan_amount,number_of_loans,repaid_amount))
						print("Write Off")
					elif repaid_amount.item(i)> 5317.0:
						#print("days :{} > 31.5 --> loan amount :{} >1617.5-->number of loans :{} > 6.5 --> repaid amount :{} > 53170 --> Default".format(days,loan_amount,number_of_loans,repaid_amount))
						print("Default")
		predict(loan_amount,repaid_amount,days,number_of_loans,lenoffunc,i=i+1)				
def main():
	dataset=pd.read_csv('pgwebwln.csv',nrows=13395)

	loan_amount=np.float64(dataset.iloc[:,:1].values)
	repaid_amount=np.float64(dataset.iloc[:,:2].values)
	days=np.float64(dataset.iloc[:,:3].values)
	number_of_loans=np.float64(dataset.iloc[:,:4].values)
       
	lmtrain,lmtest=train_test_split(loan_amount, test_size=0.2, random_state=0)
	ratrain,ratest=train_test_split(repaid_amount, test_size=0.2, random_state=0)
	dytrain,dytest=train_test_split(days, test_size=0.2, random_state=0)
	nofltrain,nofltest=train_test_split(number_of_loans, test_size=0.2, random_state=0)
	'''
	arg=sys.argv
	loan_amount=float(arg[1])
	repaid_amount=float(arg[2])
	days=float(arg[3])
	number_of_loans=float(arg[4])
	
	if len(arg)!=5:
		print("Argument Error:Invalid number of argument")
		sys.exit(1)
	'''
		
	predict(lmtest,ratest,dytest,nofltest,len(lmtest),0)
if __name__=="__main__":main()		

