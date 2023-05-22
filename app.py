from flask import Flask , request , render_template,jsonify
from src.pipeline.prediction_pipeline import CustomData , PredictionPipeline



application = Flask(__name__)
app = application


@app.route('/')

def home_page():
    return render_template('index.html')

@app.route('/predict' , methods = ["GET" , "POST"])

def predict_datapoint():
    if request.method =='GET':
        return render_template('form.html')
    
    else:
        data = CustomData(
            Delivery_person_Age = int(request.form.get('Delivery_person_Age')),
            Weather_conditions = str(request.form.get('Weather_conditions')),
            Road_traffic_density = str(request.form.get('Road_traffic_density')),
            Type_of_order = str(request.form.get('Type_of_order')),
            Type_of_vehicle = str(request.form.get('Type_of_vehicle')),
            multiple_deliveries = int(request.form.get('multiple_deliveries')),
            Festival = str(request.form.get('Festival')),
            City = str(request.form.get('City'))

        )

        
        final_new_data = data.get_data_as_dataframe()
        predict_pipeline = PredictionPipeline()
        pred = predict_pipeline.predict(final_new_data)

        results = round(pred[0],2)

        return render_template('results.html' , final_result =results)
    




if __name__ == '__main__':
    app.run(host = '0.0.0.0' , debug = True , port = 5500)

