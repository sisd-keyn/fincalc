starting_balance = float(input("Starting Balance: "))
annual_contribution = float(input("Annual Contribution: "))
annual_growth = float(input("Annual Growth: "))
years = int(input("Years: "))

balance = starting_balance
start_year = 2027
end_year = start_year + years

for year_c in range(start_year, end_year):
    print("Start of year ", year_c, " balance: ", f"{balance:,.2f}")
    balance += annual_contribution
    balance = balance * annual_growth

print("End balance: ", f"{balance:,.2f}")
