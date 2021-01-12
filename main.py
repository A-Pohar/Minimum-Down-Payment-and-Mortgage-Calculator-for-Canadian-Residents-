if __name__ == "__main__":
    print("Welcome to the minimum down payment and mortgage calculator for Canadian properties!")
    print("This calculator currently works for Canadian residents.")

    type_of_property = input("Will this property be a principal residence or investment property "
                             "(Principal/Investment)?: ").lower()
    home_value = int(input("What is the assessed value of the property you wish to purchase "
                           "(please enter an integer)?: "))

    if type_of_property == "investment":
        min_dp = int(0.2 * home_value)
        print("The minimum down payment needed would be 20% * {0} = {1}.".format(home_value, min_dp))
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
        annual_interest_rate = 0.01 * float(input("What will the interest rate be for your mortgage?: "))
        amortization_period = int(input("What will the amortization period be for your mortgage "
                                        "(must be an integer from 1 to 30)?: "))
        num_payments = amortization_period * 12
        monthly_interest_rate = annual_interest_rate / 12
        numerator = mortgage_amount * (monthly_interest_rate *
                                             pow(1+monthly_interest_rate, num_payments))
        denominator = pow(1+monthly_interest_rate, num_payments) - 1
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
