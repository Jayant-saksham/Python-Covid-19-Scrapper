import json
import requests
from win10toast import ToastNotifier
toaster = ToastNotifier()

# Data as hashmap - Wikipedia(2011)
data = {
    "Uttar Pradesh": [199812341,828],
    "Maharashtra": [112374333, 365],
    "Bihar": [104099452, 1102],
    "West Bengal": [91276115, 1029],
    "Madhya Pradesh": [72626809,236],
    "Tamil Nadu": [72147030, 555],
    "Rajasthan": [68548437, 201],
    "Karnataka": [61095297, 319],
    "Gujarat": [60439692, 308],
    "Andhra Pradesh": [49577103, 303],
    "Odisha": [41974219, 269],
    "Telangana": [35003674, 312],
    "Kerala": [	33406061, 859],
    "Assam": [31205576, 398],
    "Punjab": [27743338, 551],
    "Chhattisgarh": [25545198, 189],
    "Haryana": [25351462, 573],
    "Delhi": [16787941, 11297],
    "Jammu and Kashmir": [12267032, 297],
    "Uttarakhanda": [10086292, 189],
    "Himachal Pradesh": [6864602, 123],
    "Tripura": [3673917, 350],
    "Meghalaya": [2966889, 132],
    "Manipur": [2570390, 122],
    "Nagaland": [1978502, 119],
    "Goa": [1458545, 394],
    "Arunachal Pradesh": [1383727, 17],
    "Puducherry": [1247953, 52],
    "Mizoram": [1097206, 17],
    "Chandigarh": [1055450, 9,252],
    "Sikkim": [610577, 86],
    "Dadra and Nagar Haveli": [585764, 970],
    "Daman and Diu": [585764, 970],
    "Andaman and Nicobar Islands": [380581, 46],
    "Ladakh": [274000, 2.8],
    "Lakshadweep": [64473, 2013],
}

stacks = []
class Stacks():
    '''Stack helper class'''
    def append(self, value):
        try:
            stacks.append(value)
        except Exception as e:
            print(e)
    
    def display(self):
        print(stacks)
    def top(self):
        return stacks[-1]
    


    
class Covid():
    '''Covid 19 data helper helper class'''
    # Constructors function
    def __init__(self):
        toaster.show_toast(
            "Covid-19",
            "Narayan, lets stop the spread of virus together",
            duration=6
        )
    def menu(self):
        print("Enter 1 to get total confirmed cases")
        print("Enter 2 to get active cases")
        print("Enter 3 to get recovered cases")
        print("Enter 4 to get total deaths")
        print("Enter 5 to get total population")
        print("Enter 6 to get population density")

        
    # Function for India's data statewise
    def queryFunctionIndia(self):
        print("For India")
        try:
            response = requests.get(
                'https://api.covidindiatracker.com/state_data.json')
        except:
            print("Error, Something went wrong")

        states = json.loads(response.text)
        state_found = False
        c = input("Do you want to see state list : ")
        if c == 'y' or c=='Y':
            for i in range(len(states)):
                print(states[i]['state'])
        else:
            pass 
        state = input("Enter state : ")
        for i in range(len(states)):
            if states[i]['state'] == state:
                state_found = True
                toaster.show_toast(
                        "Covid-19",
                        f"{states[i]['state']} selected",
                        duration = 4
                )
                object.menu()
                try:
                    choice = int(input("Enter your choice : "))
                    if choice == 1:
                        toaster.show_toast(
                            f"Total cases in {states[i]['state']}",
                            f"{states[i]['confirmed']}",
                            duration=4
                        )
                        return (
                            states[i]['state'] , states[i]['confirmed'],data[states[i]['state']][0], data[states[i]['state']][1]
                        )
                    elif choice == 2:
                        toaster.show_toast(
                            f"Total active cases in {states[i]['state']}",
                            f"{states[i]['active']}",
                            duration=4
                        )
                        return (
                            states[i]['state'] , states[i]['confirmed'],data[states[i]['state']][0], data[states[i]['state']][1]
                        )
                    elif choice == 3:
                        toaster.show_toast(
                            f"Total recovered in {states[i]['state']}",
                            f"{states[i]['recovered']}",
                            duration=4
                        )
                        return (
                            states[i]['state'] ,states[i]['confirmed'], data[states[i]['state']][0], data[states[i]['state']][1]
                        )
                    elif choice == 4:
                        toaster.show_toast(
                            f"Total deaths in {states[i]['state']}",
                            f"{states[i]['deaths']}",
                            duration=4
                        )
                        return (
                            states[i]['state'] ,states[i]['confirmed'], data[states[i]['state']][0], data[states[i]['state']][1]
                        )
                    
                    elif choice == 5:
                        toaster.show_toast(
                            f"Total population of {states[i]['state']}",
                            f"{data[states[i]['state']][0]}",
                            duration=4
                        )
                        return (
                            states[i]['state'] ,states[i]['confirmed'], data[states[i]['state']][0], data[states[i]['state']][1]
                        )
                    elif choice == 6:
                        toaster.show_toast(
                            f"Population density of {states[i]['state']}",
                            f"{data[states[i]['state']][1]}",
                            duration=4
                        )
                        return (
                            states[i]['state'] ,states[i]['confirmed'], data[states[i]['state']][0], data[states[i]['state']][1]
                        )
                    else:
                        toaster.show_toast(
                            "Error",
                            "Something went wrong. Wrong choice",
                            duration=4
                        )
                        print("Invalid choice ")
                except:
                    toaster.show_toast(
                        "Error",
                        "Something went wrong",
                        duration=4
                    )
                    print("Something when wrong")
                    
                   
        
        if not state_found:
            toaster.show_toast(
                "Error",
                "State not found, Check your spelling",
                duration=4
            )
        elif state_found:
            print("Found")
            


