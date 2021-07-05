import hashlib

def md5():
    aa=input("enter your string:\t")

    b=aa.encode()
    c=hashlib.md5(b)
    hexa=c.hexdigest()
    print(len(hexa))
    return
md5()