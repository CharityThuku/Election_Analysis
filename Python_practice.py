counties = ["Arapahoe", "Denver","Jefferson"]
if counties[1] == "Denver" :
    print(counties[1])

if "El Paso" in counties:
    print("El Paso is in counties.")
else:
    print("El Paso is not in counties")
if "Arapahoe" in counties and "El Paso" in counties:
    print("Arapahoe and El Paso are in the list of counties.")
else:
    print("Arapahoe and El Paso are not in the list of counties")

for county in counties:
    print(county)

counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

for county in counties_dict:
    print(county)
for county in counties_dict.keys():
    print(county)
for voters in counties_dict.values():
    print(voters)
for county,voters in counties_dict.items():
    print(county,voters)

i = county
j = voters
for i,j in counties_dict.items():
    print(str(i) + " county has " + str(j) + " registered voters")

voting_data = [{"county":"Arapahoe" , "registered_voters": 422829},
{"county":"Denver" , "registered_voters": 463353},
{"county":"Jefferson" , "registered voters": 432435}]

for county_dict in voting_data:
    print(county_dict)
for county_dict in voting_data:
    for value in county_dict.values():
        print(value) 
for county, voters in counties_dict.items():
    print(county + " county has" + str(voters) + " registered voters")
for county, voters in counties_dict.items():
    print(f"{county} county has {voters} registered voters.")

for county, voters in counties_dict.items():
    print(f"{county} county has {voters:,.2f} registered voters.")
for county_dict in voting_data:
    for county, voters in county_dict.items():
        print(f"{county} county has {voters:,.2f} registered voters.")