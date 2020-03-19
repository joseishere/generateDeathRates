# generateDeathRates
- python script that will open the csv file
- generate a list with all of the country names
- loop through the csv and grab specific info for each country and save to a file called "status_" + date of .csv + ".txt"
- in the same loop also calculate and save deathRate (deaths/number of cases). *I DO NOT CLAIM THIS AS TRUE DEATH RATE*
- in the csv files, "occupied Palestinian territory" gives nan so I chose to get rid of it. so pop both lists.
- once we pop both lists, save the lists into two columns in a new csv called "deathRates_" + date of .csv + ".csv"

## How to use:
1. have anaconda installed
2. get csv from [here](https://github.com/CSSEGISandData/COVID-19/tree/master/csse_covid_19_data/csse_covid_19_daily_reports)
3. put in the same directory as script
4. in terminal - "python3 [script] [csv_file]"
5. profit

![Example image](https://github.com/joseishere/generateDeathRates/blob/master/updated.png)
