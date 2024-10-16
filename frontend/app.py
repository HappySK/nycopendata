from flask import Flask, request, render_template
import pandas as pd
import mlflow

app = Flask(__name__,  template_folder='templates')

@app.route('/')
def index():
    return render_template('student_performance/home.html')

@app.route('/stud_perf', methods=['GET', 'POST'])
def predict_datapoint():
    if request.method == 'GET':
        return render_template('student_performance/home.html')
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

        loaded_model = mlflow.pyfunc.load_model(model_uri=f"models:/stud_perf_regressor/latest")

        # Use the abstract function in FastTextWrapper to fetch the trained model.
        results = loaded_model.predict(form_data_df)

        return render_template("student_performance/home.html", results=f"Student's Estimated Math Score is {results[0]}")

@app.route('/diabetics', methods=['GET', 'POST'])
def predict_diabetics():
    if request.method == 'GET':
        return render_template('diabetics/index.html')
    else:
        form_data = {
            'age': [int(request.form.get("age"))],
            'gender': [str(request.form.get("gender"))],
            'polyuria': [str(request.form.get("polyuria"))],
            'polydipsia': [str(request.form.get("polydipsia"))],
            'sudden_weight_loss': [str(request.form.get("sudden_weight_loss"))],
            'weakness': [str(request.form.get("weakness"))],
            'polyphagia': [str(request.form.get("polyphagia"))],
            'genital_thrush': [str(request.form.get("genital_thrush"))],
            'visual_blurring': [str(request.form.get("visual_blurring"))],
            'itching': [str(request.form.get("itching"))],
            'irritability': [str(request.form.get("irritability"))],
            'delayed_healing': [str(request.form.get("delayed_healing"))],
            'partial_paresis': [str(request.form.get("partial_paresis"))],
            'muscle_stiffness': [str(request.form.get("muscle_stiffness"))],
            'alopecia': [str(request.form.get("alopecia"))],
            'obesity': [str(request.form.get("obesity"))]
}
        form_data_df = pd.DataFrame(form_data)

        loaded_model = mlflow.pyfunc.load_model(model_uri=f"models:/stud_perf_classifier/latest")

        # Use the abstract function in FastTextWrapper to fetch the trained model.
        diabetics_probability = loaded_model.predict(form_data_df)
        print("The output", diabetics_probability['predicted_score_Positive'][0])
        return render_template("diabetics/index.html", results=f"There is a chance of {diabetics_probability['predicted_score_Positive'][0] * 100} % that you have Diabetes")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)