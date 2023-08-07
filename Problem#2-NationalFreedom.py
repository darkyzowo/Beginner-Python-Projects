# National economic freedom


data = {
    'Singapore': 1,
    'Ireland': 6,
    'United Kingdom': 7,
    'Germany': 27,
    'Armenia': 34,
    'United States': 17,
    'Canada': 9,
    'Italy': 74
}

country_name = input()
if data.get(country_name) is not None: # This was the issue, I was taking
    # The country name, i should;ve considered it's number ID
 print(data.get(country_name))

else: 
    print("Not Found")
