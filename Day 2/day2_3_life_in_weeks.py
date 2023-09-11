""" Create a program with math and f-string that tell us how many days,weeks,months left until we live 90 years old."""
#1year=365days
#1year=52weeks
#1year=12months

age = input("What is your current age?")
age_as_int = int(age)
year_remaining = 90 - age_as_int
days_remaining = year_remaining * 365
weeks_remaining = year_remaining * 52
months_remaining = year_remaining * 12
print(f"You have {days_remaining} days, {weeks_remaining} weeks and {months_remaining} months.")