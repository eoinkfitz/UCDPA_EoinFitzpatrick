import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn
import seaborn as sns
from datetime import datetime
import numpy_financial as npf
#Step Number 1 - import the csv files of your data, & check for missing values

debtservicedataset = pd.read_csv('debt_service.csv')
debt = pd.read_csv('external_debt.csv')
debtusd = pd.read_csv('debtusd.csv')

missing_values_count1 = debtservicedataset.isnull().sum()
print(missing_values_count1[0:65])

missing_values_count2 = debt.isnull().sum()
print(missing_values_count2[0:65])

missing_values_count3 = debtusd.isnull().sum()
print(missing_values_count3[0:65])

#data shows us that 266 (all countries) were mising data in 1960 and none have published any data yet for 2020
#Step Number 2 - pivot the Worldbank data so it is easier to work with

debtservice= debtservicedataset.set_index(['Country Name','Country Code','Indicator Name','Indicator Code'])
debtservice.columns = debtservice.columns.str.extract('(\d+)', expand=False)
debtservice = debtservice.stack().reset_index(name='Debt Service').rename(columns={'level_4':'Year'})
print (debtservice.head(8))

totaldebt = debt.set_index(['Country Name','Country Code','Indicator Name','Indicator Code'])
totaldebt.columns = totaldebt.columns.str.extract('(\d+)', expand=False)
totaldebt= totaldebt.stack().reset_index(name='External Debt to GNI(%)').rename(columns={'level_4':'Year'})
print (totaldebt.head(8))

nominaldebt = debtusd .set_index(['Country Name','Country Code','Indicator Name','Indicator Code'])
nominaldebt .columns = nominaldebt .columns.str.extract('(\d+)', expand=False)
nominaldebt = nominaldebt .stack().reset_index(name='Debt USD').rename(columns={'level_4':'Year'})
print (nominaldebt.head(8))

#Step Number 3 - combine the Worldbank dataframes so it is easier to work with & set the countries as index

merge1 = totaldebt.merge(debtservice, on = ("Year","Country Name"), suffixes = ("_external debt","_Debt servicing"))
print(merge1.head(10))
merge1.to_csv("merge1.csv")
worldbankcombine = merge1.merge(nominaldebt, on = ("Year","Country Name"), suffixes = ("_merge1","_nominalUSD"))
worldbankcombine.to_csv("worldbankcombine.csv")
worldbank = worldbankcombine.set_index(['Country Name'])
print(worldbank)

missing_values_count4 = worldbank.isnull().sum()
print(missing_values_count4[0:12])

#error check shows that our combined file shows no missing values, we are good to proceed

#Step Number 4 - Narrow the dataset to focus on the past 20 years
worldbank["Year"] = pd.to_datetime(worldbank["Year"],format = '%Y-%m-%d')
worldbankrecent = worldbank.loc[(worldbank["Year"] >= '2005-01-01')]
worldbank.reset_index(drop=True, inplace=True)
yearindex = worldbankrecent.set_index(['Year'])
annualstats=yearindex.groupby("Year")["External Debt to GNI(%)","Debt Service","Debt USD"].mean()
print(annualstats)

fig,ax = plt.subplots()
ax.plot(annualstats.index,annualstats["External Debt to GNI(%)"],color = "red",label = "Debt to GNI(%) [L]")
plt.xticks(rotation=90, ha='right')
ax2 = ax.twinx()
ax2.plot(annualstats.index,annualstats['Debt Service'],linestyle = "--",color = "navy",label = "Debt Service Mean [R]")
ax.set_xlabel('Year')
ax.set_ylabel('Debt to GNI(%)')
ax2.set_ylabel('Debt Servicing')
ax.legend()
ax2.legend()
ax.legend(loc = 'center')
ax2.legend(loc = 'upper center')
ax.set_title("World Bank Sovereigns Recent Trend in Debt Servicing vs Debt to GNI(%)")
plt.show()

# Step Number 5 - generate statistics on recent sovereign debt & sort the statistics

