import csv
def deleting():
    cde,nme,prc,qnt,mfgd,expd=[],[],[],[],[],[]
    f=open("inventory.csv",'r')
    reader=csv.reader(f)
    next(reader)
    a=list(reader)
    f.close()
    for h in a:
        if h==[]:
            a.remove(h)
    zn=len(a)
    for row in a:
        cde.append(row[0])
        nme.append(row[1])
        prc.append(row[2])
        qnt.append(row[3])
        mfgd.append(row[4])
        expd.append(row[5])
    print("                                     stock in store                                                      ")
    print("-----------------------------------------------------------------------------------------------------------------")
    print("Itemno        Item name           Price(in Rs)        Quantity             Mfgdate                   Expdate")
    print("-----------------------------------------------------------------------------------------------------------------")
    for x in range(zn):
        print(cde[x],'               ',  nme[x],'              ',   prc[x],'                ',   qnt[x],'            ',   mfgd[x] ,'             ',   expd[x])
    print("-----------------------------------------------------------------------------------------------------------------")
    d=int(input("Enter the row to be deleted:  "))
    del a[d-1]
    del cde[d-1]
    del nme[d-1]
    del prc[d-1]
    del qnt[d-1]
    del mfgd[d-1]
    del expd[d-1]
    ln=len(a)
    f=open("inventory.csv",'w')
    head=['Itemno','Item name','Price(in Rs)','Quantity', 'Mfgdate' , 'Expdate']
    writer=csv.writer(f)
    writer.writerow(head)
    writer.writerows(a)
    f.close()
    print("                                     stock in store                                              ")
    print("-----------------------------------------------------------------------------------------------------------------")
    print("Itemno        Item name           Price(in Rs)        Quantity             Mfgdate                   Expdate")
    print("-----------------------------------------------------------------------------------------------------------------")
    for x in range(ln):
        print(cde[x],'               ',  nme[x],'              ',   prc[x],'                ',   qnt[x],'            ',   mfgd[x] ,'             ',   expd[x])
    print("-----------------------------------------------------------------------------------------------------------------")


