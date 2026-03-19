from sklearn.tree import DecisionTreeClassifier

X = [[180,80,44],
     [177,70,43],
     [160,60,38],
     [154,54,37],
     [166,65,40],
     [190,90,47]]

Y = [1,1,0,0,1,1]

model = DecisionTreeClassifier()
model.fit(X,Y)

result = model.predict([[185,85,45]])

print("Prediction:", result)

if result[0] == 1:
    print("Male")
else:
    print("Female")
