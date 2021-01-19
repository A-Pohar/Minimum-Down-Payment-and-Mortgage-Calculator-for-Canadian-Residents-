from decimal import Decimal

if __name__ == "__main__":
    print("Welcome to the minimum down payment and mortgage calculator for "
          "Canadian properties!")
    print("This calculator currently works for Canadian residents.")

    type_of_property = input("Will this property be a principal residence or "
                             "investment property (Principal/Investment)?: ").lower()
    home_value = int(input("What is the assessed value of the property you wish to purchase "
                           "(please enter an integer)?: "))

    if type_of_property == "investment":
        min_dp = int(0.2 * home_value)
        print("The minimum down payment needed would be 20% * {0} = {1}.".format(
            home_value, min_dp))
        inputted_dp_percent = float(input("What % down payment would you like to pay "
                                          "(must be at least 20%)?: "))
        while inputted_dp_percent < 20:
            inputted_dp_percent = float(input("Sorry, but that percentage is less than 20%. "
                                              "What % down payment would you like to pay "
                                              "(must be at least 20%)?: "))
        real_dp_percent = 0.01 * inputted_dp_percent
        real_dp = int(real_dp_percent * home_value)
        mortgage_amount = int((1 - real_dp_percent) * home_value)
        print("The down payment you will make will be ${0}, so ${1} "
              "will be borrowed as a mortgage.".format(real_dp, mortgage_amount))
        annual_interest_rate = 0.01 * float(input("What will the interest rate be "
                                                  "for your mortgage?: "))
        amortization_period = int(input("What will the amortization period be "
                                        "for your mortgage (must be an integer from 1 to 30)?: "))
        num_payments = amortization_period * 12
        monthly_interest_rate = annual_interest_rate / 12
        numerator = mortgage_amount * (monthly_interest_rate *
                                       pow(1 + monthly_interest_rate, num_payments))
        denominator = pow(1 + monthly_interest_rate, num_payments) - 1
        print(numerator)
        print(denominator)
        monthly_mortgage_payment = round(numerator / denominator, 2)
        print("---------------------------------------------------------------------------------------------")
        print("In summary, you will make a down payment of: ${0},\n"
              "take out at mortgage of ${1} with an interest rate of {2}% over an "
              "amortization period of {3} years.\n"
              "Your monthly mortgage payment will be "
              "${4}".format(real_dp, mortgage_amount, 100 * annual_interest_rate,
                            amortization_period, monthly_mortgage_payment))

    elif type_of_property == "principal":
        if home_value > 0 and home_value <= 500000:
            min_dp = Decimal("0.05") * home_value
            print("The minimum down payment needed would be 5% * {0} = {1}.".format(
                home_value, min_dp))
            inputted_dp_percent = Decimal(input("What % down payment would you like to pay "
                                                "(must be at least 5%)?: "))
            while inputted_dp_percent < 5:
                inputted_dp_percent = Decimal(input("Sorry, but that percentage is less than 5%. "
                                                    "What % down payment would you like to pay "
                                                    "(must be at least 5%)?: "))
            real_dp_percent = Decimal("0.01") * inputted_dp_percent
            real_dp = int(real_dp_percent * home_value)
            mortgage_amount = int((1 - real_dp_percent) * home_value)
            mortgage_default_insurance = 0
            if 5 <= inputted_dp_percent < 10:
                mortgage_default_insurance = Decimal("0.04") * Decimal(str(mortgage_amount))
                print("With a down paymwnt of {0}%, you will also have to pay 4% * ${1} = {2} in mortgage default "
                      "insurance. This amount will be added to your mortgage.".format(
                    inputted_dp_percent, mortgage_amount, mortgage_default_insurance))
            elif 10 <= inputted_dp_percent < 15:
                mortgage_default_insurance = Decimal("0.031") * Decimal(str(mortgage_amount))
                print("With a down paymwnt of {0}%, you will also have to pay 3.10% * ${1} = {2} in mortgage default "
                      "insurance. This amount will be added to your mortgage.".format(
                    inputted_dp_percent, mortgage_amount, mortgage_default_insurance))
            elif 15 <= inputted_dp_percent < 20:
                mortgage_default_insurance = Decimal("0.028") * Decimal(str(mortgage_amount))
                print("With a down paymwnt of {0}%, you will also have to pay 2.8% * ${1} = {2} in mortgage default "
                      "insurance. This amount will be added to your mortgage.".format(
                    inputted_dp_percent, mortgage_amount, mortgage_default_insurance))
            print("The down payment you will make will be ${0}, so ${1} will be borrowed as a mortgage. "
                  "Adding mortgage default insurance premium of ${2} will make the mortgage total = ${3}".format(
                real_dp, mortgage_amount, mortgage_default_insurance, mortgage_amount + mortgage_default_insurance))
            mortgage_amount += mortgage_default_insurance
            annual_interest_rate = Decimal("0.01") * Decimal(input("What will the interest rate be "
                                                                   "for your mortgage?: "))
            amortization_period = int(input("What will the amortization period be "
                                            "for your mortgage (must be an integer from 1 to 30)?: "))
            num_payments = amortization_period * 12
            monthly_interest_rate = annual_interest_rate / 12
            numerator = mortgage_amount * (monthly_interest_rate *
                                           pow(1 + monthly_interest_rate, num_payments))
            denominator = pow(1 + monthly_interest_rate, num_payments) - 1
            monthly_mortgage_payment = round(numerator / denominator, 2)
            print("---------------------------------------------------------------------------------------------")
            print("In summary, you will make a down payment of: ${0},\n"
                  "take out at mortgage of ${1} with an interest rate of {2}% over an "
                  "amortization period of {3} years.\n"
                  "Your monthly mortgage payment will be "
                  "${4}".format(real_dp, mortgage_amount, 100 * annual_interest_rate,
                                amortization_period, monthly_mortgage_payment))

        elif 500000 < home_value and home_value < 1000000:
            upper_difference = home_value - 500000
            min_dp = Decimal("0.05") * 500000 + Decimal("0.10") * upper_difference
            print("The minimum down payment needed would be 5% * $500000 + 10% * {0} "
                  "= {1}.".format(upper_difference, min_dp))
            min_dp_percent = round((Decimal(str(min_dp)) / Decimal(str(home_value))) * 100, 2)
            inputted_dp_percent = Decimal(input("What % down payment would you like to pay "
                                                "(must be at least {0}%)?: ".format(min_dp_percent)))
            while inputted_dp_percent < min_dp_percent:
                inputted_dp_percent = Decimal(input("Sorry, but that percentage is less than {0}%. "
                                                    "What % down payment would you like to pay "
                                                    "(must be at least {1}%)?: ".format(min_dp_percent, min_dp_percent)))
            real_dp_percent = Decimal("0.01") * inputted_dp_percent
            real_dp = int(real_dp_percent * home_value)
            mortgage_amount = int((1 - real_dp_percent) * home_value)
            mortgage_default_insurance = 0
            if 5 <= inputted_dp_percent < 10:
                mortgage_default_insurance = Decimal("0.04") * Decimal(str(mortgage_amount))
                print("With a down paymwnt of {0}%, you will also have to pay 4% * ${1} = {2} in mortgage default "
                      "insurance. This amount will be added to your mortgage.".format(
                    inputted_dp_percent, mortgage_amount, mortgage_default_insurance))
            elif 10 <= inputted_dp_percent < 15:
                mortgage_default_insurance = Decimal("0.031") * Decimal(str(mortgage_amount))
                print("With a down paymwnt of {0}%, you will also have to pay 3.10% * ${1} = {2} in mortgage default "
                      "insurance. This amount will be added to your mortgage.".format(
                    inputted_dp_percent, mortgage_amount, mortgage_default_insurance))
            elif 15 <= inputted_dp_percent < 20:
                mortgage_default_insurance = Decimal("0.028") * Decimal(str(mortgage_amount))
                print("With a down paymwnt of {0}%, you will also have to pay 2.8% * ${1} = {2} in mortgage default "
                      "insurance. This amount will be added to your mortgage.".format(
                    inputted_dp_percent, mortgage_amount, mortgage_default_insurance))
            print("The down payment you will make will be ${0}, so ${1} will be borrowed as a mortgage. "
                  "Adding mortgage default insurance premium of ${2} will make the mortgage total = ${3}".format(
                real_dp, mortgage_amount, mortgage_default_insurance, mortgage_amount + mortgage_default_insurance))
            mortgage_amount += mortgage_default_insurance
            annual_interest_rate = Decimal("0.01") * Decimal(input("What will the interest rate be "
                                                                   "for your mortgage?: "))
            amortization_period = int(input("What will the amortization period be "
                                            "for your mortgage (must be an integer from 1 to 30)?: "))
            num_payments = amortization_period * 12
            monthly_interest_rate = annual_interest_rate / 12
            numerator = mortgage_amount * (monthly_interest_rate *
                                           pow(1 + monthly_interest_rate, num_payments))
            denominator = pow(1 + monthly_interest_rate, num_payments) - 1
            monthly_mortgage_payment = round(numerator / denominator, 2)
            print("---------------------------------------------------------------------------------------------")
            print("In summary, you will make a down payment of: ${0},\n"
                  "take out at mortgage of ${1} with an interest rate of {2}% over an "
                  "amortization period of {3} years.\n"
                  "Your monthly mortgage payment will be "
                  "${4}".format(real_dp, mortgage_amount, 100 * annual_interest_rate,
                                amortization_period, monthly_mortgage_payment))

        elif home_value >= 1000000:
            min_dp = Decimal("0.20") * home_value
            print("The minimum down payment needed would be 20% * {0} = {1}.".format(
                home_value, min_dp))
            inputted_dp_percent = Decimal(input("What % down payment would you like to pay "
                                                "(must be at least 20%)?: "))
            while inputted_dp_percent < 20:
                inputted_dp_percent = Decimal(input("Sorry, but that percentage is less than 20%. "
                                                    "What % down payment would you like to pay "
                                                    "(must be at least 20%)?: "))
            real_dp_percent = Decimal("0.01") * inputted_dp_percent
            real_dp = int(real_dp_percent * home_value)
            mortgage_amount = int((1 - real_dp_percent) * home_value)
            print("The down payment you will make will be ${0}, so ${1} "
                  "will be borrowed as a mortgage with no mortgage default insurance premium.".format(
                real_dp, mortgage_amount))
            annual_interest_rate = Decimal("0.01") * Decimal(input("What will the interest rate be "
                                                      "for your mortgage?: "))
            amortization_period = int(input("What will the amortization period be "
                                            "for your mortgage (must be an integer from 1 to 30)?: "))
            num_payments = amortization_period * 12
            monthly_interest_rate = annual_interest_rate / 12
            numerator = mortgage_amount * (monthly_interest_rate *
                                           pow(1 + monthly_interest_rate, num_payments))
            denominator = pow(1 + monthly_interest_rate, num_payments) - 1
            monthly_mortgage_payment = round(numerator / denominator, 2)
            print("---------------------------------------------------------------------------------------------")
            print("In summary, you will make a down payment of: ${0},\n"
                  "take out at mortgage of ${1} with an interest rate of {2}% over an "
                  "amortization period of {3} years.\n"
                  "Your monthly mortgage payment will be "
                  "${4}".format(real_dp, mortgage_amount, 100 * annual_interest_rate,
                                amortization_period, monthly_mortgage_payment))