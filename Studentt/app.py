from flask import Flask, render_template, request
import numpy as np
from sklearn.linear_model import LinearRegression

app = Flask(__name__)

# Sample training data
X = np.array([[1], [2], [3], [4], [5], [6]])
y = np.array([35, 45, 50, 60, 70, 80])

model = LinearRegression()
model.fit(X, y)

@app.route('/', methods=['GET', 'POST'])
def home():
    prediction = None

    if request.method == 'POST':
        hours = float(request.form['hours'])
        prediction = model.predict([[hours]])[0]

    return render_template('index.html', prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)