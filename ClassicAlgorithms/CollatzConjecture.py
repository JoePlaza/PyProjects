# Collatz Conjecture

def collatz(num):
    goes=0
    while num > 1:
        if num%2==0:
            goes += 1
            num = num/2

        elif num%2 != 0:
            goes +=1
            num = (num*3)+1

    print("It took %s goes" %goes)


collatz(num)
