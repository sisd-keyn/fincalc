def calc_end_balance(start_balance, annual_contribution, annual_growth, years):
    start_year = 2027
    end_year = start_year + years

    balance = start_balance

    for year_c in range(start_year, end_year):
        balance += annual_contribution
        balance = balance * (1 + (annual_growth/100))

    return balance

def calc_annual_contribution(start_balance, end_balance, annual_growth, years):
        r = annual_growth / 100.0
        if r == 0:
            return (end_balance - start_balance) / years

        growth_factor = (1 + r) ** years
        annuity_factor = (1 + r) * (growth_factor - 1) / r
        
        annual_contribution = (end_balance - start_balance * growth_factor) / annuity_factor

        return annual_contribution

def main2():
    starting_balance = float(input("Starting Balance: "))
    annual_contribution = float(input("Annual Contribution: "))
    annual_growth = float(input("Annual Growth: "))
    years = int(input("Years: "))

    end_balance = calc_end_balance(starting_balance, annual_contribution, annual_growth, years)

    print("End balance: ", f"{end_balance:,.2f}")

def main():
    start_balance = 0
    end_balance = 1000
    annual_growth = 7
    years = 10

    ac = calc_annual_contribution(start_balance, end_balance, annual_growth, years)

    print("Annual Contribution: ", f"{ac:,.2f}")

if __name__ == "__main__":
    main()
