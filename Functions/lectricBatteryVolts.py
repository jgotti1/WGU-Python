# compute my battery voltage percent on my lectrix xp4 with a 54 volt battery

def percentage_calc(volts_current, vmin, vmax):
  return ((volts_current - vmin) / (vmax - vmin)) * 100

volts_max = 54.6
volts_min = 39

print()
voltage_current = float(input("What voltage is your battery currently at?: "))
print()
print(f'You have {percentage_calc(voltage_current, volts_min, volts_max):.2f}% battery left\n')