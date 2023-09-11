from flask import Flask, request, jsonify
import datetime
import json


app = Flask(__name__)

# Define the route for the endpoint
@app.route('/api', methods=['GET'])
def get_info():
    # Get query parameters
    slack_name = request.args.get('slack_name')
    track = request.args.get('track')

    # Validate that both query parameters are provided
    if not slack_name or not track:
        return jsonify({"error": "Both slack_name and track are required."}), 400

    # Get the current day of the week in full
    current_day_of_week = datetime.datetime.utcnow().strftime('%A')

    # Get the current UTC time
    utc_time = datetime.datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')

    # GitHub repo URL and file URL
    github_repo_url = 'https://github.com/Mint-cc/Mr-mint.git'
    github_file_url = 'https://github.com/Mint-cc/Mr-mint/blob/main/main.py'

    # Construct the original response JSON
    original_response = {
        'Slack Name': "Mr mint",
        'Current Day of the Week': "Monday",
        'Current UTC Time': "2023-09-11T04:58:01Z",
        'Track': "backend",
        'GitHub File URL': "https://github.com/Mint-cc/Mr-mint/blob/main/main.py",
        'GitHub Repo URL': "https://github.com/Mint-cc/Mr-mint.git",
        'Status Code': 200
    }

    # Create a new dictionary with rearranged keys
    new_response = {
    "slack_name": original_response["Slack Name"],
    "current_day": original_response["Current Day of the Week"],
    "utc_time": original_response["Current UTC Time"],
    "track": original_response["Track"],
    "github_file_url": original_response["GitHub File URL"],
    "github_repo_url": original_response["GitHub Repo URL"],
    "status_code": original_response["Status Code"]
     }
     
    # Convert the new_response dictionary to JSON
    new_response_json = json.dumps(new_response, indent=2)

    # Send the JSON response
    return new_response_json, 200, {'Content-Type': 'application/json'}

if __name__ == '__main__':
    app.run(debug=True)
