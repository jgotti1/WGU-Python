import os

path = os.path.join('logs', '2009')  # This is a single string path like "logs/2009"

# Convert the walk generator into a list of results
all_data = list(os.walk(path))

print(all_data)
