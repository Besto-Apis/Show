from flask import Flask, Response,request
import requests

app = Flask(__name__)

@app.route('/Token-Jwt', methods=['GET'])
def get_token():
    Key = request.args.get('Key')

    if not Key:
        return ' - Missing Access Key ! ', 400
    if Key != 'C4-BESTO-OI-LL-1K':
        return Response(' - Bad Access Key ! Call DevloPer Besto | @BestoPy')
       
    response = requests.get('https://raw.githubusercontent.com/Besto-Apis/Tt/refs/heads/main/Jwt.txt')
    if response.status_code == 200 or 201:
    	return Response(response.text, status=200, mimetype='text/plain')
    else:
    	return Response(" - Error ! For Get Jwt Token", status=500, mimetype='text/plain')
    	
if __name__ == '__main__':
    app.run(debug=False)
