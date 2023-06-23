status=True

product=[]

product_price=[]

while status:
    menu="""
                press 1 for generate note
                press 2 for view note
                press 3 for exit
    """
    print(menu)

    user_choice=int(input("Enter your choice:"))

    if user_choice==1:
        user_status=True

        while user_status:
            name=input("Enter python E-Nots name:")
            product.append(name)

            title=input("Enter python E-note title:")
            product.append((title))

            content=input("Enter python E-note content:")
            product.append((content))
            
            choice=input("do you want to add more product ? press y for yes and n for no :")
            if choice=='n' or choice=='no':
                user_status=False

    elif user_choice==2:
        price("customer panel")

        for items in range(0,len(product)):
            print(f"{product[items]} Rs. {product_price[items]}")
    else:
        print("thanku for using appliction")
        status=false