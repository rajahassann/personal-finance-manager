Development Methodology: Iterative Enhancement

v0.1 basic-
	*input date --> input monthly income-> input fixed costs -> calculate amount left -> input variable costs --> calculate savings left*
	
	1)Initialization
		Input inital balance
		For each month:
			Input Fixed Costs:
				University (Total)
				Bills (Gas & Electricity)
				House Rent
			Calculate & display amount left
			Input Variable Costs Limit:
				Grocery Limit:
			Calculate & display monthly savings
	
	2) Tracking
		Input Grocery cost (append to previous)
		calculate amount and % of grocery budget availale
			if overbudget display overflow and give warning amt will be subtracted from savings
			subtract from savings
				if savings <= 0,display new overflow (extra grocery spending) after subtracting from savings, warn savings 0 and subtract from balance
				save grocery costs for the month
		Input misc costs (appending)(warn these are cut from savings):
			subtract from savings and calculate new savings.
			if savings 0 same mechanism as above
			save misc costs for the month