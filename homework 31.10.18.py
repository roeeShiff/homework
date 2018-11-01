usernum = int(input("please enter a number: "))
arr=['zero','one','two','three','four','five','six','seven','eight','nine']

if usernum>=0 and usernum<10:
    print("your number is:",arr[usernum])

elif usernum > 9 and usernum < 100:
    a=(int(usernum/10)) + (usernum%10)
    print("your entered a two digits number")
    print("the sum of the digits is: ",a )

elif usernum > 99 and usernum <1000:
    a=(int(usernum%10))
    b=(int(usernum/10))
    c=(int(b%10))
    d=(int(b/10))
    print("your number has three digits")
    print("the multiply of the digits is:",a*c*d)

else:
    print("your number is not in range")