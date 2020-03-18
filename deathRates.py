import sys
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style="darkgrid")
import csv

def genDeathRates(csvFile):

	fileName = "status_" + csvFile[:-9] + ".txt"
	file = open(fileName, "w")

	file.write("Generating Death Rates from: " + csvFile + "\n")
	df = pd.read_csv(csvFile)

	# after reading csv get list of countries
	list_of_countries = df['Country/Region'].unique()

	# get deathRates and show useful info

	deathRates = []

	for x in list_of_countries:
    		
    		deathRates.append(df.loc[df['Country/Region'] == x, 'Deaths'].sum() / df.loc[df['Country/Region'] == x, 'Confirmed'].sum())
    		file.write(x + "\n")
    		file.write("\tConfirmed: " + str(df.loc[df['Country/Region'] == x, 'Confirmed'].sum()) + "\n")
    		file.write("\tDeaths: " + str(df.loc[df['Country/Region'] == x, 'Deaths'].sum()) + "\n")
    		file.write("\tRecovered: " + str(df.loc[df['Country/Region'] == x, 'Recovered'].sum()))
    		file.write("" + "\n")
    		file.write("\tDeath Rate: " + str( (df.loc[df['Country/Region'] == x, 'Deaths'].sum() / df.loc[df['Country/Region'] == x, 'Confirmed'].sum()) * 100) + "\n")
    		file.write("\tRecovery Rate: " + str( (df.loc[df['Country/Region'] == x, 'Recovered'].sum() / df.loc[df['Country/Region'] == x, 'Confirmed'].sum()) * 100) + "\n")

	file.close()

	countries = list_of_countries.tolist()
	countries.pop()
	deathRates.pop()

	name = "deathRates_" + csvFile[:-9] + ".csv"
	with open(name, "w") as f:
		writer = csv.writer(f)
		writer.writerows(zip(countries, deathRates))



genDeathRates(sys.argv[1])

