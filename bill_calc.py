tip_percentage= 18
bill_amount= 10
def calculate_bill():
	return (tip_percentage*.01* bill_amount)+bill_amount


def calc_alone_bill():
	return bill_amount

def tip_ave():
	return (.18*bill_amount) + bill_amount

def main():
	global bill_amount
	bill_amount= float(raw_input("How much was your bill, not including tip?"))

	dine_alone=raw_input("Did you dine alone, Y/N?")
	if (dine_alone.upper()=="N"):
		dine= int(raw_input("How many people were at dinner?"))
		tip_percentage= raw_input("Is 18 percent tip okay, Y/N?")
		if (tip_percentage.upper()=="N"):
			tip= float(raw_input("How much do you want to leave for tip?"))
			print "Your total is", ((tip*.01*bill_amount)+bill_amount)/dine
		else:
			print "Your total is", tip_ave()/dine
	else: 
		global tip_percentage
		tip_percentage= float(raw_input("How much do you want to leave for tip?"))
		alone_bill= calculate_bill()
		print "Your total is", alone_bill
	# tip_percentage= raw_input("Is 18 percent tip okay, Y/N?")
	# if (tip_percentage.upper()=="N"):
	# 	tip= int(raw_input("How much do you want to leave for tip?"))
	# else:
	# 	return tip_ave
if __name__ == "__main__":
	main()