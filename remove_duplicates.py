a=[1,2,2,3,4,3]
unique=[]
for i in a:
    if i not in unique:
        unique.append(i)
print(unique)
