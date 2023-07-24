import csv
p=0
code=[]
name=[]
quant=[]
price=[]
mfg=[]
exp=[]


def display():
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
            mfg.append(h[4])
            exp.append(h[5])
    f.close()
        
        
    
    print("                                     stock in store                                              ")
    print("-----------------------------------------------------------------------------------------------------------------")
    print("Itemno        Item name           Price(in Rs)        Quantity             Mfgdate                   Expdate")
    print("-----------------------------------------------------------------------------------------------------------------")
    for x in range(p):
        print(code[x],'               ',  name[x],'              ',   price[x],'                ',   quant[x],'            ',   mfg[x] ,'             ',   exp[x])
    print("-----------------------------------------------------------------------------------------------------------------")
def search():
    m=len(code)
    print(m)
    if True:
        f=int(input('''Search by
                                  1.Food ID
                                      2.Food Name \n     '''))
        if f==1:
            a=input("Enter the ID of the food: ").title()
            print(a)
            for w in range(0,m):
                if a == code[w]:
                    print("hii")
                    print("Itemno        Item           Price(in Rs)        Quantity             Mfgdate                   Expdate")
                    print("-----------------------------------------------------------------------------------------------------------------")
                    print(code[w],'               ',  name[w],'              ',   price[w],'                ',   quant[w],'            ',   mfg[w] ,'             ',   exp[w])         
        elif f==2:
            fnm=input("Enter the name of the food: ").title()
            for w in range(0,m):
                if fnm==name[w]:
                    print("Itemno        Item           Price(in Rs)        Quantity             Mfgdate                   Expdate")
                    print("-----------------------------------------------------------------------------------------------------------------")
                    print(code[w],'               ',  name[w],'              ',   price[w],'                ',   quant[w],'            ',   mfg[w] ,'             ',   exp[w])

