autoPlius = {
    "Volkswagen Golf": {
        "description": "A common hatchback.",
        "specs": ["1.5L", "150hp"],
        "mileage": "450.812 KM",
        "inspection": {
            "active": True,
            "exp-date": "2027-08-15"
        }
    },
    "BMW 3 Series": {
        "description": "A popular luxury sedan.",
        "specs": ["2.0L", "255hp"],
        "mileage": "120.500 KM",
        "inspection": {
            "active": True,
            "exp-date": "2026-11-20"
        }
    },
    "Renault Clio": {
        "description": "A small city car.",
        "specs": ["1.0L", "90hp"],
        "mileage": "85.200 KM",
        "inspection": {
            "active": True,
            "exp-date": "2027-03-10"
        }
    },
    "Volvo XC60": {
        "description": "A family SUV.",
        "specs": ["2.0L", "247hp"],
        "mileage": "165.000 KM",
        "inspection": {
            "active": False,
            "exp-date": "2025-09-01"
        }
    },
    "Fiat 500": {
        "description": "A tiny car.",
        "specs": ["1.0L", "70hp"],
        "mileage": "62.400 KM",
        "inspection": {
            "active": True,
            "exp-date": "2026-12-05"
        }
    },
    "Škoda Octavia": {
        "description": "A roomy everyday car.",
        "specs": ["1.5L", "150hp"],
        "mileage": "210.350 KM",
        "inspection": {
            "active": True,
            "exp-date": "2027-01-18"
        }
    }
}


tech = "galiojančia"



print("Sveiki atvykę į AUTO PLIUS puslapį!")
print("-----------------------------------")
print("Pasirinkite veiksmą")
print("1. Peržiūrėti dabartinius skelbimus")
print("2. Parduoti mašiną")
print("3. Panaikinti skelbimą")
print("4. Išeiti iš programos")

pasirinkimas = int(input("Savo pasirinkimą rašykite čia: "))

if pasirinkimas == 1:
    print("Štai visi įkelti mašinų skelbimai:", list(autoPlius.keys()))
    pasirinktaMasina = input("Kokį mašinos skelbimą norėtumėte peržiūrėti? (Įveskite pavadinimą): ")

    if autoPlius.get(pasirinktaMasina).get("inspection").get("active") == True:
        tech = "galiojančia"
    else:
        tech = "negaliojančia"

    print(f"Jūsų pasirinktos mašinos aprašymas: {autoPlius.get(pasirinktaMasina).get('description')} su {autoPlius.get(pasirinktaMasina).get('specs')} varikliu, rida {autoPlius.get(pasirinktaMasina).get('mileage')} ir {tech} tech apžiūra")  

elif pasirinkimas == 2:
    MasinaPardavimui = input("Mašinos pavadinimas ")
    Aprasymas = input("Aprašykite parduodamą mašiną ")
    Charakteristikos = input("Kokios charakteristikos ")
    Rida = input("Kokia rida ")  
    TechGalioja = input("Ar techninė apžiūra galioja ")
    TechData = input("Kada baigia galioti tech apžiūra ")  

    autoPlius.update({
            MasinaPardavimui: {
                "description": Aprasymas,
                "specs": [Charakteristikos],
                "mileage": Rida,
                "inspection": {
                    "active": TechGalioja,
                    "exp-date": TechData
                }
            }
        })
    print("Sėkmingai pridėjote naują skelbimą!")

elif pasirinkimas == 3:
    print("Štai dabartiniai skelbimai:", list(autoPlius.keys()))
    MasinaPanaikinimui = input("Kokį skelbimą norite pašalinti?: ")
    autoPlius.pop(MasinaPanaikinimui)
