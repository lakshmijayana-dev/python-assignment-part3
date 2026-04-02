import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("students.csv")

# Check data
print(df.head())

# Create avg_score
subject_cols = ['math','science','english','history','pe']
df['avg_score'] = df[subject_cols].mean(axis=1)

# Simple plot
sns.barplot(data=df, x='passed', y='math')
plt.title("Test Plot")
plt.show()
plt.show()


import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

# Load data
df = pd.read_csv("students.csv")

# Features and target
X = df[['math', 'science', 'english', 'history', 'pe', 'attendance_pct', 'study_hours_per_day']]
y = df['passed']

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Scaling
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Model
model = LogisticRegression()
model.fit(X_train_scaled, y_train)

# Training accuracy
train_acc = model.score(X_train_scaled, y_train)
print("Training Accuracy:", train_acc)

# Test accuracy
test_acc = model.score(X_test_scaled, y_test)
print("Test Accuracy:", test_acc)

# Predictions
y_pred = model.predict(X_test_scaled)

# Print results with names
print("\nPredictions:")
for i in range(len(y_test)):
    name = df.loc[X_test.index[i], 'name']
    actual = y_test.iloc[i]
    pred = y_pred[i]
    
    result = "✅ Correct" if actual == pred else "❌ Wrong"
    
    print(f"{name}: Actual={actual}, Predicted={pred} -> {result}")


    