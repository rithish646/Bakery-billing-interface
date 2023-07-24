import csv

code=[]
name=[]
quant=[]
price=[]
mfg_date=[]
exp_date=[]
p=0
prod_quant=[]
index=[]
a=[]
lst=[]
c=0
d=0

def display():
    print("\t\t LLOYDS BAKERY  \n")
    f=open("inventory.csv",'r')
    reader=csv.reader(f)
    next(reader)
    
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
    for x in range(p):
        print(code[x],'               ',  name[x],'              ',   price[x],'                ',   quant[x],'            ',   mfg_date[x] ,'             ',   exp_date[x])
    print("-----------------------------------------------------------------------------------------------------------------")
def shop():
    
    for s in code:
        prod_quant.append(0)
    i=input("DO YOU WANT TO SHOP :  ").lower()
    while(i=='y'):
        
        global d,index,lst,a
        a,index,lst=[],[],[]
        d+=1
        c=input("Enter The Item Name :  ").title()
        if c in name:
            a.append(c)
            index.append(name.index(c))
            lst.append(int(input("Enter the quantity :  ")))
        else:
            print("No  Such Item Exists ")
            t=input(" Try Again ?? (y/n) ? ").lower()
            if t == 'y':
                shop()
            
        i=input(  "CONTINUE SHOPPING (y/n) :").lower()
        

    if i=='n':
        con=input("Submit your order (y/n) :   ").lower()
        if con=='n' :
            shop()

        if con=='y':
            prod_code=[]
            prod_name=[]
            cost_price=[]
            qnty=[]
            mfg_date1=[]
            exp_date1=[]
            tcost=0
            i=0
            print(lst)
            for x in a:
            
                prod_code.append(code[index[i]])
                prod_name.append(name[index[i]])
                mfg_date1.append(mfg_date[index[i]])
                exp_date1.append(exp_date[index[i]])
                qnty.append(lst[i])
                cost_price.append(qnty[i]*int(price[index[i]]))
                tcost+=qnty[i]*int(price[index[i]])
                i+=1
            
            i=0
            
            print("                                       Your Bill                                             ")
            print("-----------------------------------------------------------------------------------------------------------------")
            print("Itemno        Item name           Price(in Rs)        Quantity             Mfgdate                   Expdate")
            print("-----------------------------------------------------------------------------------------------------------------")
            for x in range(len(prod_code)):
                print(prod_code[x],'               ',  prod_name[x],'              ',   cost_price[x],'                ',   qnty[x],'            ',   mfg_date1[x] ,'             ',   exp_date1[x])
            print("-----------------------------------------------------------------------------------------------------------------")
            print("Total  Cost :  ", tcost)
            for n in index:
                prod_quant[n]=qnty[i]
                i+=1
            
            data=open('bill.csv','a')
            w=csv.writer(data)
            for x in range(0,d):
                item1=[prod_code[x],prod_name[x],cost_price[x],qnty[x],mfg_date1[x],exp_date1[x]]
                w.writerow(item1)        
            data.close()
            global quant
            i=0
            b=[]
        
            for x in qnty:
                c=int(quant[i])
                c-=x
                quant[i]=c
                i+=1
            data=open('inventory.csv','w')
            head=['Itemno','Item name','Price(in Rs)','Quantity', 'Mfgdate' , 'Expdate']
            w=csv.writer(data)
            w.writerow(head)
        
            for x in range(0,p):
                item1=[code[x],name[x],price[x],quant[x],mfg_date[x],exp_date[x]]
                w.writerow(item1)
            data.close()
            z,i,l,k=[],0,[],[]
            #tally open
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
            #tally write
            tally=open('tally.csv','w')
            head=['Name','Quantity']
            w=csv.writer(tally)
            w.writerow(head)
            i=0
            g=[]
            g.extend(code)
        
            for s in code:
                w.writerow([name[i],int(prod_quant[i])+int(k[i])])
                i+=1
            tally.close()


                        


            
        



           

