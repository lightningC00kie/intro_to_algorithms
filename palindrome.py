s = [c for c in input() if c.isalpha()]
print('True') if s == s[::-1] else print('False')