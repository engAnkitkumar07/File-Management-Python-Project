#If Someone Searched On Google Tour Booking Then Will Show My Company Yorker Holidays
from win32comext.adsi.demos.scp import do_ScpCreate
class services: #class defining
    def __init__(self): #constructor
        pass
    def yorker(self): #fn defintion
        print('Welcome At //- Yorker Holiday Pvt.Ltd 🧑‍💻 -// That Is Great Choice') #dictionary of services
        service={
            1:'Coach Tour',
            2:'Domestic Tour',
            3:'Holidays Services',
            4: 'International & Domestic Travel ',
            5: 'Internation Sim Card',
            6: 'Travel Insurance',
            7:'Rail Ticketing',
            8:'Travel Related Services',

        }
        print("These Are All My Services")
        for key,value in enumerate(service):
            print(key+1,":",service[value])

        pick=int(input("As Your Plan Choice Above Given Services Enter Only Number 🗺️ "))
        print(pick)

        if pick==1:
            print(f'You Picked {service[1]} Service ')
            print("Your Choice Is Great👍")
            tour_name=input("Enter Your Tour Name")
            duration=input("Enter Your Duration 5 Days/4 Night")
            start_loc=input("Enter Your Starting Location")
            end_loc = input("Enter Your Ending Location")
            tour_type=input("Enter Your Tour Type AC Sleeper / None Ac")
            timing=input("Enter Your Timing..⏲️")

            print("Hotel Accommodation -->>")

            hotel_name=input("Enter Your Hotel Name")
            room_type=input('Enter Room Type Twin Sharing ')
            rating=int(input('Enter Your Hotel Rating '))

            print(" Prices Details-->> ")

            print("Adults Prices--/12,500")
            print("Child Prices--/6,500")

            #Discount
            print("Enter No. Of People For Discount")
            people=int(input())

            if people>=4:

                print("Congrates You Got it 10% Off")
                print("Please Tell Me How Many Adult In your Tour")

                adult_no=int(input())
                adult_price=adult_no*12500

                print(f"Only {adult_no} Adult {adult_price} Prices")

                children=people-adult_no
                child_price=children*6500
                print(f"Only {children} Children {child_price} Prices")
                discount=(child_price + adult_price)*10//100
                print(f"Before Discount Your Tour Price -/{child_price + adult_price} ",)
                print("Your discount price will be this-/",discount)

                print(f"Your Total Prices After discount -/{(child_price + adult_price)-discount}")
            else:
                print("OHH!")
        per=int(input("Do You Want To Clip Of Your Information Yes-1, Not-2"))
        if per==1:

            print(f"Your Service Name---{service[1]}--------\n")
            print(f"Your Tour Name---{tour_name}--------\n")
            print(f"Your duration Name--->>>{duration}--------\n")
            print(f"Your start_location >>>{start_loc}<<<<\n")
            print(f"Your Ending location  Name---{end_loc}--------\n")
            print(f"Your Tour_Type Name---{tour_type}--------\n")
            print(f"Your Timing Name---{timing}--------\n")
            print(f"Your Hotal_Name Name---{hotel_name}--------\n")
            print(f"Your Room_type Name---{room_type}--------\n")
            print(f"Your Rating of hotel---{rating}--------\n")
            print(f"People of your tour---{people}--------\n")
            print(f"Your Total Price ---{child_price+adult_price}--------\n")
            print("Click Here for printing your data THANK YOU ")

        else:
            print("Your Data Will Keep Secure ")
obj=services()

print("Searched Your Thoughts 💭 In Given Lists"
      " ['Tour 🪂','Flights Booking ✈️','Hotal Booking 🏨','Extra Services ❤️']")

while True:
# print("If You Want To Option For Revised In Other Services")
# User_press = input("Kindly Press-->A")
# if 'user_press' == 'A':

    print("0.Exit 😑")

    print("1.🪂Yorker Holiday Provides Tour Booking Services And Other Please Visit First on (www.yorkerindia.com) ")

    print("2.Flights Booking✈️ ")

    print("3.Hotal Booking 🏨 ")

    choice=int(input("enter Your Choices"))

    if choice==1:
        print("Result:",obj.yorker())
        print("I Hope You Our Services Has Proved Good Please Rate")

        Rating=int(input("Enter Your Ratings"))
        print(f"Your Rating Is {Rating} ")
    # elif choice==2:
    #     print("Result :",)
    #
    # elif choice==3:
    #     print("Result :",)
    #
    # elif choice==4:
    #     print("Result :",)







