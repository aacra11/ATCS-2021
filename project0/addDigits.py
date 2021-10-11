def addDigits(num):
    if(num<10):
        return num
    sum = 0
    while(num>0):
        sum = sum + num%10
        num = num // 10
    return addDigits(sum)

print(addDigits(6071))

