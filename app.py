#!/usr/bin/env python3

from flask import Flask, request, jsonify
from datetime import datetime


app = Flask(__name__)

@app.route('/api', methods=['GET'])
def index():
    slack_name = request.args.get('slack_name')
    day_of_week = current_time.strftime('%A')

    if slack_name is None or track is None:
        return jsonify({'error': 'Both slack_name and track are required'})

    current_time = datetime.utcnow()
    format_time = current_time.strftime('%Y-%m-%dT%H:%M:%SZ')
    track = request.args.get('track')

    return jsonify({
        'slack_name': slack_name,
        'current_day': day_of_week,
        'utc_time': format_time,
        'track': track,
        'github_file_url': 

        })

