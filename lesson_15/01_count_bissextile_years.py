# Assignment
# Exercise 1. [Count of bissextile years] A year is bissextile if it is divisible by 4 and not by
# 100 unless it is divisible by 400. Develop a Python function:
# • countBissextile(year1, year2) that returns the number of bissextile years in the range [ year1, year2).

#################################################################

# Solution 1

def countBissextile(year1: int, year2: int):
    
    # List to store bissextile years
    bissextile = []

    # Iterate through the years in the given range
    for y in range(year1, year2):
        if y % 4 == 0 and y % 100 != 0: # if (y % 4 == 0 and y % 100 != 0) or y % 400 == 0: --> Compacted alternative
            bissextile.append(y)

        elif y % 400 == 0:
            bissextile.append(y)

    return len(bissextile)

# Testing
if __name__ == "__main__":
    print(countBissextile(2000, 2015))

#################################################################

# Solution 2

# Check if a year is bissextile (divisible by 4 and not by 100 unless divisible by 400)
def check_bisestile(year):
    return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0

# Function to count bissextile years in a given range
def countBissextile(year1: int, year2: int):
    # Initialize counter for bissextile years
    counter_bis = 0

    # Iterate through the years in the given range
    for y in range(year1, year2):
        if check_bisestile(y):
            counter_bis += 1

    return counter_bis

# Testing
y1 = int(input())
y2 = int(input())

countBissextile(y1, y2)

print(f"{countBissextile(y1, y2)}")

# Expected output:
# print(count_bissextile(2000, 2015))  # 4
# print(count_bissextile_with_helper(2000, 2015))  # 4