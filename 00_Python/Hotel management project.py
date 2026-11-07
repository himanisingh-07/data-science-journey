
#HOTEL MANAGEMENT PROJECT.

print("===============================HIMALAYA HOTEL==================================")
print()
print("MENU:\n1.BREAK FAST(7:00AM-11:AM)\n2.LUNCH(12:00PM-4:00PM)\n3.SNACKS(4:30PM-7:00PM)\n4.DINNER(7:00PM-10:00PM)")
opt='y'
bal=0
while (opt=='y'):
    opt1=int(input("Please enter your option(1, 2, 3 ,4):"))
    print()
    if opt1==1:
        print("Welcome to the Break fast menu:")
        print("1.Chai-Rs.20\n2.Maggi-Rs.40\n3.Veg poha-Rs.70\n4.Veg rolls(5 pieces)-Rs.80\n5.Veg sandwich(4 slices)-Rs.100")
        opt_1=int(input("Please enter your option(1, 2, 3, 4, 5):"))
        if opt_1==1:
            print("You have selected chai.....Enjoy!!!!")
            bal+=20
        elif opt_1==2:
            print("You have selected Maggi.....Enjoy!!!!")
            bal+=40
        elif opt_1==3:
            print("You have selected Veg poha......Enjoy!!!!")
            bal+=70
        elif opt_1==4:
            print("You have selected Veg rolls.....Enjoy!!!!")
            bal+=80
        elif opt_1==5:
            print("You have selected Veg sandwich.....Enjoy!!!!")
            bal+=100
        else:
            print("INVALID CHOICE...Try again and choose the correct option")
            
    
    elif opt1==2:
        print("Wel-Come to the lunch menu:")
        print("1.Tandoori naan(Plain/Butter)-Rs.20\n2.Tandoori roti(Plain/Butter)-Rs.15\n3.Paneer Butter masala-Rs.80\n4.Veg Biryani-Rs.100\n5.Dal makhni-Rs.80\n6.Dal Tadka-Rs.70\n7.Rice-Rs.60")
        opt_2=int(input("Please enter your option(1, 2, 3, 4, 5, 6, 7):"))
        if opt_2==1:
            print("You have selected Tandoori naan.....Enjoy!!!!")
            bal+=20
        elif opt_2==2:
            print("You have selected Tandoori roti.....Enjoy!!!!")
            bal+=15
        elif opt_2==3:
            print("You have selected Paneer Butter masala......Enjoy!!!!")
            bal+=80
        elif opt_2==4:
            print("You have selected Veg Biryani.....Enjoy!!!!")
            bal+=100
        elif opt_2==5:
            print("You have selected Dal makhni.....Enjoy!!!!")
            bal+=80
        elif opt_2==6:
            print("You have selected Dal Tadka.....Enjoy!!!!")
            bal+=70
        elif opt_2==7:
            print("You have selected Rice.....Enjoy!!!!")
            bal+=60
        else:
            print("INVALID CHOICE...Try again and choose the correct option")

    elif opt1==3:
        print("Wel-Come to the Snacks menu:")
        print("1.Tomato soup-Rs.30\n2.Green salad-Rs.30\n3.Coffee-Rs.40\n4.Cold Drinks-Rs.20 each")
        opt_3=int(input("Please enter your option(1, 2, 3, 4):"))
        if opt_3==1:
            print("You have selected Tomato soup.....Enjoy your soup!!!!")
            bal+=30
        elif opt_3==2:
            print("You have selected Green salad.....Enjoy your healthy diet!!!!")
            bal+=30
        elif opt_3==3:
            print("You have selected Coffee......Enjoy the Beverage!!!!")
            bal+=40
        elif opt_3==4:
            print("You have selected Cold Drinks.....Enjoy having it!!!!")
            bal+=20
        else:
            print("INVALID CHOICE...Try again and choose the correct option")

    elif opt1==4:
        print("Welcome to the Dinner menu:")
        print("1.Chai-Rs.20\n2.Roti sabji-Rs.40\n3.Plain rice and dal-Rs.60\n4.Chinese noodles-Rs.60\n5.Aloo paratha-Rs.20")
        opt_4=int(input("Please enter your option(1, 2, 3, 4, 5):"))
        if opt_4==1:
            print("You have selected chai.....Enjoy!!!!")
            bal+=20
        elif opt_4==2:
            print("You have selected Roti sabji.....Enjoy!!!!")
            bal+=40
        elif opt_4==3:
            print("You have selected Plain rice and dal......Enjoy!!!!")
            bal+=60
        elif opt_4==4:
            print("You have selected Chinese noodles.....Enjoy!!!!")
            bal+=60
        elif opt_4==5:
            print("You have selected Aloo paratha.....Enjoy!!!!")
            bal+=20
        else:
            print("INVALID CHOICE...Try again and choose the correct option")

    else:
        print("INVALID CHOICE...Try again and choose the correct option")
    opt=input("SIR/MADAM do you want to order again?(y/n):")
print("SIR/MADAM your total bill is :",bal,".Rs")
print("Thanks for coming to our hotel........!!!!")
