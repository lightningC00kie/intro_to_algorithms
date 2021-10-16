n = int(input())
b = True
while n > 1:
    if n % 3 ==0:
        n //= 3 
    else:
        b = False
        break

print(b)