from flask import Flask, request
import os
import json

app = Flask(__name__)

filename = 'webhookPayloads.txt'

if os.path.exists(filename):
    append_write = 'a'
else:
    append_write = 'w'

@app.route('/', methods=['POST','GET'])
def index():
    if request.method == 'GET':
        return '<h1>Hello from Webhook Listener!</h1>'
    if request.method == 'POST':
        f = open(filename,append_write)
        req_data = request.get_json()
        #str_obj = json.dumps(req_data)
        str_obj = "nikhilpost"
        f.write(str_obj+'\n')
        f.close()
        return '{"success":"true"}'

# run the app
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, threaded=True, debug=True)
