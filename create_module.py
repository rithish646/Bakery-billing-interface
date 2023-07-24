from datetime import date,timedelta
import csv
code=[]
name=[]
quant=[]
price=[]
mfg_date=[]
exp_date=[]
p=0
def detail():
    v=int(input("Enter the no of items :  "))
    global p
    p=v
    for x in range(0,v):
        code.append(int(input("Enter the item Code :  ")))
        name.append(input("Enter the item name :  " ).title())
        quant.append(int(input("Enter the quantity :  ")))
        price.append(int(input("Enter the price :  ")))
        mfg_date.append(date.today())
        exb=date.today()+timedelta(days=int(input("Enter the days to expire : ")))
        exp_date.append(exb)
    save()        
def save():
    #stock
    info=open('stock.csv','w')
    head=['Itemno','Item name','Price(in Rs)','Quantity', 'Mfgdate' , 'Expdate']
    w=csv.writer(info)
    w.writerow(head)
    for x in range(0,p):
        item1=[code[x],name[x],price[x],quant[x],mfg_date[x],exp_date[x]]
        w.writerow(item1)
    info.close()
    #inventory
    data=open('inventory.csv','w')
    head=['Itemno','Item name','Price(in Rs)','Quantity', 'Mfgdate' , 'Expdate']
    w=csv.writer(data)
    w.writerow(head)
    for x in range(0,p):
        item1=[code[x],name[x],price[x],quant[x],mfg_date[x],exp_date[x]]
        w.writerow(item1)
    data.close()
    z,i=[],0
    for b in code:
        z.append(0)
        i+=1
    tally=open('tally.csv','w')
    head=['Name','Quantity']
    w=csv.writer(tally)
    w.writerow(head)
    i=0
    for s in code:
        w.writerow([name[i],z[i]])
        i+=1
    tally.close()
    display()
def display():
    f=open("inventory.csv",'r')
    reader=csv.reader(f)
    next(reader)
    global code,name,quant,price,mfg_date,exp_date
    code=[]
    name=[]
    quant=[]
    price=[]
    mfg_date=[]
    exp_date=[]
    for h in reader:
        if h!=[]:
            global p
            p+=1
            code.append(h[0])
            name.append(h[1])
            quant.append(h[2])
            price.append(h[3])
            mfg_date.append(h[4])
            exp_date.append(h[5])
    f.close()
        
        
    
    print("                                     stock in store                                              ")
    print("-----------------------------------------------------------------------------------------------------------------")
    print("Itemno        Item name           Price(in Rs)        Quantity             Mfgdate                   Expdate")
    print("-----------------------------------------------------------------------------------------------------------------")
    for x in range(len(code)):
        print(code[x],'               ',  name[x],'              ',   price[x],'                ',   quant[x],'            ',   mfg_date[x] ,'             ',   exp_date[x])
    print("-----------------------------------------------------------------------------------------------------------------")



    
