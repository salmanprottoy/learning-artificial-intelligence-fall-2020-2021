import pandas as pd
from sklearn.tree import DecisionTreeClassifier

data = pd.read_csv('ip.csv')
# input set
X = data.drop(columns=['BA'])
# output set
y = data['BA']

model = DecisionTreeClassifier()
model.fit(X, y)

prediction = model.predict([[19216810128, 19216810129, 19216810158], [1921681064, 1921681065, 1921681094], [19216810160,19216810161,19216810190]])

print(prediction)
