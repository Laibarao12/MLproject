##THIS application.py is for DEPLOYMENT PURPOSE 

from flask import Flask, request, render_template
from src.pipeline.predict_pipeline import CustomData, PredictPipeline

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predictdata', methods=['POST'])
def predict_data():
    data = CustomData(
        gender=request.form['gender'],
        race_ethnicity=request.form['race_ethnicity'],
        parental_level_of_education=request.form['parental_level_of_education'],
        lunch=request.form['lunch'],
        test_preparation_course=request.form['test_preparation_course'],
        reading_score=request.form['reading_score'],
        writing_score=request.form['writing_score']
    )

    pred_df = data.get_data_as_data_frame()
    print(pred_df)

    pred_pipeline = PredictPipeline()
    results = pred_pipeline.predict(pred_df)

    return render_template('result.html', results=results[0])

if __name__ == "__main__":
    app.run(host="0.0.0.0")


