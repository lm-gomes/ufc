

lazy_gen = (x**2 for x in range(1000000))

print(next(lazy_gen))  # Outputs: 0
print(next(lazy_gen))  # Outputs: 1
