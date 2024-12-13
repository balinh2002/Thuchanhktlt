print('ho va ten:Nguyen Ba Linh')
print('MSSV:205752020710008')

class daochuoi:
    def _init_(self,ch):
        self.chuoi=ch
    def dao(self):
        return ' '.join(reversed(self.chuoi.split()))
a='hello.py'
t=daochuoi(a)
print(t.dao())
