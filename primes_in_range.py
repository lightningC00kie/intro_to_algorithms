import time

def main():
    A = int(input())
    B = int(input())
    start_time = time.time()

    smallest = B
    largest = counter = percentage = 0

    for i in range(A, B+1):
        n = 2
        is_prime = True
        while n * n <= i:
            if i % n == 0:
                is_prime = False
                break
            n += 1
        
        if is_prime:
            counter += 1

            if i < smallest:
                smallest = i
            
            if i > largest:
                largest = i

    if counter == 0:
        smallest = largest = None
    else:
        percentage = (counter/((B-A)+1)) * 100
        

    print('Number of primes: ', counter)
    print('Smallest prime: ', smallest)
    print('Largest prime: ', largest)
    print('Percentage of numbers that are prime: ', f'{percentage:.1f}')

    print("--- %s seconds ---" % (time.time() - start_time))


if __name__ == '__main__':
    main()