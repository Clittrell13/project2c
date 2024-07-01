cents = int(input("Please enter an amount in cents less than a dollar: "))

quarters = cents // 25
cents %= 25

dimes = cents // 10
cents %= 10

nickels = cents // 5
cents %= 5

pennies = cents

print(f"Your change will be Q: {quarters},"
      f" D: {dimes}, "
      f"N: {nickels}, "
      f"P: {pennies}")
