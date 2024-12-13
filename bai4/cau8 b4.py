print("Sinh vien:Nguyen Ba Linh")
print("MSSV:205752020710008")
def dai_nhat (s):
    dainhat = ''
    for i in s:
        if len(i) >= len(dainhat):
            dainhat = i
    return dainhat
s = input('nhap chuoi: ').split()
print(dai_nhat(s))
