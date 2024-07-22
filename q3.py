def StringMethod( num ):

    NumString = str(num)

    RevString = NumString[::-1]    

    return RevString == NumString

def NumMethod( num ):

    RevNum = 0
    temp = num

    while(temp != 0) :
        RevNum = (RevNum * 10) + (temp % 10)

        temp = temp // 10

    return RevNum == num 

num = int(input('Please Enter The Number You Want To Check For Palindrome : '))

print(StringMethod( num ))

print(NumMethod( num ))







