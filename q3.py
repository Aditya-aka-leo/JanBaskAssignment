def StringMethod( num ):

    numString = str(num)

    revString = numString[::-1]                     # reversing the string to check for pallindrome

    return revString == numString

def NumMethod( num ):

    revNum = 0

    temp = num

    while(temp != 0) :
        revNum = (revNum * 10) + (temp % 10)        # create a reversed number from original number by extracting from last place

        temp = temp // 10                           # moving the to the next digit from back

    return revNum == num 

num = int(input('Please Enter The Number You Want To Check For Palindrome : '))

print(StringMethod( num ))

print(NumMethod( num ))