stats=worldbankrecent.groupby("Country Name")["External Debt to GNI(%)","Debt Service","Debt USD"].max()
maxdebtservice = stats.sort_values(["Debt Service"],ascending=False)

print(maxdebtservice)

# Step 6 - filter for the top names,

top20 = maxdebtservice.head(20)



# Step Number 7 graph the data

fig,ax = plt.subplots()
ax.bar(top20.index,top20['Debt Service'],color = "green",label = "Top 20 World Bank Sovs by Debt Servicing Costs")
plt.xticks(rotation=90, ha='right')
plt.title("Heavily Indebted Nations in recent times")
ax.legend()
plt.show()

# 8a) - narrow to two more famous recent defaults and analyze the factors that led to the default
#create a Numpy array and list from your graph/top20 table to analyse the top5 names in more detail

top5maxdebtserv = np.array([94.367,59.6,58.4,36.09,32.95])
averagedebtservicingoftop5 = np.mean(top5maxdebtserv)
print("Of the 5 Sovereigns who had the largest debt servicing costs the average (of their max) debt servicing was",averagedebtservicingoftop5)

Top5withDebtServicingData = [['Mongolia','Liberia','Belize', 'Lebanon','Ukraine'],[94.367,59.6,58.4,36.09,32.95]]

#print each item of the top 5 using ITERROWS

Top5Dataframe = pd.DataFrame({'Country Name' : ['Mongolia','Liberia','Belize', 'Lebanon','Ukraine'],
'External Debt to GNI%' :  [284.67,497.93,107.55,148.95,128.49],
'Debt Service' : [94.367,59.6,58.4,36.09,32.95]})
print("   THE TOP5 DATAFRAME ")
print(Top5Dataframe)
print("")
for row in Top5Dataframe.iterrows():
    print("")
    print(row)

#filter to show the max debt servicing data for the two famous defaults

print("The max debt servicing since 2005 of",Top5withDebtServicingData[0][3])
print("is",Top5withDebtServicingData[1][3])

print("The max debt servicing since 2005 of",Top5withDebtServicingData[0][4])
print("is",Top5withDebtServicingData[1][4])

#8(b) analyse Lebanon
lebanon =  worldbank[worldbank["Country Code"]=="LBN"]
ukraine =  worldbank[worldbank["Country Code"]=="UKR"]

def Debt_timeseries(axes, x, y, color, xlabel, ylabel):
    axes.plot(x,y, color= color)
    axes.set_xlabel(xlabel)
    axes.set_ylabel(ylabel, color = color)
    axes.tick_params('y',colors=color)

fig,ax = plt.subplots()
Debt_timeseries(ax, lebanon['Year'],lebanon['External Debt to GNI(%)'],'blue','Year','Debt to GNI (%) Lebanon')
ax2 = ax.twinx()
Debt_timeseries(ax2, lebanon['Year'],lebanon['Debt Service'],'green','Year','Debt Service Lebanon')
ax.set_title("Lebanon Debt Servicing vs Debt to GNI(%)")
plt.show()

# use the scatterplot function to build the bubble map

import seaborn as sns
data = lebanon
sns.relplot(data=data, x="Debt Service", y="External Debt to GNI(%)", legend=False,sizes=(40, 400), alpha = .5,height = 6,size = 'Debt USD')
plt.title("Lebanon Debt Servicing vs Debt to GNI(%)")
plt.show()

#8(c) analyse Ukraine

ukraine =  worldbank[worldbank["Country Code"]=="UKR"]
fig,ax = plt.subplots()
Debt_timeseries(ax, ukraine['Year'],ukraine['External Debt to GNI(%)'],'blue','Year','Debt to GNI (%) Ukraine')
ax2 = ax.twinx()
Debt_timeseries(ax2, ukraine['Year'],ukraine['Debt Service'],'green','Year','Debt Service Ukraine')
ax.set_title("Ukraine Debt Servicing vs Debt to GNI(%)")
plt.show()

