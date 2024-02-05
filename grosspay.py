# input number of hours and rate per hour
hours = float(input("Enter the number of hours worked: "))
rate = float(input("Enter the rate per hour: "))

# Calculate the gross pay
gross_pay = hours* rate
print(f"The gross pay is: {gross_pay:.2f}")

