def StringMethod( num ):

    NumString = str(num)

    RevString = NumString[::-1]                     # reversing the string to check for pallindrome

    return RevString == NumString

def NumMethod( num ):

    RevNum = 0
    temp = num

    while(temp != 0) :
        RevNum = (RevNum * 10) + (temp % 10)        # create a reversed number from original number by extracting from last place

        temp = temp // 10                           # moving the to the next digit from back

    return RevNum == num 

num = int(input('Please Enter The Number You Want To Check For Palindrome : '))

print(StringMethod( num ))

print(NumMethod( num ))







