import requests

def consulta():
    response = requests.get('https://api.covid19api.com/summary')
    print(response.status_code)
    countries = response.json()["Countries"]
    for  country in countries:
        print(country["Country"] + " -  Total confirmed " + str(country["TotalConfirmed"] ))
consulta()