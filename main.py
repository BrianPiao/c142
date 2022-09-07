from flask import Flask,jsonify,request
from store import allmov,lm,nlm,dnw
from demo import output
from cont import get_recommendations

app = Flask(__name__)
@app.route("/get-movie")
def getmov():
    movieData = {
        "title": allmov[0][19],
        "poster_link": allmov[0][27],
        "release_date": allmov[0][13] or "N/A",
        "duration": allmov[0][15],
        "rating": allmov[0][20],
        "overview": allmov[0][9]
    }
    return jsonify({
        "data": movieData,
        "status": "success"
    })

@app.route("/like-movie" , methods = ["POST"])
def like_movie():
    m = allmov[0]
    lm.append(m)
    allmov.pop(0)
    return jsonify({
        "status" : "success"
    }),201

@app.route("/dislike-movie" , methods = ["POST"])
def dislike_movie():
    m = allmov[0]
    nlm.append(m)
    allmov.pop(0)
    return jsonify({
        "status" : "success"
    }),201

@app.route("/unwatched-movie" , methods = ["POST"])
def unwatched_movie():
    m = allmov[0]
    dnw.append(m)
    allmov.pop(0)
    return jsonify({
        "status" : "success"
    }),201

@app.route("/popular-movie")
def popular_movie():
    movieData = []
    for i in output:
        b  = {
            "title": i[0],
            "poster_link": i[1],
            "release_date": i[2] or "N/A",
            "duration": i[3],
            "rating": i[4],
            "overview": i[5]
        }
        movieData.append(b)
    return jsonify({
        "data": movieData,
        "status": "success"
    }),200
    
@app.route("/rec-movies")
def rec_movies():
    allrec = []
    for i in lm:
        o = get_recommendations(i[19]) 
        for e in o:
            allrec.append(e)
    import itertools
    allrec.sort()
    allrec = list(allrec for allrec, _ in itertools.groupby(allrec))
    movieData = []
    for i in allrec:
        b  = {
            "title": i[0],
            "poster_link": i[1],
            "release_date": i[2] or "N/A",
            "duration": i[3],
            "rating": i[4],
            "overview": i[5]
        }
        movieData.append(b)
    return jsonify({
        "data": movieData,
        "status": "success"
    }),200
if(__name__ == "__main__"):
    app.run(debug = True)