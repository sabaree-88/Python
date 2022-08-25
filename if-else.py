n = int(input().strip())
if n%2!=0:
    print("Weird")
elif n%2==0:
    if range(n,6):
        print("Not Weird")
    elif range(n,21):
        print("Weird")
    else:
        if range(n,101) :
            print("Not Weird")

else:
    if n%2==0 and n>20:
        print("Not Weird")