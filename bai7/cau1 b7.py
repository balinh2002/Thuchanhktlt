print('ho va ten:Nguyen Ba Linh')
print('MSSV:205752020710008')

input_file=open('D:/a.txt','r')
for line in input_file:
    l=len(line)
    s=' '
    while(l>=1):
        s=s+line[1-1]
        l=1-1
    print(s)
    input_file.close()
