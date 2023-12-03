import matplotlib.pyplot as plt
import numpy as np

# Sample data: Year vs Internet Penetration Rate for different continents
years = np.array([2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022])
asia_rates = np.array([35, 38, 42, 45, 49, 53, 56, 60, 63, 65])
africa_rates = np.array([16, 18, 21, 25, 28, 31, 35, 38, 42, 45])
europe_rates = np.array([74, 75, 76, 78, 79, 81, 83, 85, 86, 87])
america_rates = np.array([61, 62, 64, 66, 68, 69, 71, 72, 74, 75])

plt.figure(figsize=(10,6))
plt.plot(years, asia_rates, label='Asia', color='blue')
plt.plot(years, africa_rates, label='Africa', color='green')
plt.plot(years, europe_rates, label='Europe', color='red')
plt.plot(years, america_rates, label='America', color='purple')

plt.title("Global Internet Penetration Rates Over the Last Decade")
plt.xlabel("Year")
plt.ylabel("Internet Penetration Rate (%)")
plt.legend()
plt.grid(True)
plt.tight_layout()

plt.savefig("internet_penetration.png") # Save the figure
plt.show()
