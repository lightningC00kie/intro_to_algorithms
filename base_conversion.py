import sys

base = []


n = []

for line in sys.stdin:
    if '>' in line:
        line = line.strip()
        start_base = int(line.split('>')[0])
        end_base = int(line.split('>')[1])
    else:
        temp = line.strip()
        l = []
        for c in temp:
            l.append(c)
        for i in range(len(l)):
            if ord(l[i]) >= 97 and start_base >= 10:
                l[i] = str(ord(l[i]) - 87)
    
            l[i] = int(l[i]) * (start_base**(len(l)-i-1))
        n.append([True, start_base, end_base])
        n.append(l)
        

for i in range(len(n)):
    sum = 0
    if n[i][0] == True:
        continue
   
    for ii in range(len(n[i])):
        
        sum += n[i][ii]
    n[i] = sum

for i in range(len(n)):

    converted = ''
    
    if isinstance(n[i], int):
        temp = n[i]

        if temp == 0:
            converted = '0'
        else:
            while temp >= 1:
                rem = temp % end_base
                if rem >= 10:
                    converted += chr(ord('A')+rem-10) 
                else:
                    converted += str(temp % end_base)
                temp //= end_base
        print(converted[::-1])
    else:
        start_base = n[i][1]
        end_base = n[i][2]

    