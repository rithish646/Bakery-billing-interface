import sales_module as sale
import create_module as c
import modify_module as m
import delete_module as d
import search_module as r
def no():
    n=int(input("Choose your mode :\n 1 . USER \n 2.ADMIN \n"))
    if n ==2:
        x=int(input("ENTER THE PIN :   "))
        if x==123:
            j=int(input("Enter the mode : \n 1. Create \n 2.Modify \n 3.Delete \n 4.Search  \n 5.View the day's sales \n"))
            if j==1:
                print("Using this mode will erase all the data in inventory!!")
                ed=input("Are you sure  to continue(Y/N) : ").upper()
                if ed=='Y':
                    c.detail()
                    
                else:
                    no()

            elif j==2:
                m.modification()
                
            elif j==3:
                d.deleting()

            elif j==4:
                r.display()
                r.search()
            elif j==5:
                s=open("stock.csv",'r')
                t=open("tally.csv",'r')
                sr=list(next(csv.reader(s)))
                tr=list(next(csv.reader(t)))
                print("                                     stock in store                                              ")
                print("-----------------------------------------------------------------------------------------------------------------")
                print("Itemno        Item name           Price(in Rs)        Quantity             Mfgdate                   Expdate")
                print("-----------------------------------------------------------------------------------------------------------------")
                for el in sr:
                    print(el[0],'               ',  el[1].center(11,' '),'              ',   el[2],'                ',   el[3],'            ',   el[4] ,'             ',   el[5])
                print("-----------------------------------------------------------------------------------------------------------------")
                s.close()
                print("                                        Day's sales                                            ")
                print("-----------------------------------------------------------------------------------------------------------------")
                print("Item Name            Quantity")
                print("-----------------------------------------------------------------------------------------------------------------")
                for lm in tr:
                    print(lm[0].center(11,' '),'            ',lm[1])
                print("-----------------------------------------------------------------------------------------------------------------")
                    
                
            else:
                print("Invalid mode")
                e=input("Do yo want to continue(Y/N) : ").upper()
                if e==Y:
                    no()
                    
        else:
            print("Wrong pin")
            l=input("Do yo want to continue(Y/N) : ").upper()
            if l=='Y':
                no()
                
    elif n==1:
        sale.display()
        sale.shop()
        
    else:
        print("Invalid code")
        yn=input("Do yo want to continue(Y/N) : ").upper()
        if yn==Y:
            no()
        
no()

              
        
