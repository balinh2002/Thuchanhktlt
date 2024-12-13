print('ho va ten:Nguyen Ba Linh')
print('MSSV:205752020710008')

class Nguoi(object):
 def getGender(self):
  return "Unknoun"

class Nam(Nguoi):
 def getGender(self):
     return "Nam"
class Nu(Nguoi):
 def getGender(self):
     return "Nu"

aNam = Nam()
aNu = Nu()
print (aNam.getGender())
print (aNu.getGender())
