import random
import time
print("***خوش امديد به قرعه کشي ما***")
time.sleep(3)
listr=[]
z=int(input("تعداد شرکت کننده وارد کنيد = "))
for i in range(z):
    x=input("شرکت کننده عزيز نام خود را وارد کنيد = ")
    listr.append(x)
for i in listr:
    print("ليست شرکت کننده ها -> ",i)
while listr:
    print("ليست قرعه کشي در حال چرخش هست")
    time.sleep(2)
    r=random.choice(listr)
    time.sleep(2)
    print("برنده قرعه کشي اين ماه -> ",r)
    time.sleep(2)
    listr.remove(r)
    time.sleep(2)
    print("افراد باقي مانده در قرعه کشي -> ",listr)
    time.sleep(2)
    print("---Repad---")
    time.sleep(4)
    if(listr==[]):
        print("قرعه کشي به پايان رسيد")
