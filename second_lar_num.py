a=[10,20,5,8]
first=second=-9999
for i in a:
    if i>first:
        second=first
        first=i
    elif i>second and i!=first:
        second=i
print(second)

