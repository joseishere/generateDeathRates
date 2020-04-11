import sys
import pandas as pd
import csv

def simplify(csvFile):

	fileName = "status_" + csvFile[:-9] + ".txt"
	file = open(fileName, "w")

	file.write("Simplifying data from: " + csvFile + "\n")
	df = pd.read_csv(csvFile)

	# after reading csv get list of countries
	list_of_countries = df['Country_Region'].unique()

	# simplify the original csv, pull important data from it
	# each list will be a column in our new csv
	confirmed = ['confirmed']
	deaths = ['deaths']
	recovered = ['recovered']

	deathRates = ['deathRates']
	recoveryRates = ['recoveryRates']


	for x in list_of_countries:

			confirmed.append(df.loc[df['Country_Region'] == x, 'Confirmed'].sum())
			deaths.append(df.loc[df['Country_Region'] == x, 'Deaths'].sum())
			recovered.append(df.loc[df['Country_Region'] == x, 'Recovered'].sum())

			deathRates.append(df.loc[df['Country_Region'] == x, 'Deaths'].sum() / df.loc[df['Country_Region'] == x, 'Confirmed'].sum())
			recoveryRates.append(df.loc[df['Country_Region'] == x, 'Recovered'].sum() / df.loc[df['Country_Region'] == x, 'Confirmed'].sum())

			file.write(x + "\n")
			file.write("\tConfirmed: " + str(df.loc[df['Country_Region'] == x, 'Confirmed'].sum()) + "\n")
			file.write("\tDeaths: " + str(df.loc[df['Country_Region'] == x, 'Deaths'].sum()) + "\n")
			file.write("\tRecovered: " + str(df.loc[df['Country_Region'] == x, 'Recovered'].sum()))
			file.write("" + "\n")
			file.write("\tDeath Rate: " + str( (df.loc[df['Country_Region'] == x, 'Deaths'].sum() / df.loc[df['Country_Region'] == x, 'Confirmed'].sum()) * 100) + "\n")
			file.write("\tRecovery Rate: " + str( (df.loc[df['Country_Region'] == x, 'Recovered'].sum() / df.loc[df['Country_Region'] == x, 'Confirmed'].sum()) * 100) + "\n")

	file.close()

	countries = list_of_countries.tolist()
	# for csv files after 03/17/20, no need to pop list anymore
	# countries.pop()
	# deathRates.pop()

	countries.insert(0, "country")

	name = "simplified_" + csvFile[:-9] + ".csv"
	with open(name, "w") as f:
		writer = csv.writer(f)
		writer.writerows(zip(countries, confirmed, deaths, recovered, deathRates, recoveryRates))


simplify(sys.argv[1])