# use the scatterplot function to build the bubble map
import seaborn as sns
#create data
data2 = ukraine
sns.relplot(data=data2, x="Debt Service", y="External Debt to GNI(%)", legend=False,sizes=(40, 400), alpha = .5,height = 6,size = 'Debt USD')
plt.title("Ukraine Debt Servicing(%) vs Debt to GNI(%)")
plt.show()

#8(d) the implications of refinancing for Lebanon

lebanonindexed = lebanon.set_index(['Year'])
print(lebanonindexed)

#lebanonindexed shows us that the country's debt was 73.9BN USD in the year of default
#we need to calculate how a hypothetical restructured debt profile would look for the country
#lets use an example pricing of Ukraine who are also relatively recently out of default
#We assume Lebanon's restructuring gets them a 20% haircut, i.e. debt reduced to 80% of original level
#Ukraine priced a 8YR bond in 2021 with an interest rate of 6.875% (let's use 7% for simple example)
#we calculate the cost of refinancing the 73.9BN of principal based on the pricing (only for illustrative purpose)
#We also assume that Lebanon issues amortising debt (amortising monthly)

newissuedbond = 73.985005358*0.8
annualrate = 0.07
annual_rate_periodic = (1+annualrate)**(1/12) - 1
bond_payment_periods = 8*12
periodic_bond_payment = -1*npf.pmt(annual_rate_periodic, bond_payment_periods, newissuedbond)
initial_interest_payment = newissuedbond*annual_rate_periodic
initial_principal_payment = periodic_bond_payment - initial_interest_payment
principal_remaining = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
# Loop through each bond payment period
for i in range(0, bond_payment_periods):
    # Handle the case for the first iteration
    if i == 0:
        previous_principal_remaining = newissuedbond
    else:
        previous_principal_remaining = principal_remaining[i - 1]
    # Calculate the interest and principal payments
    interest_payment = round(previous_principal_remaining * annual_rate_periodic , 2)
    principal_payment = round(periodic_bond_payment - interest_payment, 2)
    # Catch the case where all principal is paid off in the final period
    if previous_principal_remaining - principal_payment < 0:
        principal_payment = previous_principal_remaining
    # Collect the principal remaining values in an array
    principal_remaining[i] = previous_principal_remaining - principal_payment

#We now graph the speed of amortisation (paying down the debt)

plt.plot(principal_remaining, color="m",marker = 'o', linestyle = 'dashed',markersize = 4, linewidth =0.8,label = "Outstanding Principal")
plt.title(label="Lebanon Debt Amortisation (USD BN) (based on 20% haircut at Restructuring)")
plt.xlabel('Number of Months (i.e. Monthly Repayment Schedule)')
plt.ylabel('Outstanding Principal (USD BN)')
plt.show()

#Part 9) What has been the impact of Covid-19 on National GDP Levels to our two Defaulted Sovereigns?
import requests


request=requests.get('http://api.worldbank.org/v2/country/ukr/indicators/NY.GDP.MKTP.KD.ZG?format=json')
ukrgdp = request.json()
print(request.status_code)
print(request.text)
print(ukrgdp)
request2=requests.get('http://api.worldbank.org/v2/country/lbn/indicators/NY.GDP.MKTP.KD.ZG?format=json')
lebgdp = request2.json()
print(request2.status_code)
print(request2.text)
print(lebgdp)

#10 How has Covid-19 affected Sovereign Debt levels??
#import latest Debt levels for 2020 (only Developed countries available, (i.e. World Bank goes to 2019)
#OECD file shows general government Debt to GDP up to and including 2020

oecd2020debt = pd.read_csv('ggvtdebt.csv')
print(oecd2020debt)

missing_values_count5 = oecd2020debt.isnull().sum()
print(missing_values_count5[0:8])

#error check shows that OECD file has no missing values

annualstats=oecd2020debt.groupby("TIME")["Value"].mean()
print(annualstats)

annualstats.plot(x="TIME",y="Value",kind="line", color="c",title="Trend in OECD Country General Govt Debt to GDP(%)",rot=90)
plt.xlabel('Year')
plt.ylabel('Average Gen Govt Debt to GDP (%) OECD Countries')
plt.show()














