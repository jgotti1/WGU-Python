# Many documents use a specific format for a person's name. Write a program that reads a person's name in the following format:

# firstName middleName lastName (in one line)

# and outputs the person's name in the following format:

# lastName, firstInitial.middleInitial.

# If the input has the following format:

# firstName lastName (in one line)

# the output is:

# lastName, firstInitial.

# Ex: If the input is:

# Ex: If the input is:

name = input()

def name_out(name):
    parts = name.split()
    
    if len(parts) == 3:
        first, middle, last = parts
        p1 = first[0]
        p2 = middle[0]
        p3 = last
        return (f"{p3}, {p1}.{p2}")
    elif len(parts) == 2:
        first, last = parts
        p1 = first[0]
        p2 = last
        return (f"{p2}, {p1}")
    else:
        return "Not Valid Input"
      
                



print(name_out(name))
