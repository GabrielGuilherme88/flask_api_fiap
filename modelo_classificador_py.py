import joblib
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

data = load_iris()
x,y = data.data, data.target

x_train, x_test, y_train, y_test = train_test_split(
    
    x, y, 
    
        test_size=0.2, random_state=42)

model = LogisticRegression(max_iter=200, random_state=42)
model.fit(x_train, y_train)

score = model.score(x_test, y_test)
print(f"Model accuracy: {score:.4f}")

joblib.dump(model, "iris_model.pkl")
print("Model saved as iris_model.pkl")