import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file.
dalys_data = pd.read_csv('/Users/Zhihan/Library/CloudStorage/OneDrive-InternationalCampus,ZhejiangUniversity/26-26_Study/IBI/IBI1_2025-26/Practical10/dalys-rate-from-all-causes.csv')

# Show 3rd and 4th columns (Year and DALYs) for the first 10 rows.
first_10_year_dalys = dalys_data.iloc[:10, 2:4]
print("First 10 rows (Year, DALYs):")
print(first_10_year_dalys)
# Across Afghanistan's first 10 recorded DALY years, the maximum DALYs occurs in 1998.

# Use a Boolean filter to show all years recorded for Zimbabwe.
zimbabwe_years = dalys_data.loc[dalys_data["Entity"] == "Zimbabwe", "Year"]
print("\nAll years recorded for Zimbabwe:")
print(zimbabwe_years.to_list())
# Zimbabwe data are recorded from 1990 (first year) to 2019 (last year).

# Find countries with maximum and minimum DALYs in 2019.
data_2019 = dalys_data.loc[dalys_data["Year"] == 2019, ["Entity", "DALYs"]]
max_country = data_2019.loc[data_2019["DALYs"].idxmax(), "Entity"]
min_country = data_2019.loc[data_2019["DALYs"].idxmin(), "Entity"]

print("\nCountry with maximum DALYs in 2019:", max_country)
print("Country with minimum DALYs in 2019:", min_country)
# In 2019, maximum DALYs: Lesotho; minimum DALYs: Singapore.

# Plot DALYs over time for one of those countries (Lesotho).
lesotho_data = dalys_data.loc[dalys_data["Entity"] == max_country, ["Year", "DALYs"]]
plt.figure(figsize=(10, 5))
plt.plot(lesotho_data["Year"], lesotho_data["DALYs"], marker="o", color="tab:blue")
plt.xlabel("Year")
plt.ylabel("DALYs")
plt.title(f"DALYs Over Time in {max_country}")
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()

# Question from question.txt:
# "Which country had the largest decrease in DALYs rate from 1990 to 2019?"
subset = dalys_data.loc[dalys_data["Year"].isin([1990, 2019]), ["Entity", "Year", "DALYs"]]
pivot = subset.pivot(index="Entity", columns="Year", values="DALYs").dropna()
pivot["change_2019_minus_1990"] = pivot[2019] - pivot[1990]
largest_decrease_country = pivot["change_2019_minus_1990"].idxmin()
largest_decrease_value = pivot.loc[largest_decrease_country, "change_2019_minus_1990"]

print("\nAnswer to question.txt:")
print(
	f"Country with largest decrease from 1990 to 2019: {largest_decrease_country} "
	f"({largest_decrease_value:.2f})"
)