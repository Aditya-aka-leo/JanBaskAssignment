
def CountSubArray( st , pat ) :

    NumOcc = st.count( pat )

    return NumOcc

str = input("Please Enter The String : ")

pattern = input("Please Enter The Pattern : ")

ans = CountSubArray( str , pattern )

print(f"The Number Of Times Pattern '{pattern}' was found is : {ans} ")

