from lib import Student


users=[]

def daxilet():
    ad=input("Ad:")
    soyad=input("Soyad:")
    username=input("Username:")
    password=input("Pass:")
    return[ad,soyad,username,password]



def qeydiyyat():
    sayi=int(input("nece dene telebe elave etmek isteyirsiz:"))
    for user in range(sayi):
        user=Student(*daxilet())
        users.append(user)


def datanigoster():
    for user in users:
        user.show()



def axtar(ad):
    for user in users:
        if user.ad==ad:
            user.show()
        elif not( user.ad==ad):
            print("yoxdu bele bir sey")

list1=[]
list2=[]

def longest_name():
    for user in users: 
        t = len(user.ad)
        list1.append(t)
        list2.append(user.ad)
    list1.sort()
    for i in list2:
        if len(i) == list1[-1]:
            print(i)
        else:
            pass

def soyad():
    for user in users:
        if "ov" in user.soyad:
            user.show()

def sifre():
    for user in users:
        if len(user.password)>8:
            user.show()

            




print("1.Qeydiyyat elemek ucun 1 deymesin bas ")

ch=int(input("Reqem yaz:"))


if ch==1:
    qeydiyyat()
    datanigoster()


print("1.Qeydiyyat elemek ucun 1 deymesin bas \n 2. axtarmaq ucun 2 duymesin basin \n 3. En uzun istifadeci adi olani tapmaq ucun 3 duymesin basin \n .4 Soyadinda ov olanlar ucun 4 duymesin basin \n 5. sifre uzunlugu 8den boyuk olanlar ucun 5 duymesini basin ")

ch=int(input("Reqem yaz:"))

if ch==2:
    ad=input("ad daxil ele")
    axtar(ad)


if ch==3:
    longest_name()

if ch==4:
    soyad()

if ch==5:
    sifre()



    

        














