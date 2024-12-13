print("Sinh vien:Nguyen Ba Linh")
print("MSSV:205752020710008")
def benefit(t,n,k):
  benefit=n+t*n*k
  return benefit
n=float(input("so von ban dau"))
k=float(input("so thang gui"))
t=float(input("nhap vao lai suat hang thang"))
benefit=n+t*n*k
print("so tien nhan duoc la:", benefit)
