import matplotlib.pyplot as plt
UK = {"2020":66.7,"2024":69.2}
China = {"2020":1426,"2024":1410}
Italy = {"2020":59.4,"2024":58.9}
Brazil = {"2020":208.6,"2024":212.0}
USA = {"2020":331.6,"2024":340.1}

def growth_rate(country):
    percentage_growth = ((country["2024"] - country["2020"]) / country["2020"]) * 100
    return percentage_growth

countries = ["UK", "China", "Italy", "Brazil", "USA"]
country_dicts = [UK, China, Italy, Brazil, USA]
country_growth = [(country, growth_rate(data)) for country, data in zip(countries, country_dicts)]
country_growth.sort(key=lambda x: x[1], reverse=True)
for country, rate in country_growth:
    print(country)
for country in countries:
    if country == "UK":
        print(f"Population growth rate for {country}: {growth_rate(UK):.2f}%")
    elif country == "China":
        print(f"Population growth rate for {country}: {growth_rate(China):.2f}%")
    elif country == "Italy":
        print(f"Population growth rate for {country}: {growth_rate(Italy):.2f}%")
    elif country == "Brazil":
        print(f"Population growth rate for {country}: {growth_rate(Brazil):.2f}%")
    elif country == "USA":
        print(f"Population growth rate for {country}: {growth_rate(USA):.2f}%")

plt.bar(countries, [growth_rate(UK), growth_rate(China), growth_rate(Italy), growth_rate(Brazil), growth_rate(USA)], color=['blue', 'red', 'green', 'orange', 'purple'])
plt.xlabel('Countries')
plt.ylabel('Population Growth Rate (%)')
plt.title('Population Growth Rate from 2020 to 2024')
plt.ylim(-5, 5)
plt.axhline(0, color='black', linewidth=0.5)
plt.show() 
