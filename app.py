from flask import Flask, request, jsonify
import datetime

app = Flask("my_app")  #  "my_app"  name of Flask application

@app.route('/api', methods=['GET'])
def get_info():
    slack_name = "Mr Mint"  # Set the Slack name to "Mr Mint"
    track = "backend"  # Set the track to "backend"
    current_day = datetime.datetime.now().strftime('%A')
    utc_time = datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')
    github_file_url = "https://github.com/Mint-cc/Mr-mint/blob/main/app.py"
    github_repo_url = " https://github.com/Mint-cc/Mr-mint"

    response_data = {
        "slack_name": slack_name,
        "current_day": current_day,
        "utc_time": utc_time,
        "track": track,
        "github_file_url": github_file_url,
        "github_repo_url": github_repo_url,
        "status_code": 200
    }

    return jsonify(response_data)

if __name__ == '__main__':
    app.run()
