# forest_fire_prediction
A Flask-based web app that predicts the probability of forest fire occurrence using temperature, oxygen, and humidity as input. Built with a logistic regression model and a clean Materialize CSS UI. Outputs risk level and percentage chance to help with early warning.
🔥 Forest Fire Prediction App
This project is a Machine Learning-based web application that predicts the probability of a forest fire occurring based on environmental inputs such as temperature, oxygen level, and humidity.

📌 Features:

    👉Logistic Regression model trained on a labeled forest fire dataset

    👉Web interface built using Flask

    👉Takes real-time user input and predicts the risk percentage of forest fire

    👉Responsive UI styled with Materialize CSS

    👉Error handling and user-friendly messages for invalid input

📊 Input Parameters:

    🔹Temperature (°C)

    🔹Oxygen (ppm)

    🔹Humidity (%)

✅ Output:

    ⭐ Percentage probability of fire occurrence

    ⭐ Message indicating safety level (e.g., 🔥 High Risk or ✅ Safe)

📁Project Structure:

csharp

Copy

Edit

ForestFireApp/

├── app.py               # Flask backend

├── forest_fire.py       # Model training & pickle generation

├── model.pkl            # Saved ML model

├── Forest_fire.csv      # Dataset

├── templates/

│   └── forest_fire.html # Frontend HTML

└── static/
   
    ├── css/
    
    │   └── materialize.css
    
    └── css2/
    
        └── style.css

📦 Requirements:

    🔸Python 3.10+

    🔸Flask

    🔸NumPy

    🔸Pandas

    🔸scikit-learn

📌 Author

Made with ❤️ by Dharshini

Feel free to fork, improve, or contribute!
