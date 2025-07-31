from flask import Flask,request, url_for, redirect, render_template
import pickle
import numpy as np

app = Flask(__name__)

model=pickle.load(open('model.pkl','rb'))
@app.route('/')
def hello_world():
    return render_template("forest_fire.html")

@app.route('/predict', methods=['POST', 'GET'])
def predict():
    try:
        int_features = [int(x) for x in request.form.values()]
        final = [np.array(int_features)]
        prediction = model.predict_proba(final)  # Gives probabilities

        probability = prediction[0][1]  # Probability of class 1 (fire)
        output = '{:.2f}%'.format(probability * 100)  # Convert to percentage

        if probability > 0.5:
            return render_template('forest_fire.html',
                                   pred=f'🔥 High Risk: {output} chance of forest fire.',
                                   bhai="⚠️ Take immediate preventive measures.")
        else:
            return render_template('forest_fire.html',
                                   pred=f'✅ Low Risk: Only {output} chance of fire.',
                                   bhai="✔️ Your forest is safe for now.")
    except ValueError:
        return render_template('forest_fire.html',
                               pred='❌ Invalid input: Please enter only numbers in all fields.',
                               bhai="Try again.")



if __name__ == '__main__':
    app.run(debug=True)