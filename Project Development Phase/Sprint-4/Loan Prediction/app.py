from flask import Flask, render_template, request
import numpy as np
import pickle
import pandas
import os
app=Flask (__name__)
model = pickle.load(open ('rdf1.pkl', 'rb')) 
scale = pickle.load(open('scale1.pkl','rb')) 
@app.route('/') # rendering the html template 
def home(): 
    return render_template('home.html')
@app.route('/prediction',methods=["POST","GET"])  
def prediction(): 
    return render_template('prediction.html')

@app.route('/result', methods = [ "POST","GET"])# route to show the predictions in a web UI def 
def result():
   input_feature=[int(x) for x in request.form.values() ]
    #input_feature = np.transpose(input_feature)
   input_feature=[np.array(input_feature)]
   print(input_feature)
   names = ['Gender', 'Married', 'Dependents', 'Education', 'Self Employed', 'Applicant Income', 'Coapplicant Income', 'LoanAmount', 'Loan_Amount_Term', 'Credit_History', 'Property_Area']
   data = pandas.DataFrame(input_feature, columns=names) 
   print(data)
   #data_scaled = scale.fit_transform(data) #data = pandas.DataFrame(, columns=names)
   # predictions using the loaded model file prediction=model.predict(data)
   prediction=model.predict(data)
   print (prediction)
   prediction = int(prediction)
   print(type(prediction))
   if (prediction == 0):
      return render_template("result.html", result = "Loan wiil Not be Approved")
   else:
    #showing the prediction results in a UI
      return render_template("result.html", result = "Loan will be Approved")

  
    
  
if __name__=="__main__":
# app.run(host='0.0.0.0', port=8000, debug=True) 
  port=int(os.environ.get('PORT',5000)) 
  app.run(debug=False)