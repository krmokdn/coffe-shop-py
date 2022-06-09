latte=3
mocha=4
icm=10

print("kahvelerimiz= latte,mocha ve icm olarak 3 çeşittir")

ksecim=str(input("hangi kahveyi tercih edersiniz?="))

if  ksecim== "latte":
    bsecim=input("tall,grande,vetti? Hangi boy olsun?=")
    if bsecim=="tall":
        print("hasap tutarınız:",latte*1.25)
    elif bsecim=="grande":
        print("hesap tutarınız:",latte*1.50)
    elif bsecim=="vetti":
        print("hesap tutarınız:",latte*2)
    else:
        print("geccersiz secim")
    
elif (ksecim=="mocha"):
    bsecim=input("tall,grande,vetti? Hangi boy olsun?=")
    if bsecim=="tall":
        print("hasap tutarınız:",mocha*1.25)
    elif bsecim=="grande":
        print("hesap tutarınız:",mocha*1.50)
    elif bsecim=="vetti":
        print("hesap tutarınız:",mocha*2)
    else:
        print("geccersiz secim")    
    
elif (ksecim=="icm"):
    bsecim=input("tall,grande,vetti? Hangi boy olsun?=")
    if bsecim=="tall":
        print("hasap tutarınız:",icm*1.25)
    elif bsecim=="grande":
        print("hesap tutarınız:",icm*1.50)
    elif bsecim=="vetti":
        print("hesap tutarınız:",icm*2)
    else:
        print("gecersiz secim")
        
else:
    print("geçersiz bir secim yaptınız lütfen belirtilen kahve adlarından birini girin.")
