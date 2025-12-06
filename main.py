from flask import Flask, request, jsonify

app = Flask(__name__)


#using a get method
@app.route('/get-user/<user_id>')
def get_user(user_id):
    user_id = {
        'user_id': user_id,         
        'name': 'john patrick',
        'email': 'johnpatrick@gmail.com'
    }


if __name__ == '__main__' :
    app.run(debug=True)  #run the flask server 
