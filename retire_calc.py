import sys

age = float(input("What is your age? "))

current_savings = float(input("How much do you have saved currently? "))

print(current_savings)

time_to_save = float(input("At what age do you plan to retire? ")) - age

amount_needed = float(input("How much monthy income would you need tomorrow to continue your ideal quality of life? "))

inflation = .0275

return_rate = float(input("What return rate do you expect from your investments? "))

yearly_total_needed = round((12 * amount_needed) * ((1 + inflation) ** time_to_save), 2)

total_savings_needed = round((yearly_total_needed / (return_rate)), 2)

compounding_ratio = (1 + (return_rate)) ** time_to_save

current_savings_compounded = round((current_savings * compounding_ratio), 2)


need_to_save = round((total_savings_needed - current_savings_compounded), 2)

# def yearly_savings_rate(need_to_save, return_rate, time_to_save):
#     return need_to_save * (return_rate) / (((1+return_rate) ** (time_to_save)) - 1)

def yearly_savings_rate(F, i, n):
    return F * (i) / (((1+i) ** (n)) - 1)

savings_rate = yearly_savings_rate(need_to_save, return_rate / 12 , time_to_save * 12)
monthly_savings_rate = round(savings_rate)


print("Required yearly income:")
print(yearly_total_needed)

print("Your total savings goal:")
print(total_savings_needed)

print("Your current savings would compound to:")
print(current_savings_compounded)

print("You need to save an additional:")
print(need_to_save)

print("You can reach that goal by saving at least $", monthly_savings_rate , "per month")

print("This line is a test to make sure that github catches my work")
