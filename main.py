import argparse

parser = argparse.ArgumentParser()
# 'nargs="?"' makes the argument optional
# 'type=int' converts the string input into an integer
# 'default=0' sets the default value if no argument is passed
parser.add_argument("starting_balance", type=int)
parser.add_argument("annual_contribution", type=int)
parser.add_argument("annual_growth", type=float)
parser.add_argument("years", type=int)

args = parser.parse_args()

starting_balance = args.starting_balance
annual_contribution = args.annual_contribution
annual_growth = args.annual_growth
years = args.years

balance = starting_balance
start_year = 2027
end_year = start_year + years

for year_c in range(start_year, end_year):
    print("Start of year ", year_c, " balance: ", f"{balance:,.2f}")
    balance += annual_contribution
    balance = balance * annual_growth

print("End balance: ", f"{balance:,.2f}")
