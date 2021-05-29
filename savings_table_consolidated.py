rows = int(input("How many years left to save? "))
columns = 28 # substitute for possible savings %
mylist = [[0 for x in range(columns)] for x in range(rows)]

return_rate = float(input("What is your expected return rate? "))
income = float(input("What is your yearly income? "))

existing_retirement = (int(input("How much do you have saved currently? ")))

r = rows
t = (return_rate)
q = 1 + t
p = 1

for i in range(rows):
    for j in range(1): # This loop fills the first column with the year numbers of savings.
        mylist[i][j] = r
        r = r - 1
    for j in range(1,2):  # This loop fills the second column with the return rate raised to the nth(year) power
        mylist[i][j] = round((q ** p), 3) # to correspond to compounded interest
        p = p + 1
    f = 7.0 # represents the starting range of 7% savings
    for j in range(2, columns): # This loop multiplies compounding constants by savings rates from f=7.0 % to ((columns - 2)/2) ie...14.5 %
        mylist[i][j] = round(mylist[i][1] * (income * (f/100))) # in increments of .5% and then resetting for the outer loop
        f = f + (.5)


totals = []

for j in range(3, columns):
    subtotal = 0
    for i in range(rows):
        subtotal = subtotal + mylist[i][j]
    totals.append(subtotal)
savings_percents = [i/2 for i in range(14, 30)]
# savings_percents = [i + .2 for i in range(7 ,columns)]

savings_amounts = []
for item in savings_percents:
    savings_amounts.append(round(item/100 * income))



print(savings_percents)

print(savings_amounts)
print(totals)
