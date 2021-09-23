import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from datetime import datetime

dublingaa = pd.read_csv('C:\\Users\\LydonLaptop\\PycharmProjects\\pythonProject\\dublingaa.csv')

#quick peak at the dataset#

print(dublingaa.head())

#add a total score for and conceded column and winning margin

dublingaa["goalsscored_in_points"]= dublingaa["goals_for"]*3
dublingaa["goalsagainst_in_points"]= dublingaa["goals_against"]*3
dublingaa["totalpoints_for"] = dublingaa["goalsscored_in_points"] + dublingaa["points_for"]
dublingaa["totalpoints_against"] = dublingaa["goalsagainst_in_points"] + dublingaa["points_against"]
dublingaa["winning_margin"]=dublingaa["totalpoints_for"] - dublingaa["totalpoints_against"]
dublingaa["Year"] = dublingaa["Season"].astype(str)
dublingaa["Match"] = dublingaa["Year"] + " " + dublingaa["Fixture"]
dublingaa["Series_Yr"] = dublingaa["Year"] + " " + dublingaa["Series"]
print(dublingaa)

#quick check to make sure the calc worked

dublingaa.plot(x="Match",y="winning_margin",kind="scatter", color="blue",title="Winning Margin over Time",rot=68)


plt.grid(True,linestyle="--")
plt.show()

#summary statistics

# Has there been a material drop off in their winning margin?

print(dublingaa.groupby("Season")["winning_margin"].agg([np.mean,min,sum,max]))
print(dublingaa.groupby("Series_Yr")["winning_margin"].agg([max,min,sum]))

meanmargin = dublingaa.groupby("Season")["winning_margin"].mean()
meanmargin_byseries = dublingaa.groupby("Series_Yr")["winning_margin"].mean()

meanmargin.plot(x="Season",kind="bar", color="blue",title="Avg Margin per season")
plt.grid(True,linestyle="--")
plt.show()

meanmargin_byseries.plot(x="Season",kind="bar", color="green",title="Avg Margin per Series, per Season",rot=40)
plt.grid(True,linestyle="--")
plt.show()

# what about points scored and conceded?

print(dublingaa.groupby("Series_Yr")["totalpoints_for"].agg([np.mean,min,sum,max]))
print(dublingaa.groupby("Series_Yr")["totalpoints_against"].agg([np.mean,min,sum,max]))
print(dublingaa.groupby("Season")["goals_for"].agg([np.mean,min,sum,max]))

meantotalpoints=dublingaa.groupby("Season")["totalpoints_for"].mean()
meangoals=dublingaa.groupby("Series_Yr")["goals_for"].mean()
meantotalgoals_against=dublingaa.groupby("Season")["goals_against"].mean()

dublingaa.plot(x="totalpoints_against",y="totalpoints_for",kind="scatter",title="points scored vs against since 2011")
plt.grid(True,linestyle="--")
plt.show()

meantotalpoints.plot(x="Season",y="totalpoints_for",kind="bar",color="orange",title="Average points (inc goals) per season")
plt.grid(True,linestyle="--")
plt.show()

meantotalgoals_against.plot(x="Season",y="totalpoints_against",kind="bar",color="cyan",title="Avg Goals conceded")
plt.grid(True,linestyle="--")
plt.show()

meangoals.plot(x="Series_Yr",y="goals_for",kind="bar",color="pink",title="Average goals per season",rot=45)
plt.grid(True,linestyle="--")
plt.show()

print(dublingaa.groupby("Season")["goals_for"].agg([np.mean,min,sum,max]))
print(dublingaa.groupby("Series_Yr")["goals_for"].agg([np.mean,min,sum,max]))

fi, ax = plt.subplots()
ax.plot(dublingaa["Series_Yr"],dublingaa["goals_for"])
plt.show()
















