print('ho va ten:Nguyen Ba Linh')
print('MSSV:205752020710008')

def file_read (fname):
    from itertools import islice
    with open(fname, "w") as myfile:
        myfile.write("K61KTDIENTUVIENTHONG\n")
        myfile.write("DHV")
        txt = open (fname)
    print(txt.read())
file_read('D:/abc.txt')
