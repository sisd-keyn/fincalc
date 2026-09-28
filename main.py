balance = 0
annualContribution = 8000
annualGrowth = 1.07
start_year = 2027
end_year = start_year + 49

for year_c in range(start_year, end_year):
    print("Start of year ", year_c, " balance: ", f"{balance:,.2f}")
    balance += annualContribution
    balance = balance * annualGrowth

