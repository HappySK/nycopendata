from flask import Flask, request, render_template
import pandas as pd
import mlflow
from os import environ


application = Flask(__name__,  template_folder='student_performance/frontend')

app = application
mlflow_tracking_uri = environ["MLFLOW_TRACKING_URI"]

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/stud_perf', methods=['GET', 'POST'])
def predict_datapoint():
    if request.method == 'GET':
        return render_template('home.html')
    else:
        form_data = {
            "gender": [str(request.form.get("gender"))],
            "race_ethnicity": [str(request.form.get("ethnicity"))],
            "parental_level_of_education": [str(request.form.get("parental_level_of_education"))],
            "lunch": [str(request.form.get("lunch"))],
            "test_preparation_course": [str(request.form.get("test_preparation_course"))],
            "reading_score": [int(request.form.get("reading_score"))],
            "writing_score": [int(request.form.get("writing_score"))]
        }

        form_data_df = pd.DataFrame(form_data)

        mlflow.set_tracking_uri(mlflow_tracking_uri)
        loaded_model = mlflow.pyfunc.load_model(model_uri=f"models:/stud_perf_regressor/latest")

        # Use the abstract function in FastTextWrapper to fetch the trained model.
        results = loaded_model.predict(form_data_df)

        return render_template("home.html", results=f"Student's Estimated Math Score is {results[0]}")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)