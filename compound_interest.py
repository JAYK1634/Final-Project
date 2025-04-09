# compound_interest.py

def compound_interest(principal, rate, time):
    amount = principal * (1 + rate / 100) ** time
    return amount - principal

p = float(input("Enter principal amount: "))
r = float(input("Enter annual interest rate: "))
t = float(input("Enter time in years: "))

ci = compound_interest(p, r, t)
print(f"Compound interest: {ci:.2f}")
