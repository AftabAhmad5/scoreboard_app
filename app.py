from flask import Flask, request, render_template

app = Flask(__name__)

# Initialize scores and team names
home_score = 0
away_score = 0
home_team = "Home Team"
away_team = "Away Team"

@app.route('/')
def index():
    return render_template('scoreboard.html', home_score=home_score, away_score=away_score, home_team=home_team, away_team=away_team)

@app.route('/update_home_score', methods=['POST'])
def update_home_score():
    global home_score
    home_score = int(request.form['home_score'])
    return render_template('scoreboard.html', home_score=home_score, away_score=away_score, home_team=home_team, away_team=away_team)

@app.route('/update_away_score', methods=['POST'])
def update_away_score():
    global away_score
    away_score = int(request.form['away_score'])
    return render_template('scoreboard.html', home_score=home_score, away_score=away_score, home_team=home_team, away_team=away_team)

@app.route('/update_home_team', methods=['POST'])
def update_home_team():
    global home_team
    home_team = request.form['home_team']
    return render_template('scoreboard.html', home_score=home_score, away_score=away_score, home_team=home_team, away_team=away_team)

@app.route('/update_away_team', methods=['POST'])
def update_away_team():
    global away_team
    away_team = request.form['away_team']
    return render_template('scoreboard.html', home_score=home_score, away_score=away_score, home_team=home_team, away_team=away_team)

if __name__ == '__main__':
    app.run(debug=True)
