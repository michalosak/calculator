#!/usr/bin/env python
# -*- coding: utf-8 -*-
def isanumber(a): #check that number is integer
    boola= True
    try:
        boola=int(a)
        return True
    except:
        boola= False
        return False

hallway_doors=[]
open_doors=[]
otwarte=str()

ile_razy = input("How many times do you want to walk throught hallway? (default 100) ")

if (isanumber(ile_razy)==False):
    ile_razy=100

for drzwi in range(0,100):
    hallway_doors.append('closed')



for ilosc_przejsc in range(0,int(ile_razy)):

    przejscie=0

    for door in range(len(hallway_doors)):

        przejscie+=1
        co_ktore_otwieramy=ilosc_przejsc+1

        if (przejscie==co_ktore_otwieramy):
            przejscie=0
            if (hallway_doors[door]=="open"):
                hallway_doors[door]="closed"
            else:
                hallway_doors[door]="open"

        if (ilosc_przejsc+1==int(ile_razy) and hallway_doors[door]=="open"):
            otwarte+=str(door+1)+", "

print()
print("Following doors are open: " +otwarte)
