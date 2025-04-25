# Test data for OctoFit Tracker
# This file contains sample data for users, teams, activities, leaderboard, and workouts

from datetime import timedelta

test_data = {
    "users": [
        {"username": "thundergod", "email": "thundergod@mhigh.edu", "password": "thundergodpassword"},
        {"username": "metalgeek", "email": "metalgeek@mhigh.edu", "password": "metalgeekpassword"},
        {"username": "zerocool", "email": "zerocool@mhigh.edu", "password": "zerocoolpassword"},
        {"username": "crashoverride", "email": "crashoverride@hmhigh.edu", "password": "crashoverridepassword"},
        {"username": "sleeptoken", "email": "sleeptoken@mhigh.edu", "password": "sleeptokenpassword"},
    ],
    "teams": [
        {"name": "Blue Team", "members": ["thundergod", "metalgeek"]},
        {"name": "Gold Team", "members": ["zerocool", "crashoverride", "sleeptoken"]},
    ],
    "activities": [
        {"user": "thundergod", "activity_type": "Cycling", "duration": timedelta(hours=1)},
        {"user": "metalgeek", "activity_type": "Crossfit", "duration": timedelta(hours=2)},
        {"user": "zerocool", "activity_type": "Running", "duration": timedelta(hours=1, minutes=30)},
        {"user": "crashoverride", "activity_type": "Strength", "duration": timedelta(minutes=30)},
        {"user": "sleeptoken", "activity_type": "Swimming", "duration": timedelta(hours=1, minutes=15)},
    ],
    "leaderboard": [
        {"user": "thundergod", "score": 100},
        {"user": "metalgeek", "score": 90},
        {"user": "zerocool", "score": 95},
        {"user": "crashoverride", "score": 85},
        {"user": "sleeptoken", "score": 80},
    ],
    "workouts": [
        {"name": "Cycling Training", "description": "Training for a road cycling event"},
        {"name": "Crossfit", "description": "Training for a crossfit competition"},
        {"name": "Running Training", "description": "Training for a marathon"},
        {"name": "Strength Training", "description": "Training for strength"},
        {"name": "Swimming Training", "description": "Training for a swimming competition"},
    ],
}