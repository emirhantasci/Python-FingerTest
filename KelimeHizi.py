# -*- coding: utf-8 -*-
"""
Created on Sun Mar  6 18:23:55 2022

@author: emirh
"""

import time
import datetime

dosya = open("a.txt", "r")
satirSayisi=0

first=datetime.datetime.now()
for satir in dosya:
    before = datetime.datetime.now()
    print(satir.strip())
    text=input("Yaz: ")
    if str(text.strip().lower()) == str(satir.strip().lower()):
           after = datetime.datetime.now()
           speed = after-before
           seconds =round(speed.total_seconds(),2)
           print("Kelimeyi {} saniyede yazdın.".format(seconds))
    else:
        print("Kelimeyi yanlış yazdın.")
    satirSayisi+=1
end=datetime.datetime.now()
totalspeed = end-first
totalseconds = round(totalspeed.total_seconds(), 2)
print("Toplamda ", satirSayisi, " adet kelimeyi ", totalseconds, " saniyede yazdınız.")