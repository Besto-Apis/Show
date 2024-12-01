from flask import Flask, Response, request
import requests,base64

app = Flask(__name__)

encoded_token = 'Z2hwX0ZnY3FXWDRsTUM5RkFWZVJvZlM0TTBRTGQwU3ZNYjFBM0cxOA=='
GITHUB_TOKEN = base64.b64decode(encoded_token).decode()
REPO_OWNER = 'Besto-Apis'
REPO_NAME = 'ToKens'

def github_request(method, file_path, data=None):
    url = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/contents/{file_path}"
    headers = {"Authorization": f"token {GITHUB_TOKEN}"}
    response = requests.request(method, url, headers=headers, json=data)
    return response
    
def fetch_file_content(file_path):
    response = github_request("GET", file_path)
    if response.status_code == 200:
        content = base64.b64decode(response.json()["content"]).decode("utf-8").strip()
        return content
    print(f"Error fetching {file_path}, Status: {response.status_code}")
    return ""

@app.route('/Token-Jwt', methods=['GET'])
def get_token():
    Jwt = request.args.get('Jwt')
    Key = request.args.get('Key')
    
    if not Key:
        return ' - Missing Access Key ! ', 400
    if Key != 'C4-BESTO-JWT-TOKENS-H9L0':
        return Response(' - Bad Access Key ! Call DevloPer Besto | @BestoPy')

    if Jwt is None or int(Jwt) not in range(1, 6):
        return Response(" - Invalid Jwt Number !", status=400)

    file_name = f'Jwt{Jwt}.txt'
    file_content = fetch_file_content(file_name)
    if file_content:
        return Response(file_content, status=200, mimetype='text/plain')
    return Response(" - Error : No Jwt{Jwt} File !", status=500, mimetype='text/plain')

if __name__ == '__main__':
    app.run(debug=False)
