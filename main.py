from flask import Flask , jsonify
from pycricbuzz import Cricbuzz
import json

app = Flask(__name__)

@app.route('/' ,methods=['GET'])
def cricket_info():
    result = []
    c = Cricbuzz()
    matches = c.matches()
    print (json.dumps(matches,indent=4))
    result.append(matches)
    return jsonify({'matches': result})

@app.route('/info/<mid>' ,methods=['POST'])
def match_info(mid):
    match_info_result = []
    c = Cricbuzz()
    minfo = c.matchinfo(mid)
    print(json.dumps(minfo, indent=4, sort_keys=True))
    match_info_result.append(minfo)
    return jsonify({'match information':match_info_result})

@app.route('/live/<mid>',methods=['POST'])
def live_score(mid):
    match_live_score = []
    c = Cricbuzz()
    lscore = c.livescore(mid)
    print("***********")
    print(json.dumps(lscore, indent=4, sort_keys=True))
    match_live_score.append(lscore)
    return jsonify({'Live score ': match_live_score})

@app.route('/player/<mid>',methods=['POST'])
def players(mid):
    players_info = []
    c = Cricbuzz()
    cplayers = c.players_mapping(mid)
    players_info.append(cplayers)
    return jsonify({'player': players_info})



@app.route('/commentory/<mid>',methods=['POST'])
def commentary(mid):
    commentory_by_ball = []
    c = Cricbuzz()
    comm = c.commentary(mid)
    print(json.dumps(comm, indent=4, sort_keys=True))
    commentory_by_ball.append(comm)
    return jsonify({'commentory by Ball': commentory_by_ball})

@app.route('/scorecard/<mid>',methods=['POST'])
def scorecard(mid):
    result = []
    c = Cricbuzz()
    scard = c.scorecard(mid)
    print(json.dumps(scard, indent=4, sort_keys=True))
    result.append(scard)
    return jsonify({'scorecard' : result })


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)