# Driver function
if __name__ == "__main__":
    object = Covid()
    def shortMenu():
        print("Enter t if you are from town : ")
        print("Enter c if you are from city : ")
        print("Enter v if you are from village : ")

    while True:
        try:
            choice = int(input("Enter 1 to start :  "))
        except:
            print("Something went wrong")
            break
        if choice == 1:
            state_got,confirmed_got,population_got,population_density_got = object.queryFunctionIndia()
            positive_probability = confirmed_got/population_got
            positive_probability = positive_probability*100
            print("Percentage positive", positive_probability)   
            if positive_probability>=0.1 and positive_probability<0.2:
                rating = 0
            elif positive_probability>=0.2 and positive_probability<0.3:
                rating = 1
            elif positive_probability>=0.3 and positive_probability<0.4:
                rating = 2
            elif positive_probability>=0.4 and positive_probability<0.5:
                rating = 3
            elif positive_probability>=0.5 and positive_probability<0.6:
                rating = 4
            elif positive_probability>=0.6 and positive_probability<1:
                rating = 5
            elif positive_probability>=1 and positive_probability<1.5:
                rating = 6
            elif positive_probability>=1.5 and positive_probability<2:
                rating = 7
            elif positive_probability>=2 and positive_probability<3:
                rating = 8
            elif positive_probability>=3 and positive_probability<4:
                rating = 9
            else:
                rating = 10
            
            print(rating)
            rating401 = rating*0.4
            stackObject = Stacks()
            print(round(rating401, 0), "added")
            stackObject.append(round(rating401, 0))

            if population_density_got>=0 and population_density_got<100:
                ratingdensity = 0
            elif population_density_got>=100 and population_density_got<150:
                ratingdensity = 1
            elif population_density_got>=150 and population_density_got<200:
                ratingdensity = 2
            elif population_density_got>=200 and population_density_got<250:
                ratingdensity = 3
            elif population_density_got>=250 and population_density_got<300:
                ratingdensity = 4
            elif population_density_got>=300 and population_density_got<350:
                ratingdensity = 5
            elif population_density_got>=350 and population_density_got<400:
                ratingdensity = 6
            elif population_density_got>=400 and population_density_got<450:
                ratingdensity = 7
            elif population_density_got>=450 and population_density_got<500:
                ratingdensity = 8
            elif population_density_got>=500 and population_density_got<550:
                ratingdensity = 9
            else:
                ratingdensity = 10
            shortMenu()
            c = input("Your choice : ")
            if c == 'c' or c == 'C':
                ratingdensity = ratingdensity*2
            elif c == 'v' or c == 'V':
                ratingdensity = ratingdensity*0.5
            else:
                print("Wrong choice")

            ratingdensity = ratingdensity / 2
            ratingdensity = ratingdensity * 0.4
            rating402 = rating401 + ratingdensity
            add = round(rating402,0)
            print(add, "added")
            stackObject.append(add)
            print("How much crowded place you have visited in past 15 days")
            print("Rate yourself from 0 - 10")
            try:
                visitedRating = int(input("You choice : "))
            except:
                print("Something went wrong")
                break 
            visitedRating = visitedRating * 0.1

            rating403 = rating402 + visitedRating
            add = round(rating403,0)
            print(add, "added")
            stackObject.append(add)
            print("HOw many days you have visted such crowded place in past days")
            print("Rate yourself from 0 - 10")
            try:
                daysRating = int(input("You choice : "))
            except:
                print("Something went wrong")
                break 
            daysRating = daysRating * 0.1
            rating404 = rating403 + daysRating
            add = round(rating404, 0)
            print(add, "added")
            stackObject.append(add)
            stackObject.display()
            top = stackObject.top()
            print(top)
            print(f"Probability is {top/10}")
            toaster.show_toast(
                "Probability is",
                f"{top/10}",
                duration=4
            )
            
        else:
            print("Exiting....")
            break
    
    stacks.clear()