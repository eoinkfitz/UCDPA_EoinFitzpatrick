import pandas as pd
import matplotlib.pyplot as plt

from datetime import datetime

#classes 1 & 2 working with datetimes date strings etc

black_monday=datetime(1987,10,19)
print(black_monday)

mybirthday= datetime(1988,9,14)
mybdaystring= mybirthday.strftime("%a,%b,%d,%y")
print(mybdaystring)

Emerbirthday= datetime(1986,12,8)
Emerbdaystring= Emerbirthday.strftime("%a,%b,%d,%y")
print(Emerbdaystring)

agegap= mybirthday - Emerbirthday
print(agegap)

print(datetime.now())

ronanbday = datetime (2021,2,6)
ronandueday = datetime (2021,2,22)

from datetime import timedelta

offset = timedelta(days=16)

differencevsduedate= ronandueday- offset
print(differencevsduedate)

if differencevsduedate== ronanbday:
    print(True)


#Classes 3 -5 Dictionaries, Boolean Operators etc.

goalscorers = {'Rashford':17, 'Greenwood':17, 'Fernandes':24}
print(goalscorers)

if goalscorers['Rashford'] == 17:
        print(goalscorers['Rashford'])

if goalscorers['Rashford'] > goalscorers['Greenwood']:
        print("Rashford scored more goals than Greenwood")
elif goalscorers['Rashford'] < goalscorers['Greenwood']:
        print("Rashford scored less goals than Greenwood")
else:
     print("Rashford & Greenwood scored same number of goals")


#Class 7  For and While Loops

leagueswon = {'ManUtd':20, 'Lpool':20, 'Chelsea':7, 'Leeds':7, 'Everton':5, 'Arsenal':3}

for k in leagueswon:
    print(leagueswon[k])

cupswon = 0
while cupswon< 7:
        cupswon = (cupswon+1)
        if cupswon ==5:
            break
print('cups won are max five')

leagueswon = 0
while leagueswon> 5:
        print(leagueswon)
        if l <5:
            break
print('these teams are the only ones to win more than 5 leagues')



#Class 8 - 9 The DataFrame & Accessing Data

import matplotlib.pyplot as plt

worldcupwins = (1,2,4,4,5)
country = ('England','France','Germany', 'Italy', 'Brazil')
plt.scatter(x=country,y=worldcupwins,color='green',linestyle= '--')
plt.xlabel('Country')
plt.ylabel('World Cup Wins')
plt.title("World Cup Wins by Country")
plt.show()

wcwinstable = [['England',1],['France',2],['Brazil',4],['Germany',4]]
wcwinstabledf= pd.DataFrame(wcwinstable,columns=['Country','World Cup Wins'])

print(wcwinstabledf)

print(wcwinstabledf[0:2])
print(wcwinstabledf[1:3])

print(wcwinstabledf)

print(wcwinstabledf.iloc[[1,2],1:2])

#altering the data in the dataframe = makes England & France 5 time winners

wcwinstabledf.iloc[:2,1:] = 5

print(wcwinstabledf)

#altering the data in the dataframe = makes Brazil 7 time winners

wcwinstabledf.iloc[2,1] = 7

print(wcwinstabledf)




#Class 10-13 Aggregating & Summarising Data

print(wcwinstabledf.count())

print(wcwinstabledf.mean())


leaguetable = [['Utd',100,50],['Spurs',80,40],['Leeds',75,30],['Arsenal',74,22],['Chelsea',71,21],['Lpool',64,18],['Fulham',62,12]]
leaguetabledf= pd.DataFrame(leaguetable,columns=['Team','Points','Goals Scored'])

print(leaguetabledf)

#prints the top 4 teams
print(leaguetabledf.head(4))

#prints the bottom 3 teams
print(leaguetabledf.tail(3))

print(leaguetabledf.describe())

print(leaguetabledf.describe(include='all'))

print(leaguetabledf.describe(percentiles=[.1,.5,.8,.9]))

print(leaguetabledf.Points>85)
#shows that only the first team managed to get points above 85 in the season

print(leaguetabledf.Team=='Lpool')
#shows that only the fifth placed team is liverpool



topscorers = [['Fernandes','Utd',30,15],['Kane','Spurs',20,20],['Diaz','Leeds',15,10],['Cavani','Utd',24,12]]
topscorersdf= pd.DataFrame(topscorers,columns=['Player','Team','Points','Assists'])

print(topscorersdf)

mask_united = topscorersdf.Team == 'Utd'

utddf = topscorersdf.loc[mask_united]

print(utddf)

print(utddf.describe)
#gives you the info you need just for utd goalscorers
print(topscorersdf.describe)
#gives info you need for all the top goal scorers


# class 14 - plotting the data

#bring back in the topscorers table so we can see it easily again

topscorers = [['Fernandes','Utd',30,15],['Kane','Spurs',20,20],['Diaz','Leeds',15,10],['Cavani','Utd',24,12]]
topscorersdf= pd.DataFrame(topscorers,columns=['Player','Team','Goals scored','Assists'])

topscorersdf.plot(x='Player', y = 'Goals scored', kind='bar',title='Top Goal Scorers in season')


plt.show()

topscorersdf.plot(x='Player', y = 'Assists', kind='bar',title='Top Assists in season')

plt.show()


# finally last thing is importing a csv

import pandas as pd

googlecsv = pd.read_csv('C:\\Users\\LydonLaptop\\PycharmProjects\\pythonProject\\Google.csv')

print(googlecsv)

print(googlecsv.head(5))
print(googlecsv.tail(3))

olympicmedals = pd.read_csv('C:\\Users\\LydonLaptop\\PycharmProjects\\pythonProject\\Google2.csv')

print(olympicmedals)

#prints the most six recent day's medals in the olympics
print(olympicmedals.head(6))

#prints the last 2 rows in the dataset
print(olympicmedals.tail(2))


dfmedals=pd.DataFrame(olympicmedals.head(6))
#creates dfmedals as a dataframe, i.e. a table of the past six days

print(dfmedals)

#plots the medals by country of the last six days
dfmedals.plot(x='Date',kind="barh",title="Gold Medals Per Day")
plt.show()





