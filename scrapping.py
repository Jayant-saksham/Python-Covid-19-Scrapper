import json
import requests
from win10toast import ToastNotifier
toaster = ToastNotifier()

stacks = []
class DataStructure():
    '''Data Structure class helper'''
    def stack(self):
        print("Enter y to display : ")
        c = input("Your choice : ")
        if c=='y' or c=='Y':
            print(stacks)
        else:
            pass
    


class Covid():
    '''Covid 19 data helper helper class'''
    def check_all_countries(self):
        response = requests.get("https://disease.sh/v3/covid-19/countries")
        countries = json.loads(response.text)
        for i in range(len(countries)):
            print(countries[i]['country'])

    # Function for world's data country wise
    def queryFunctionWorld(self):
        print("DO you want to see country list ? y for yes")
        myChoice = input("Your choice : ")
        if myChoice =='y' or myChoice == 'Y':
            self.check_all_countries()
        else:
            pass    
        country = input("Enter your country : ")
        try:
            response = requests.get('https://disease.sh/v3/covid-19/countries')
        except:
            print("Error, Something went wrong")

        country_found = False
        countries = json.loads(response.text)
        for i in range(len(countries)):
            if countries[i]['country'] == country:
                country_found = True
                png_icon = countries[i]['countryInfo']['flag']
                print("Enter 1 to get total cases")
                print("Enter 2 to get total recoverd cases")
                print("Enter 3 to get cases today")
                print("Enter 4 to get today's recovered cases today")
                print("Enter 5 to get active cases")
                print("Enter 6 to get total population")
                try:
                    choice = int(input("Enter your choice : "))
                    if choice == 1:
                        toaster.show_toast(
                            f"Total cases in {countries[i]['country']}",
                            f"{countries[i]['cases']}",
                            duration=6
                        )
                        return (f"Total cases {countries[i]['cases']}")
                    elif choice == 2:
                        toaster.show_toast(
                            f"Total recovered cases in {countries[i]['country']}",
                            f"{countries[i]['recovered']}",
                            duration=6
                        )
                        return (f"Recovered cases {countries[i]['recovered']}")
                    elif choice == 3:
                        toaster.show_toast(
                            f"Today's cases in {countries[i]['country']}",
                            f"{countries[i]['todayCases']}",
                            duration=6
                        )
                        return (f"Today's cases {countries[i]['todayCases']}")
                    elif choice == 4:
                        toaster.show_toast(
                            f"Today's recovered cases in {countries[i]['country']}",
                            f"{countries[i]['todayRecovered']}",
                            duration=6
                        )
                        return (
                            f"Today's recovered cases {countries[i]['todayRecovered']}")
                    elif choice == 5:
                        toaster.show_toast(
                            f"Active cases in {countries[i]['country']}",
                            f"{countries[i]['active']}",
                            duration=6
                        )
                        return (f"Active cases {countries[i]['active']}")
                    elif choice == 6:
                        toaster.show_toast(
                            f"Total population of {countries[i]['country']}",
                            f"{countries[i]['population']}",
                            duration=6
                        )
                        return (
                            f"Total population of {countries[i]['country']} is {countries[i]['population']}")
                    else:
                        toaster.show_toast(
                            "Error",
                            "Something went wrong",
                            duration=6
                        )
                        print("Invalid choice ")
                except:
                    toaster.show_toast(
                        "Error",
                        "Something went wrong",
                        duration=6
                    )
                    print("Something when wrong")
        if not country_found:
            toaster.show_toast(
                "Error",
                "Country not found",
                duration=4
            )

    # Function for India's data statewise
    def queryFunctionIndia(self):
        print("For India")
        state = input("Enter state : ")
        try:
            response = requests.get(
                'https://api.covidindiatracker.com/state_data.json')
        except:
            print("Error, Something went wrong")

        state_found = False
        countries = json.loads(response.text)
        for i in range(len(countries)):
            if countries[i]['state'] == state:
                state_found = True
                print("Enter 1 to get total cases")
                print("Enter 2 to get total recoverd cases")
                print("Enter 3 to get cases today")
                print("Enter 4 to get today's recovered cases today")
                print("Enter 5 to get active cases")
                print("Enter 6 to get total population")
                try:
                    choice = int(input("Enter your choice : "))
                    if choice == 1:
                        toaster.show_toast(
                            f"Total cases in {countries[i]['state']}",
                            f"{countries[i]['confirmed']}",
                            duration=6
                        )
                        return (f"Total cases {countries[i]['confirmed']}")
                    elif choice == 2:
                        toaster.show_toast(
                            f"Total recovered cases in {countries[i]['country']}",
                            f"{countries[i]['recovered']}",
                            duration=6
                        )
                        return (f"Recovered cases {countries[i]['recovered']}")
                    elif choice == 3:
                        toaster.show_toast(
                            f"Today's cases in {countries[i]['country']}",
                            f"{countries[i]['todayCases']}",
                            duration=6
                        )
                        return (f"Today's cases {countries[i]['todayCases']}")
                    elif choice == 4:
                        toaster.show_toast(
                            f"Today's recovered cases in {countries[i]['country']}",
                            f"{countries[i]['todayRecovered']}",
                            duration=6
                        )
                        return (
                            f"Today's recovered cases {countries[i]['todayRecovered']}")
                    elif choice == 5:
                        toaster.show_toast(
                            f"Active cases in {countries[i]['country']}",
                            f"{countries[i]['active']}",
                            duration=6
                        )
                        return (f"Active cases {countries[i]['active']}")
                    elif choice == 6:
                        toaster.show_toast(
                            f"Total population of {countries[i]['country']}",
                            f"{countries[i]['population']}",
                            duration=6
                        )
                        return (
                            f"Total population of {countries[i]['country']} is {countries[i]['population']}")
                    else:
                        toaster.show_toast(
                            "Error",
                            "Something went wrong",
                            duration=6
                        )
                        print("Invalid choice ")
                except:
                    toaster.show_toast(
                        "Error",
                        "Something went wrong",
                        duration=6
                    )
                    print("Something when wrong")
        if not state_found:
            toaster.show_toast(
                "Error",
                "Country not found",
                duration=4
            )

# Menu function
def menu():
    print("Enter 1 to get data country wise")
    print("Enter 2 to get data of India only")
    print("Any key to exit")


# Driver function
if __name__ == "__main__":
    object = Covid()
    while True:
        menu()
        try:
            choice = int(input("Enter your choice : "))
        except:
            print("Something went wrong")
            break
        if choice == 1:
            object.queryFunctionWorld()
        elif choice == 2:
            object.queryFunctionIndia()
        else:
            print("Exiting....")
            break