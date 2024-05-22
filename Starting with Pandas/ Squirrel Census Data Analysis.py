import pandas as pd

data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
grey = len(data[data["Primary Fur Color"] == "Gray"] )
cinnamon = len(data[data["Primary Fur Color"] == "Cinnamon"] )
Black = len(data[data["Primary Fur Color"] == "Black"] )

dict = {
    "Primary Fur Color" :  ['Grays', 'Cinnamon', 'Black'],
    "count" : [grey,cinnamon,Black]
}

df=pd.DataFrame(dict)
df.to_csv("Squirral_count.csv")

