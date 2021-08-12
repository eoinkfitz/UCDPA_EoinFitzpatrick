import pandas as pd
import matplotlib.pyplot as plt

from datetime import datetime

olympics = pd.read_csv('C:\\Users\\LydonLaptop\\PycharmProjects\\pythonProject\\Olympic_Medals_Table.csv')

print(olympics.head(10))

#Class 1 Transforming DataFrames & class # 2 New columns

#ranking the medals table
olympics_ranked = olympics.sort_values(["Gold","Silver","Bronze"],ascending=[False,False,False])

print(olympics_ranked)

#filter for USA only

usaonly = olympics_ranked[olympics_ranked["Country"]=="USA"]

print(usaonly)

#filter for Golds above ten

goldsmorethan10 = olympics_ranked[olympics_ranked["Gold"]>10]

print(goldsmorethan10)

#tells me only 5 teams got more than 10 gold medals

#adding a new column

olympics_ranked["gold_weighting"] = olympics_ranked["Gold"]*3
olympics_ranked["silver_weighting"] = olympics_ranked["Silver"]*2
olympics_ranked["bronze_weighting"] = olympics_ranked["Bronze"]*1

olympics_ranked["total_weighting"] = olympics_ranked["gold_weighting"] + olympics_ranked["silver_weighting"]  + olympics_ranked["bronze_weighting"]

olympics_ranked["totalmedals"] = olympics_ranked["Gold"] + olympics_ranked["Silver"] + olympics_ranked["Bronze"]

print(olympics_ranked)

# now rank by the total weighting

finalranking = olympics_ranked.sort_values(["total_weighting"],ascending=False)

print(finalranking)

# class 3 - Summary statistics

meangoldmedals = finalranking["Gold"].mean()

print(meangoldmedals)

#tells me the average gold medals is 13 medals

mediansilver = finalranking["Silver"].median()

print(mediansilver)

#tells me median silver is 16.5 medals

maxbronze = finalranking["Bronze"].max()

print(maxbronze)

#tells me max bronze is 47 medals

#percentiles

def pct10(column):
    return column.quantile (0.1)

def pct50(column):
    return column.quantile (0.5)

percentiles = finalranking["Gold"].agg([pct10,pct50])

print(percentiles)

#how many golds across the ten countries

totalgolds = finalranking["Gold"].cumsum()

print(totalgolds)

#tells me there have been 130 gold medals won across the countries

finalranking["totalgolds"] = finalranking["Gold"].cumsum()

print(finalranking)

#added a cumulative column to my medals table

#Class 4 - Duplicates & counting

olympics_historical = pd.read_csv('C:\\Users\\LydonLaptop\\PycharmProjects\\pythonProject\\Olympic_Medals_Table_Historical.csv')

finalrankinghistorical= pd.DataFrame(olympics_historical.head(30))

print(finalrankinghistorical)

cleanedrank = finalrankinghistorical.drop_duplicates(subset=["Country"])

print (cleanedrank)

#has cleaned by ranking to have only 1 country

proportions = finalrankinghistorical["Country"].value_counts(normalize=True)

print(proportions)

#tells me also there is 10% of each country

#Class 5 - Grouped Summary Statistics

everymedalmean = finalrankinghistorical.groupby(["Country"])[["Gold","Silver","Bronze"]].mean()

#group summary stat. tells me each country's avg gold medals in last 3 Olympic Games

print (everymedalmean)

#Class 6 Pivot Tables

historicalpivot = olympics_historical.pivot_table(values="Gold",index ="Year")

print(historicalpivot)

#pivots automatically give an mean. this shows the mean of golds won by these countries in each year

#building on the pivot table to multiple values & indices

historicalpivotexpanded = olympics_historical.pivot_table(values="Gold",index ="Country",columns="Year",fill_value=0,margins=True)

print(historicalpivotexpanded)

#gives us a lovely summary view of the medals table. Pivot on two variables. margins=True gives you a mean column

