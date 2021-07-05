import hashlib

def md5():
    aa=input("enter your string:\t")
    for i in range(5):
        b=aa.encode()
        c=hashlib.md5(b)
        hexa=c.hexdigest()

        print(hexa)
        return
md5()