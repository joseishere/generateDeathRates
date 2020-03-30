# generateDeathRates
- python script that will open the csv file
- generate a list with all of the country names
- loop through the csv and grab specific info for each country and save to a file called "status_" + date of .csv + ".txt"
- in the same loop also calculate and save deathRate (deaths/number of cases). *I DO NOT CLAIM THIS AS TRUE DEATH RATE*
- same for recovery rate
- also generates a new csv with the simplified data called "simplified_" + date of .csv + ".csv"
- simplified csv has country, confirmed, deaths, recovered, deathRates, recoveryRates

## How to use:
1. have anaconda installed
2. get csv from [here](https://github.com/CSSEGISandData/COVID-19/tree/master/csse_covid_19_data/csse_covid_19_daily_reports)
3. put in the same directory as script
4. in terminal - "python3 [script] [csv_file]"
5. profit

![Example image](https://github.com/joseishere/generateDeathRates/blob/master/updated.png)

# UPDATE
- as COVID-19 has progressed, the csv files have changed in format
- as such script is not functioning after 03-22-20
- code is simple to read and as such easy to modify and make work, you are free to do so
- will change script when I have time to do so
