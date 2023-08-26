# Pandas Tutorial, using my Oura Data

import pandas as pd
import matplotlib.pyplot as plt

# Reads in CSV data file into a Pandas dataframe
oura_data = pd.read_csv("/home/seany42/Documents/PandOura/SM Oura Data 0920 to 0123.csv", index_col=0)
oura_data.name = "The Original Dataset"


#build a table of basic info about 3 of the columns
analysis_table = oura_data.agg(
    {
        'Sleep Score': ['min', 'max', 'mean', 'median', 'std'],
        'Readiness Score': ['min', 'max', 'mean', 'median', 'std'],
        'Average HRV': ['min', 'max', 'mean', 'median', 'std'],
    }
)

print("How do I read and write data in Pandas\n")
print(oura_data["Sleep Score"])
print(f"\nMy best sleep score is {oura_data['Sleep Score'].max()}.")
print(f"\nA summary of my Oura Data is;\n {oura_data.describe()}")
print(f"\nA summary of my Average HRV is;\n {oura_data['Average HRV'].describe()}")
print(f"\nThe first 10 lines of my dataset are;\n{oura_data.head(10)}")
print(f"\nThe data tpyes in my dataset are;\n{oura_data.dtypes}")

#oura_data.to_excel("/home/seany42/Documents/PandOura/Seans_Oura_Data.xlsx", sheet_name="The First Years", index=False)
print("\nYour file is now available in Excel format....you're welcome!\n")

print(oura_data.info())


print("\n\nHow do I select a subset of a dataframe?\n")
steps_taken = oura_data["Steps"] # 1 column
print(steps_taken.head())
print(steps_taken.shape)

steps_readiness = oura_data[['Steps', "Readiness Score"]] # 2 columns
print(f"The shape of my 2D subset is {steps_readiness.shape}")

low_step_days = oura_data[oura_data["Steps"] < 3000]
print(low_step_days)
print(f"You had {low_step_days.shape} low step days.")

lazy_days = oura_data[oura_data["Long Periods of Inactivity"].isin([4,5])]
print(f"\nThese were the data from days where I was sedentary;\n {lazy_days}")



print("\n\nNow let's create some plots from Panadas!")
#oura_data["Sleep Score"].plot()
#oura_data.plot.line('Readiness Score')

plot_data = oura_data[['Sleep Score', 'Lowest Resting Heart Rate', 'Readiness Score']]
plot_data.plot.area(figsize=(12, 4), subplots=True)

plt.show()

oura_data["Readiness Recovery Ratio"] = oura_data["Readiness Score"] / oura_data["Recovery Index Score"]
print(f"\nThe first 10 lines of my dataset (with an added calculated column are;\n{oura_data.head(10)}")


print("\nI've renamed the first column from sleep score to sleepy time")
oura_data_renamed = oura_data.rename(columns={"Sleep Score": "Sleepy Time"})
oura_data_renamed.name = "Its a Copy"
print("\nNote that this done on a new copy of the dataset.")
print(oura_data_renamed.name)
print(oura_data_renamed.head(5))

print("\nThis is the orginal of the dataset.")
print(oura_data.name)
print(oura_data.head(5))


print("\nWe are going to do some basic summary stats now.\n")
print(f"My average Sleep Score is {oura_data['Sleep Score'].mean():.2f}")
print(f"\nThe medians of Sleep and Sleep Effeciency are :\n{oura_data[['Sleep Score', 'Sleep Efficiency']].median()}")
analysis_table = oura_data.agg(
    {
        'Sleep Score': ['min', 'max', 'mean', 'median', 'std'],
        'Readiness Score': ['min', 'max', 'mean', 'median', 'std'],
        'Average HRV': ['min', 'max', 'mean', 'median', 'std'],
    }
)
print(analysis_table)
print(f"\nThe average readiness score, grouped by periods of inactivity, are:\n{oura_data[['Long Periods of Inactivity', 'Readiness Score']].groupby('Long Periods of Inactivity').mean()}\n.")
print(f"\nThis the the same but for all number based columns:\n{oura_data.groupby('Long Periods of Inactivity').mean(numeric_only=True)}")
print(f"\nThe frequencies of {oura_data.groupby('Long Periods of Inactivity')['Long Periods of Inactivity'].count()}")


print(f"This is how we sort the data by Sleep Score:\n{oura_data.sort_values(by='Sleep Score', ascending=False).head(10)}")
print(f"This is how we sort the data by Sleep then Readiness Scores:\n{oura_data.sort_values(by=['Sleep Score', 'Readiness Score'], ascending=False).head(10)}")


print(f"This is a pivot table:\n{oura_data.pivot_table(index='Long Periods of Inactivity', aggfunc='mean', margins=True,)}.")
print(f"The unique items in the Steps field are:\n{oura_data.Steps.unique()}") #requires the field looked at not to have any spaces


