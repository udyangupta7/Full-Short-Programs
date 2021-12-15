try:
    import logging as lg
    lg.basicConfig(filename="logging.txt",
                   filemode='a',
                   format='%(asctime)s %(levelname)s -%(message)s',
                   datefmt='%Y-%m-%d %H:%M:%S %A')
    while True:
        print("WELCOME TO THE ONLINE SHOPPING PORTAL! ENTER A CHOICE TO START:\n\t 0. HELP\t1. SHOPPING CENTRE LAYOUT\t2. MOVIE BOOKINGS\t3. TOY STORE\t4. BIG BAZAAR:")
        choice = int(input("\nENTER YOUR CHOICE HERE ---> "))
        if choice < 0 or choice > 5:
            print("\nWrong entry. Try again.\n")
        else:
            break
    if choice == 0:
        string = """
        HELLO, WELCOME TO JENNIFER LOPEZ SHOPPING CENTRE WHERE ALL YOUR NEEDS ARE FULLfilled under one roof!
        
        Under this one big building, you will find everything under one roof. Drop your infants at one of the two daycare centres or you can take them along 
        with you on our easy to pull carriages available on all floors next to the baby changing staitons. We have excellent food courts and private restaurants 
        for your evening to end on a perfect note.For any emergencis, contact Mr. Amraj, the head in charge of the security or call 911. 
              Thank you.   visit again   
        """
        print("\n",string.upper())
    elif choice == 1:
        print("""
        \nWELCOME TO THE SHOPPING CENTRE LAYOUT.
\tFLOOR 1 IS ENTIRELY DEDICATED TO THE MODERN HOME AND MODULAR NEEDS.  
\tFLOOR 2 IS FOR THE KIDS AND YOUNG ADULTS.   
        """)
    elif choice == 2:
        print("\nWELCOME TO PVR.")
        while True:
            pvr_choice = int(input("PRESS 1 FOR MOVIE TITLES CURRENTLY PLAYING OR 9 FOR OTHER OPTIONS: "))
            if pvr_choice == 1:
                print(
                    """MOVIES PLAYING CURRENTLY:\n\t1. TITANIC\n\t2. SHANG CHI- THE LEGEND OF TEN RINGS.\n\t3. INDIANA JONES- RAIDERS OF THE LOST ARC\n\t4. HE'S JUST NOT THAT INTO YOU\n\t5. DISNEY'S DUMBO""")
                while True:
                    shows_list = int(input("SELECT A MOVIE TITLE FOR THE TIMINGS: "))
                    if shows_list < 1 or shows_list > 5:
                        print(
                            "PLEASE SELECT A VALID MOVIE. \n\tMOVIES PLAYING CURRENTLY:\n\t1. TITANIC\n\t2. SHANG CHI- THE LEGEND OF TEN RINGS.\n\t3. INDIANA JONES- RAIDERS OF THE LOST ARC\n\t4. HE'S JUST NOT THAT INTO YOU\n\t5. DISNEY'S DUMBO")
                    else:
                        break
                if shows_list == 1:
                    print("\nTITANIC SHOWS ARE:\n\t1. 9:45 AM\n\t2. 11:00 AM\n\t3. 2:00 PM\n\t4. 5:00 PM\n\t5. 7:30 PM")
                    while True:
                        timing_list = int(input("SELECT YOUR PREFERRED SHOW TIME:"))
                        if timing_list < 1 or timing_list > 5:
                            print("INVALID SELECTION. PLEASE TRY AGAIN.")
                        else:
                            print("YOUR MOVIE HAS BEEN BOOKED SUCCESSFULLY. ENJOY YOUR SHOW!")
                            break
                elif shows_list == 2:
                    print(
                        "\nSHANG CHI- THE LEGEND OF TEN RINGS SHOWS ARE:\n\t1. 10:10 AM\n\t2. 12:45 PM\n\t3. 4:45 PM\n\t4. 7:40 PM")
                    while True:
                        timing_list = int(input("SELECT YOUR PREFERRED SHOW TIME:"))
                        if timing_list < 1 or timing_list > 4:
                            print("INVALID SELECTION. PLEASE TRY AGAIN.")
                        else:
                            print("YOUR MOVIE HAS BEEN BOOKED SUCCESSFULLY. ENJOY YOUR SHOW!")
                            break
                elif shows_list == 3:
                    print(
                        "\nINDIANA JONES- RAIDERS OF THE LOST ARC SHOWS ARE:\n\t1. 9:45 AM\n\t2. 11:15 AM\n\t3. 2:30 PM\n\t4. 6:00 PM\n\t5. 9:30 PM")
                    while True:
                        timing_list = int(input("SELECT YOUR PREFERRED SHOW TIME:"))
                        if timing_list < 1 or timing_list > 5:
                            print("INVALID SELECTION. PLEASE TRY AGAIN.")
                        else:
                            print("YOUR MOVIE HAS BEEN BOOKED SUCCESSFULLY. ENJOY YOUR SHOW!")
                            break
                elif shows_list == 4:
                    print("\nHE'S JUST NOT THAT INTO YOU SHOWS ARE:\n\t1. 3:45 PM\n\t2. 6:45 PM\n\t3. 9:00 PM")
                    while True:
                        timing_list = int(input("SELECT YOUR PREFERRED SHOW TIME:"))
                        if timing_list < 1 or timing_list > 3:
                            print("INVALID SELECTION. PLEASE TRY AGAIN.")
                        else:
                            print("YOUR MOVIE HAS BEEN BOOKED SUCCESSFULLY. ENJOY YOUR SHOW!")
                            break
                elif shows_list == 5:
                    print(
                        "\nHE'S JUST NOT THAT INTO YOU SHOWS ARE:\n\t1. 10:10 AM\n\t2. 12:30 PM\n\t3. 3:00 PM\n\t4. 5:45 PM\n\t5. 8:30 PM\n\t6. 9:30 PM")
                    while True:
                        timing_list = int(input("SELECT YOUR PREFERRED SHOW TIME:"))
                        if timing_list < 1 or timing_list > 6:
                            print("INVALID SELECTION. PLEASE TRY AGAIN.")
                        else:
                            print("YOUR MOVIE HAS BEEN BOOKED SUCCESSFULLY. ENJOY YOUR SHOW!")
                            break


                break
            elif pvr_choice == 9:
                print("WELCOME TO PVR. PlEASE CONTACT THE HELP DESK FOR ANY AND ALL BOOKING RELATED ISSUES.")
                feedback = str(input("\n\tPLEASE DROP YOUR FEEDBACK HERE: "))
                print("YOUR FEEDBACK IS:", feedback)
                break
            else:
                print("WRONG CHOICE. TRY AGAIN.")
    elif choice == 3:
        while True:
            toy_input = int(input("""WELCOME TO THE TOY STORE. IT IS LOCATED ON THE 2ND FLOOR, RIGHT NEXT THE CRECHE AND BABY SITTING SECTION.\t
        PRESS 0 TO FIND THE CONTACT INFORMATION.
        PRESS 1 TO ORDER TOYS ONLINE AND PICK THEM UP AT THE STORE. (DELIVERY WILL BE STARTING SOON.)
        PRESS 2 TO CONTACT THE DELIVERY CENTRE FOR ALL THINGS RELATED TO DELIVERY.
        MAKE A CHOICE: """))
            if toy_input == 0:
                print("YOU CAN CONTACT 1800-2345-2394 FOR ANY GRIEVANCE AND 1800-2345-2395 FOR ALL STORE RELATED QUERIES.")
                break
            elif toy_input == 1:
                toy_email = str(input("ONLINE STORE COMING SOON. WE WILL KEEP YOU UPDATED. LEAVE YOUR EMAIL ID BELOW TO HELP US TO KEEP US UPDATED: "))
                break
            elif toy_input == 2:
                toy_order = int(input("ENTER YOUR ORDER ID: "))
                print("YOUR ORDER WILL BE DELIVERED BETWEEN THE NEXT 2 TO 4 DAYS. FOR ANY OTHER ASSISTANCE, PLEASE CONTACT THE HELP DESK AT THE STORE.")
                break
            elif toy_input != 0 or toy_input != 1 or toy_input != 2:
                print("WRONG INPUT. PLEASE TRY AGAIN.\n")
    elif choice == 4: print("WELCOMNE TO BIG BAZAAR, A STORE FOR ALL YOUR DAILY NEEDS. PLEASE VISIT US IN THE BASEMENT.")
except Exception as e:
    print("Please check the logging file for error.")
    lg.error("Error found in the code. Pl rectify and try again.")