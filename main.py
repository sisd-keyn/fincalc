def calc_start_balance(end_balance, annual_contribution, annual_growth, years):
    r = annual_growth / 100.0
    if r == 0:
        return end_balance - annual_contribution * years

    growth_factor = (1 + r) ** years
    annuity_factor = (1 + r) * (growth_factor - 1) / r

    start_balance = (end_balance - annual_contribution * annuity_factor) / growth_factor

    return start_balance

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

def calc_years(start_balance, end_balance, annual_contribution, annual_growth):
    r = annual_growth / 100.0
    if r == 0:
        return (end_balance - start_balance) / annual_contribution

    years = 0
    balance = start_balance

    while balance < end_balance:
        balance += annual_contribution
        balance = balance * (1 + r)
        years += 1

    return years

def calc_annual_growth(start_balance, end_balance, annual_contribution, years):
    if years <= 0:
        return 0.0

    # Binary search to solve for interest rate r numerically
    low = -0.999
    high = 10.0
    max_iterations = 100
    tolerance=1e-7

    for _ in range(max_iterations):
        mid = (low + high) / 2.0
        
        if abs(mid) < 1e-9:
            predicted_eb = start_balance + annual_contribution * years
        else:
            gf = (1 + mid) ** years
            af = (1 + mid) * (gf - 1) / mid
            predicted_eb = start_balance * gf + annual_contribution * af

        if abs(predicted_eb - end_balance) < tolerance:
            return mid * 100.0

        if predicted_eb < end_balance:
            low = mid
        else:
            high = mid

    return ((low + high) / 2.0) * 100.0

def calc_years_from_age(current_year, birth_year, target_age):
    years_until_target_age = target_age - (current_year - birth_year)
    return years_until_target_age

def main():
    start_balance = 50000
    annual_contribution = 32000
    end_balance = 100000/0.04
    annual_growth = 7

    retirement_age = 52
    years = calc_years_from_age(2026, 1995, retirement_age)

    x = calc_annual_contribution(start_balance, end_balance, annual_growth, years)

    print("Annual Contribution: ", f"{x:,.2f}")

if __name__ == "__main__":
    main()
