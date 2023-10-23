'''
NAME:KELVIN NZIOKA
REG_NO: PA106/G/9983/20
'''



def calc_tax(gross_pay):
    if gross_pay >= 50000:
        tax_rate = 0.35
    elif 40000 <= gross_pay  and gross_pay< 50000:
        tax_rate = 0.30
    elif 20000 <= gross_pay < 40000:
        tax_rate = 0.25
    elif 12000 <= gross_pay < 20000:
        tax_rate = 0.15
    else:
        tax_rate = 0

    tax_amount = gross_pay * tax_rate
    return tax_amount

# Input gross pay
gross_pay = float(input("Enter the gross pay: "))

# Calculate tax using the calc_tax function
tax = calc_tax(gross_pay)

# Calculate net pay
net_pay = gross_pay - tax

# Display tax amount and net pay
print(f"Tax Amount: {tax:.2f}")
print(f"Net Pay: {net_pay:.2f}")
