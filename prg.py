from flask import Flask, request, render_template
from joblib import load
app = Flask(__name__)
model= load('lrtest.save')
trans=load('transsformer')


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/y_predict',methods=['POST'])
def y_predict():
    '''
    For rendering results on HTML GUI
    '''
    x_test = [[x for x in request.form.values()]]
    print(x_test)
    x_test[0][0]=int(x_test[0][0])
    x_test[0][2]=int(x_test[0][2])
    x_test[0][6]=int(x_test[0][6])
    x_test[0][7]=int(x_test[0][7])
    
    test=trans.transform(x_test)
    print(test)
    prediction = model.predict(test)
    print(prediction)
    if prediction[0]==1:
        output='Good'
    else:
        output='Bad'
    
    return render_template( 'index.html',prediction_text='Financial Risk: {}'.format(output))

@app.route('/more_info',methods=['GET'])
def more_info():
    return render_template('new.html')


if __name__ == "__main__":
    app.run(debug=True)

