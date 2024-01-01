def fruit_store():
    print("\n\n\t\t WELCOME TO FRUIT MARCKET\n")
    print("\t\t1)  MANAGER")
    print("\t\t2)  CUSTOMER\n\n")

    a=int(input("enter your role: "))
    one=("ADD FRUIT STOCK")
    two=("VIEW FRUIT STOCk")
    three=("UPDATE FRUIT STOCK")

    if a==1:
        print("\n\n\t\tFRUIT MARCKET MANAGER\n")
        print("\t\t1)",one)
        print("\t\t2)",two)
        print("\t\t3)",three,"")       
    

    b=int(input("enter your choice: "))

    if b==1:
        NAME=str(input("ENTER FRUIT NAME: "))
        QTY=int(input("ENTER QTY(IN KG): "))
        PRICE=int(input("ENTER PRICE"))
        print("\n\n")

        NEXT=str(input("DO YOU WANT PERFORM MORE OPRATIONS : PRESS 'Y' FOR YES AND 'N' FOR NO :"))
        print("\n\n")
        if NEXT=="Y" or NEXT=="y":
            NAME1=str(input("ENTER FRUIT NAME: "))
            QTY1=int(input("ENTER QTY(IN KG): "))
            PRICE1=int(input("ENTER PRICE: "))

    elif b==2:
        print("\n\n'",NAME,"'",{"QTY:",QTY,'PRICE',PRICE,"\n\n"})

        

    b=int(input("enter your choice: "))

    if b==1:
        NAME1=str(input("ENTER FRUIT NAME: "))
        QTY2=int(input("ENTER QTY(IN KG): "))
        PRICE=int(input("ENTER PRICE"))

    elif b==2:
        print("\n\n",NAME,{"QTY:",QTY,"PRICE:",PRICE})
        print(NAME1,{"QTY:",QTY1,"PRICE:",PRICE1 })
    
fruit_store()