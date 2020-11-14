import json
import requests
from win10toast import ToastNotifier
from PIL import Image
toaster = ToastNotifier()


class Covid():
    '''Project helper class'''

    def fetch_data(self):
        response = requests.get("https://disease.sh/v3/covid-19/countries")
        countries = json.loads(response.text)
        number_of_countries = len(countries)
        print(number_of_countries)
        for i in range(len(countries)):
            print(countries[i]['country'])

    def queryFunction(self):
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
                        print(f"Total cases {countries[i]['cases']}")
                    elif choice == 2:
                        toaster.show_toast(
                            f"Total recovered cases in {countries[i]['country']}",
                            f"{countries[i]['recovered']}",
                            duration=6
                        )
                        print(f"Recovered cases {countries[i]['recovered']}")
                    elif choice == 3:
                        toaster.show_toast(
                            f"Today's cases in {countries[i]['country']}",
                            f"{countries[i]['todayCases']}",
                            duration=6
                        )
                        print(f"Today's cases {countries[i]['todayCases']}")
                    elif choice == 4:
                        toaster.show_toast(
                            f"Today's recovered cases in {countries[i]['country']}",
                            f"{countries[i]['todayRecovered']}",
                            duration=6
                        )
                        print(
                            f"Today's recovered cases {countries[i]['todayRecovered']}")
                    elif choice == 5:
                        toaster.show_toast(
                            f"Active cases in {countries[i]['country']}",
                            f"{countries[i]['active']}",
                            duration=6
                        )
                        print(f"Active cases {countries[i]['active']}")
                    elif choice == 6:
                        toaster.show_toast(
                            f"Total population of {countries[i]['country']}",
                            f"{countries[i]['population']}",
                            duration=6
                        )
                        print(
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


# driver function
if __name__ == "__main__":
    object = Covid()
    object.queryFunction()
