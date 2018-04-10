from flask import Flask
from service.msRehber import getRehber

app = Flask(__name__)

@app.route('/rehber/<int:kodu>', methods=['GET'])
def restRehber(kodu):
    return getRehber(kodu)

if __name__=="__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
    print("Server started successfully!")
