import csv#code,name,price,qty,mfg,exp
from datetime import date,timedelta
n=[]
nme=[]
def display():
    code=[]
    name=[]
    quant=[]
    price=[]
    mfg_date=[]
    exp_date=[]
    p=0
    f=open("inventory.csv",'r')
    reader=csv.reader(f)
    next(reader)
    
    for h in reader:
        if h!=[]:
            global n ,nme
            p+=1
            n=[]
            nme=[]
            code.append(h[0])
            name.append(h[1])
            quant.append(h[2])
            price.append(h[3])
            mfg_date.append(h[4])
            exp_date.append(h[5])
            n.append(h[3])
            nme.append(h[1])
            
    f.close()
    print("                                     stock in store                                              ")
    print("-----------------------------------------------------------------------------------------------------------------")
    print("Itemno        Item name           Price(in Rs)        Quantity             Mfgdate                   Expdate")
    print("-----------------------------------------------------------------------------------------------------------------")
    for x in range(p):
        print(code[x],'               ',  name[x],'              ',   price[x],'                ',   quant[x],'            ',   mfg_date[x] ,'             ',   exp_date[x])
    print("-----------------------------------------------------------------------------------------------------------------")
def modification():
    f=open("inventory.csv",'r')
    reader=csv.reader(f)
    next(reader)
    z=list(reader)
    f.close()
    for i in z:
        if i==[]:
            z.remove(i)
    m=int(input('''Do you want to,
                                       1.Add food items
                                       2.Modify existing food items :  '''))
    if m==1:
        global n ,nme
        print("Adding food item")
        w=open("inventory.csv",'a')
        writer=csv.writer(w)
        nf=[0 for x  in range(0,6) ]
        nf[0]=int(input("Enter the code : "))
        nf[1]=input("Enter the name : ").title()
        nf[2]=int(input("Enter the price : "))
        nf[3]=int(input("Enter the quantity : "))
        nf[4]=date.today()
        ed=int(input("Enter the days for product to expire : "))
        nf[5]=nf[4]+timedelta(days=ed)
        writer.writerow(nf)
        w.close()
        #stock
        info=open('stock.csv','a')
        w=csv.writer(info)
        w.writerow(nf)
        info.close()
        #inventory
        z,i,l,k=[],0,[],[]
        tally=open('tally.csv','r')
        r=csv.reader(tally)
        next(r)
        tal=list(r)
        for h in tal:
            if h==[]:
                tal.remove(h)
        ln=len(tal)
        for y in tal:
            l.append(y[0])
            k.append(y[1])
        tally.close()
        display()
        #tally write
        tally=open('tally.csv','a')
        head=['Name','Quantity']
        w=csv.writer(tally)
        i=0
        g=[]
        for o in nme:
            g.append(0)
        for s in n:
            w.writerow([nme[i],g[i]])
            i+=1
        tally.close()        
        
    elif m==2:
        print("Modifying existing items")
        w=open("inventory.csv",'w')
        cde,name,qnt,prc,mfg,exd,i=[],[],[],[],[],[],0
        stock=open("stock.csv",'r')
        reader=csv.reader(stock)
        next(reader)
        stk=list(reader)
        stock.close()
        for u in stk:
            if u ==[]:
                stk.remove(u)
            
        writer=csv.writer(w)
        head=['Itemno','Item name','Price(in Rs)','Quantity', 'Mfgdate' , 'Expdate']
        writer.writerow(head)
        r=int(input("Enter the row to be modified : "))
        c=int(input("Enter the column to be modified : "))
        if r < len(z):
            
            for x,stc in z:
                if x==z[r-1]:
                    if c==1:
                        x[0]=int(input("Enter new code : "))
                        stc[0]=x[0]
                    elif c==2:
                        x[1]=input("Enter new name : ").title()
                        stc[1]=x[1]
                    elif c==3:
                        x[2]=int(input("Enter new price : "))
                        stc[2]=x[2]
                    elif c==4:
                        r=int(input("Enter the quantity to be added : "))
                        x[3]+=r
                        stc[3]+=r
                    elif c==5:
                        print("Manufacturing date cannot be modified")
                    elif c==6:
                        x[5]+=timedelta(days=int(input("Enter the days for the product to expire : ")))
                    else:
                        print("Invalid column")

        else:
            print("Invalid row")
        writer.writerows(z)
        w.close()
