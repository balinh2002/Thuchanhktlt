print("Sinh vien:Nguyen Ba Linh")
print("MSSV:205752020710008")
j=[]

for i in range (2000, 3201):

 if (i%7==0) and (i%5!=0):

  j.append(str(i))

print(','.join(j))
