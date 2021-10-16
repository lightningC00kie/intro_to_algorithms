n = temp = int(input())
factors = ''
i=2
prod = 1
repeat = True
counter = 0
counter2 = 0
while prod != n:
# checking if i is a prime number in each iteration of the outer while loop
    if repeat:
        counter2 += 1
        prime = True
        j = 2           
        
        while j * j <= i:
            if i % j == 0:
                prime = False
                break
            j += 1

###########################################

# if temp is divisible by i and i is prime then we continue to divide the new value of temp by i and add the number of times
# we divide by i to a counter variable until eventually temp will not be divisible by i
    if temp % i == 0 and prime==True:
        repeat = False
        counter += 1
        temp = temp // i
        continue
# if temp is not divisible by i (we figure out which condition is false because we check if counter != 0 in which case i was in fact prime)
# then we add i to the power of counter to the string factors and then reset the variable for the next iteration
# we also get a new value for prod which will be checked before the while loop executes again. If prod is equal to n then we have found all the prime factors
# and we can exit the loop
    else:
        if counter != 0:
            if counter == 1:
                factors += f'{i} * '
            else:
                factors += f'{i}^{counter} * '
            prod *= i**counter
            counter = 0
            i = 1
        i += 1
        repeat = True
        prime = False


print(factors[:-3], counter2)