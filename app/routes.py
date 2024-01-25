from flask import jsonify, request
from app import app, db
from app.models import Leaderboard
from datetime import datetime, timedelta

#Display current week leaderboard (Top 200)
@app.route('/current_week_leaderboard', methods=['GET'])

def current_week_leaderboard():
    # Calculate the start date of the current week
    today = datetime.now()
    start_of_week = today - timedelta(days=today.weekday())

    # Fetch the top 200 scores for the current week
    leaderboard = Leaderboard.query.filter(Leaderboard.TimeStamp >= start_of_week). \
         order_by(Leaderboard.Score.desc()).limit(200).all()
    #leaderboard = Leaderboard.query.filter(Leaderboard.TimeStamp >= start_of_week).order_by(Leaderboard.Score.desc()).limit(200).all()

    # Convert the leaderboard data to a JSON response
    leaderboard_data = [{
        'UID': entry.UID,
        'Name': entry.Name,
        'Score': entry.Score,
        'Country': entry.Country,
        'TimeStamp': entry.TimeStamp.strftime('%Y-%m-%d %H:%M:%S')
    } for entry in leaderboard]

    print(len(leaderboard_data))
    return jsonify({'leaderboard': leaderboard_data})




#Display last week leaderboard (Top 200)
@app.route('/last_week_leaderboard', methods=['GET'])
def last_week_leaderboard():
    # Get the country from the request parameters
    country = request.args.get('country')

    if not country:
        return jsonify({'error': 'Country parameter is required'}), 400

    # Calculate the start and end dates of the last week
    today = datetime.now()
    end_of_last_week = today - timedelta(days=today.weekday() + 1)
    start_of_last_week = end_of_last_week - timedelta(days=6)

    # Fetch the top 200 scores for the last week in the specified country
    leaderboard = Leaderboard.query.filter(
        Leaderboard.TimeStamp >= start_of_last_week,
        Leaderboard.TimeStamp <= end_of_last_week,
        Leaderboard.Country == country
    ).order_by(Leaderboard.Score.desc()).limit(200).all()

    # Convert the leaderboard data to a JSON response
    leaderboard_data = [{
        'UID': entry.UID,
        'Name': entry.Name,
        'Score': entry.Score,
        'Country': entry.Country,
        'TimeStamp': entry.TimeStamp.strftime('%Y-%m-%d %H:%M:%S')
    } for entry in leaderboard]

    print(len(leaderboard_data))
    return jsonify({'leaderboard': leaderboard_data})



#Fetch user rank, given the userId.
@app.route('/user_rank', methods=['GET'])
def user_rank():
    # Get the userId from the request parameters
    user_id = request.args.get('userId')

    if not user_id:
        return jsonify({'error': 'userId parameter is required'}), 400

    # Fetch the rank of the user with the specified userId
    user_entry = Leaderboard.query.filter_by(UID=user_id).first()

    if not user_entry:
        return jsonify({'error': f'User with userId {user_id} not found'}), 404

    # Fetch the count of users with a higher score
    higher_rank_count = Leaderboard.query.filter(Leaderboard.Score > user_entry.Score).count()

    # The user's rank is one plus the count of higher scores
    user_rank = higher_rank_count + 1

    print(user_rank)
    return jsonify({'userId': user_id, 'userRank': user_rank})