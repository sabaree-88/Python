def is_leap(year):
    leap = False
    
    # Write your logic here
    if year*4/4==0:
        leap=True
    if year*4/4==0 and year*4/100==0:
        leap=False
    elif year*4/4==0 and year*4/100==0 and year*4/400==0:
        leap=True 
    return leap

year = int(input())
print(is_leap(year))