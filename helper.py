import names
import random

char1 = random.choice(names.get_last_name()).upper()
char2 = random.choice(names.get_first_name()).upper()
char3 = random.choice(names.get_last_name()).upper()
char4 = random.choice(names.get_first_name()).upper()
name = char1 + char2 + char3 + char4
print(name)
