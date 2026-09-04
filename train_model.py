import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.tree import DecisionTreeClassifier
import joblib

df = pd.read_csv("student_data.csv")

encoder = LabelEncoder()
df["Performance"] = encoder.fit_transform(df["Performance"])

X = df.drop("Performance", axis=1)
y = df["Performance"]

model = DecisionTreeClassifier()
model.fit(X, y)

joblib.dump(model, "student_model.pkl")

print("Model Trained Successfully")