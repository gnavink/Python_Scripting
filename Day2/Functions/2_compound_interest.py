# interest.py

principal = 1000        # Initial amount
rate = 0.05             # Interest rate
numyears = 5            # Number of years


def calculate_compund_interest(principal, rate, numyears):
    year = 0
    while year < numyears:
        principal = principal * (1 + rate)
        print(year, principal)
        year += 1
    return principal

compunded_principal = calculate_compund_interest(principal,rate,numyears)
print(f'compunded_principal: {compunded_principal}')
	    