finalrankinghistorical2012 = finalrankinghistorical[finalrankinghistorical["Year"]==2012]
finalrankinghistorical2016 = finalrankinghistorical[finalrankinghistorical["Year"]==2016]
finalrankinghistorical2020 = finalrankinghistorical[finalrankinghistorical["Year"]==2020]

print(finalrankinghistorical2012)
print(finalrankinghistorical2016)
print(finalrankinghistorical2020)

finalrankinghistorical2020sorted = finalrankinghistorical2020.sort_values(["Gold"],ascending=[False])

graph2020=finalrankinghistorical2020sorted.plot(x="Country",y="Gold",kind="bar",color="purple",title="2020 Gold Medals")
plt.show()

#Class 7 Indices etc

finalrankinghistorical_ind = finalrankinghistorical.set_index("Country")

spainfrancefilter = finalrankinghistorical_ind.loc[[("Spain"),("France")]]

#I set countries to be the index and then can filter for spain and france in the Index Loc

print(spainfrancefilter)

#multi-level indices - Hierarchical Indexes
#indices can be useful, and make it easier to play with the data

finalrankinghistorical_ind2 = finalrankinghistorical.set_index(["Country","Year"]).sort_index()

print(finalrankinghistorical_ind2)

spainfrancefilter2012 = finalrankinghistorical_ind2.loc[[("Spain",2012),("France",2012)]]

print(spainfrancefilter2012)

#Class 8 Slicing & Subsetting Data

slicedChinaFrance = finalrankinghistorical_ind2.loc[("China",2012):("France",2020)]

#printsall the entries for and including China to France
print(slicedChinaFrance)

#slicing columns

ChinatoFranceSilverBronze= finalrankinghistorical_ind2.loc[("China",2012):("France",2020),"Silver":"Bronze"]

print (ChinatoFranceSilverBronze)

#using iloc

print(finalrankinghistorical_ind2.iloc[0:31,0:4])


#Class 10 Visualizing your data

finalrankinghistorical2020 = finalrankinghistorical[finalrankinghistorical["Year"]==2020]

print(finalrankinghistorical2020)

sort2020 = finalrankinghistorical2020.sort_values(["Gold"],ascending=False)
sort2012 = finalrankinghistorical2012.sort_values(["Gold"],ascending=False)
sort2016 = finalrankinghistorical2016.sort_values(["Gold"],ascending=False)
print(sort2020)
print(sort2012)
print(sort2016)

sort2020.plot(x="Country",y="Gold",kind="bar",color="green",title="2020 Gold Medals")
sort2020.plot(x="Country",y="Gold",kind="scatter",color="cyan",title="2020 Gold Medals")

plt.show()
plt.show()

del sort2020["Year"]
sort2020.plot(x='Country',kind="bar",title="Medals per Country 2020")
plt.show()

sort2020.plot(x='Country',kind="line",title="Medals per Country 2020")
plt.show()



#Class 11 - Dealing with missing Values

olympics_historical_new = pd.read_csv('C:\\Users\\LydonLaptop\\PycharmProjects\\pythonProject\\Olympic_Medals_Table_Historical_New.csv')

print(olympics_historical_new)

print(olympics_historical_new.isna().any())

#tells me there is an NA in gold silver and Bronze

print(olympics_historical_new.isna().sum())

#tells me 5 missing values, 2 gold, 2 silver, 1 bronze

olympicscleaned = olympics_historical_new.fillna(0)

#fills in the missing values

print(olympicscleaned.isna().sum())

#the cleaned dataset has no #nas

#class 13 and 14 writing and editing CSV data

olympicscleaned = olympics_historical_new.fillna(0)

olympicscleaned["total medals"] = olympicscleaned["Gold"]+ olympicscleaned["Silver"]+ olympicscleaned["Bronze"]

print(olympicscleaned)

#we have now added a column and cleaned the dataset
#we will now save the dataset as a new file

olympicscleaned.to_csv("olympicscleaned.csv")

data=pd.read_csv("netflix_titles.csv")

print(data.head())































































