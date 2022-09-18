# create empty set
s = set()

# Add elements to set
s.add(1)
s.add(1)
s.add(2)
s.add(3)
s.add(4)
# only unique elements are added
print(s)    # {1, 2, 3, 4}

s.remove(2)
print(s)    # {1, 3, 4}

print(f"The set has {len(s)} elements.")    # The set has 3 elements.