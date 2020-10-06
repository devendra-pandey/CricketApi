from flask import Flask , jsonify
from pycricbuzz import Cricbuzz
import json


app = Flask(__name__)

# @app.route('/' ,methods=['GET'])
# def cricket_info():
#     result = []
c = Cricbuzz()
matches = c.matches()
print (json.dumps(matches,indent=4))
    # result.append(matches)
    # return jsonify({'matches': result})

@app.route('/info/<int:mid>' ,methods=['GET'])
def match_info(mid):
    c = Cricbuzz()
    minfo = c.matchinfo(mid)
    print(json.dumps(minfo, indent=4, sort_keys=True))

@app.route('/live/<int:mid>',methods=['GET'])
def live_score(mid):
    c = Cricbuzz()
    lscore = c.livescore(mid)
    print("***********")
    print(json.dumps(lscore, indent=4, sort_keys=True))

@app.route('/commentory/<int:mid>',methods=['GET'])
def commentary(mid):
    c = Cricbuzz()
    comm = c.commentary(mid)
    print(json.dumps(comm, indent=4, sort_keys=True))

@app.route('/scorecard/<int:mid>',methods=['GET'])
def scorecard(mid):
    c = Cricbuzz()
    scard = c.scorecard(mid)
    print(json.dumps(scard, indent=4, sort_keys=True))


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)