
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#class 1-6 joins, merges, left right, suffixes etc.

yellowjersey = pd.read_csv('yellowjersey.csv')
stagewinners = pd.read_csv('stagewinners.csv')
historicalstagewinners = pd.read_csv('historicalstagewinners.csv')

print(yellowjersey.head())
print(stagewinners.head())

yellow_and_winner = yellowjersey.merge(stagewinners, on = "Stage", suffixes = ("_in Yellow","_StageWinner"))

print(yellow_and_winner.head())

stagewinner_historicalwins = stagewinners.merge(historicalstagewinners, left_on = "Stage Winner", right_on = "Rider", how = "left")

print(stagewinner_historicalwins)

#notice with the left join, it doesnt only shows the data from this year's tour, ignoring Anquetil Merckx etc.

#working with indexes


stagewinners2 = pd.read_csv('stagewinners.csv',index_col="Stage")
yellow2 = pd.read_csv('yellowjersey.csv',index_col="Stage")

yellow_stage = stagewinners2.merge(yellow2, on = "Stage", how = "right",suffixes = ["_Stage","_inYellow"])

print(yellow_stage)

# shows us the same as before, but now the index is the stage number

# class 8 filtering joins. showing us only observations based on whether they match in another table


yellowjersey3 = pd.read_csv('yellowjersey.csv')
stagewinners3 = pd.read_csv('stagewinners.csv',index_col="Stage")
historicalstagewinners3 = pd.read_csv('historicalstagewinners.csv')

yellowstage3 = yellowjersey3.merge(stagewinners3,on= "Team")
print(yellowstage3)

# class 9 concatenate
stagewinners2021 = pd.read_csv('stagewinners2021.csv',index_col="Stage")
allwinners = pd.concat([stagewinners3, stagewinners2021], keys = ["2020","2021"])

print(allwinners)

#append method

allwinners2 = stagewinners3.append([stagewinners2021])

print(allwinners2)

# append is handy but it doesnt take keys like concat does

#class 10 verifying integrity

yellowjersey4 = pd.read_csv('yellowjersey.csv')
stagewinners4 = pd.read_csv('stagewinners.csv')
historicalstagewinners4 = pd.read_csv('historicalstagewinners.csv')

yellow_and_winner4 = yellowjersey.merge(stagewinners, on = "Stage", suffixes = ("_in Yellow","_StageWinner"),validate="one_to_one")

# if we have validate one to one on stage its fine, but on team its not as there are no multiple (i.e not unique) teams

print(yellow_and_winner4)

historicalstagewinners5 = pd.read_csv('historicalstagewinners.csv')

rank = historicalstagewinners5.sort_values(by="Historical Wins", ascending = False)

print(rank)

rank.plot(x= "Rider", y = "Historical Wins", title = "Most Tour Stage Wins", kind= "bar", color = "yellow")
plt.show()

# using merge order class 11

aapl = pd.read_csv('AAPL.csv')
fb = pd.read_csv('FB.csv')

print(aapl)
print(fb)


stockprices = pd.merge_ordered(aapl, fb, on = ["Time"], suffixes= ("_Apple", "Facebook"),fill_method="ffill",how="left")

print(stockprices.tail())

stockprices.plot(x="Time",y = ["Close Price_Apple","Close PriceFacebook"])
plt.show()



#the ffill method fixed the missing date information we had!! :)
#merge as of method can round to nearest time of day also for us


#class 13 query method

yellowjersey5 = pd.read_csv('yellowjersey.csv')
stagewinners5 = pd.read_csv('stagewinners.csv')
historicalstagewinners5 = pd.read_csv('historicalstagewinners.csv')

print(stagewinners5.query('Team=="Sky"'))
print(stagewinners5.query('Stage>7'))

#class 14 melt method

top3seasonwins = pd.read_csv('tourtop3seasonvictories horizontal.csv')

print(top3seasonwins)

seasonwins_tall = top3seasonwins.melt(id_vars=["Rider","Team"], value_name = "SeasonWins", var_name = "Season")

print(seasonwins_tall)

seasonwins_tall["cumulative wins"] = seasonwins_tall.groupby("Rider")["SeasonWins"].cumsum()

#cumulative sum if in python!!

print(seasonwins_tall)

seasonwins_tall.plot(x="Season", y = "SeasonWins",kind="bar")
plt.show()











































