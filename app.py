from flask import Flask
 
app = Flask(__name__)
 
@app.route('/')
def first_api():
    return 'Looking Cool'
 
# main function
if __name__ == '__main__':
    app.run()
