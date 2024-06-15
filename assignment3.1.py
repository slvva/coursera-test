hrs=input(Enter number of hours: ')
h=float(hours)

rate=input('Enter rate per hour: ')
r=float(rate)

if h<=40:
    print(h*r)
else:
    print(40*r+(h-40)*r*1.5)
