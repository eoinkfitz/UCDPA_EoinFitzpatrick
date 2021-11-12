#import the packages you need

import matplotlib.pyplot as plt
import pandas as pd

#Number 1 ---->  simple graph examples

fig,ax=plt.subplots()

x = [1,2,3,4,5]
y = [2,4,1,7,8]
y1 = [8,8,7,4,3]
y2 = [4,5,6,8,14]
y3 = [4,2,1,11,1]

ax.plot(x)
plt.show()
ax.bar(y1,y2)
plt.show()

#"Number 2 ----> Scatter Chart example

worldcupwins = (1,2,4,4,5)
country = ('England','France','Germany', 'Italy', 'Brazil')
plt.scatter(x=country,y=worldcupwins,color='green',linestyle= '--')
plt.xlabel('Country')
plt.ylabel('World Cup Wins')
plt.title("World Cup Wins by Country")
plt.show()


#Number 3 ----> another Line chart example
goals = [13,12,15,18,19,25,14,19]
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'July','Aug']

plt.plot(months,goals, color ="cyan", linestyle ='--')

# Add Labels
plt.xlabel('Months')
plt.ylabel('Goals')
plt.title('Goals scored by Man United each month in the season')

#show the graph
plt.show()


#Number 4 - If then Else examples

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

#Number 5 - For & While Loops

leagueswon = {'ManUtd':20, 'Lpool':20, 'Chelsea':7, 'Leeds':7, 'Everton':5, 'Arsenal':3}

for k in leagueswon:
    print(leagueswon[k])

cupswon = 0
while cupswon< 7:
        cupswon = (cupswon+1)
        if cupswon ==5:
            break
print('cups won are max five')

#Number 6 Introduction to DataFrames (essentially excel tables). Dataframes are very important

leaguetable = [['Utd',100,50],['Spurs',80,40],['Leeds',75,30],['Arsenal',74,22],['Chelsea',71,21],['Lpool',64,18],['Fulham',62,12]]
leaguetabledf= pd.DataFrame(leaguetable,columns=['Team','Points','Goals Scored'])
print(leaguetabledf)
#prints the top 4 teams
print(leaguetabledf.head(4))
#prints the bottom 3 teams
print(leaguetabledf.tail(3))

print(leaguetabledf.Points>85)
#shows that only the first team managed to get points above 85 in the season

print(leaguetabledf.Team=='Lpool')
#shows that only the fifth placed team is liverpool

topscorers = [['Fernandes','Utd',30,15],['Kane','Spurs',20,20],['Diaz','Leeds',15,10],['Cavani','Utd',24,12]]
topscorersdf= pd.DataFrame(topscorers,columns=['Player','Team','Points','Goals scored'])
print(topscorersdf)
print(topscorersdf.describe)
#gives info you need for all the top goal scorers

topscorersdf.plot(x='Player', y = 'Goals scored', kind='bar',title='Top Goal Scorers in season')
plt.show()

#Number 7 - simple example of important csvs as DataFrames

olympicmedals = pd.read_csv('C:\\Users\\LydonLaptop\\PycharmProjects\\pythonProject\\olympics.csv')

print(olympicmedals)

dfmedals=pd.DataFrame(olympicmedals.head(6))
#creates dfmedals as a dataframe, i.e. a table of the past six days
print(dfmedals)
#plots the medals by country of the last six days
dfmedals.plot(x='Date',kind="barh",title="Gold Medals Per Day")
plt.show()
