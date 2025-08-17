from flask import Flask, request, render_template
import joblib
from utils.feature_extraction import extract_features

app = Flask(__name__)
model = joblib.load('model/phishing_model.pkl')

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        url = request.form['url']
        features = extract_features(url)
        feature_list = [features['url_length'], features['has_ip'], features['has_https'],
                        features['special_chars'], features['domain_age']]
        prediction = model.predict([feature_list])
        result = "Phishing" if prediction[0] == 1 else "Safe"
        return render_template('result.html', result=result)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
