import pandas as pd

data = pd.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
colors = data['Primary Fur Color'].tolist()
print(colors)
countG = 0
countC = 0
countB = 0
for color in colors:
    if 'Gray' == color:
        countG += 1
    elif 'Cinnamon' == color:
        countC += 1
    elif 'Black' == color:
        countB += 1

print(countG)
print(countC)
print(countB)

squirrels = {
    'Fur Color' : ['grey', 'red', 'black'],
    'count' : [countG, countC, countB]
}

new_df = pd.DataFrame(squirrels)
new_df.to_csv('squirrel_colors.csv')