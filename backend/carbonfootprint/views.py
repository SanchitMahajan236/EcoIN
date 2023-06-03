from django.shortcuts import render, HttpResponse
from backend.settings import GPT_KEY
import requests
# Create your views here.
def Home(request):
    return render(request,'carbonfootprint/perspective.html')

def IndividualCalculator(request):
    if request.method == "POST":
        print(request.POST.items())
        emission = 0
        current = float(request.POST['electricity'])   # In units = KWH
        gas = float(request.POST['gas'])   # In grams
        vehicle = request.POST['vehicle']   # Car , Bus
        milage = float(request.POST['mileage'])
        distance =float( request.POST['distance'])
        emissions_factor = 0

        if (vehicle == "Car"):
            car_fuel = request.POST['fuel']     # Data is shared in the group
            if car_fuel == 'gasoline':
                emissions_factor = 2.31  # in kg CO2 per liter
            elif car_fuel == 'diesel':
                emissions_factor = 2.68  # in kg CO2 per liter
        elif (vehicle == "Bus"):
            car_fuel = request.POST['fuel']     # Data is shared in the group
            emissions_factor = 0.68  # in kg CO2 per km

        # Fuel

        if vehicle == 'car':
            emission = (distance / milage) * emissions_factor
        elif vehicle == 'bus':
            emission = distance * emissions_factor
        # Electricity
        emissions_factor = 0.93
        emission = emission + current*emissions_factor
        
        #LPG
        emissions_factor = 2.983
        emission = emission + emissions_factor*gas

        # GPT WORK
        prompt = "Emission :" + str(emission) + ". Suggest ways to reduce it"
        target_url = "https://api.openai.com/v1/completions"
        header = {
        "Authorization" : "Bearer " + GPT_KEY 
        # For Organizations
        # "<Organization_name>" : "<KEY>"
        }

        # To get the available models list.
        # response = requests.request(method="POST",url=target_url,headers=header)

        header["Content-Type"] = "application/json"

        body = {
        "model": "gpt-3.5-turbo",
        "messages": [{"role": "user", "content": "Hello!"}]
        }

    
        response = requests.request(method="POST",url=target_url,headers=header,data = body)
        result = response.json()

        print("==============================")
        print(f"The output is:\n{result}")


        context = {
            "electricity": current,
            "gas":gas,
            "ac":float(request.POST['ac']),
            "vehicle":vehicle,
            "mileage":milage,
            "distance":distance,
            "prompt":True
        }
        context['emission'] = round(emission,3)
        return render(request,"carbonfootprint/individual.html", context = context)
    context = {
            "electricity": 0,
            "gas":0 ,
            "ac":0,
            "vehicle":"petrol",
            "mileage":0,
            "distance":0
    }
    return render(request,"carbonfootprint/individual.html",context=context)

def BusinessCalculator(request):
    return render(request,"carbonfootprint/business.html")