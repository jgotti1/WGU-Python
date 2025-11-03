# 11.14 LAB: Radioactive decay
# lab activity
# 11.14.1: LAB: Radioactive decay

# Full screen
# 0 / 10
# Complete the functions in the template to implement the formulas shown below.

# The formula to calculate how much of a radioactive isotope with half-life T will remain after time t is:


# The formula can be rearranged to calculate the half-life of an isotopegiven how much remains after decay:


# The notation used in the formulas is:

# e = Euler's number
# t = the length of time (in years) during which an isotope decays
# T = the half-life (in years) of the isotope
# N0 = the initial amount of the isotope
# Nt the amount of the isotope remaining after time t
# Then, complete the main program to:

# Read a choice
# Read 3 numbers from one line:
# Choice N: N0, t, and T
# Choice T: N0, Nt, and t
# Call compute_Nt() if the choice is N, compute_T if the choice is T
# Output the result with four digits after the decimal point.
# Note: Use math.exp() to calculate the exponential value with the base set to e.

# Ex: If the input is:

# N
# 100 50 28.94
# the output is:

# Nt = 30.1930
# Ex: If the input is:

# T
# 100 30.1930 50
# the output is:

# T = 28.9400

import math

# An isotope has half-life T.
# Return the amount of a starting mass N0
# of the isotope that remains after time t
def compute_Nt(N0, t, T):
    return N0 * math.exp((-t * math.log(2)) / T)


# Return the half-life of an isotope given that
# a mass N0 decays to Nt after time t
def compute_T(N0, Nt, t):
    return (t * math.log(2)) / (math.log(N0) - math.log(Nt))


if __name__ == '__main__':
    choice = input()   # 'N' or 'T'

    if choice == 'N':                     # Calculate amount of material
        N0, t, T = map(float, input().split())
        Nt = compute_Nt(N0, t, T)
        print(f'Nt = {Nt:.4f}')

    elif choice == 'T':                   # Calculate half-life
        N0, Nt, t = map(float, input().split())
        T = compute_T(N0, Nt, t)
        print(f'T = {T:.4f}')

    else:
        print("invalid choice")

