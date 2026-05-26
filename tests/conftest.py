"""Pytest configuration and shared fixtures for the FastAPI tests."""

import pytest
from fastapi.testclient import TestClient
from src.app import app, activities


@pytest.fixture
def client():
    """Create a test client for the FastAPI application."""
    return TestClient(app)


@pytest.fixture(autouse=True)
def reset_activities():
    """Reset activities to initial state before each test."""
    # Store original state
    original_state = {
        "Chess Club": {
            "description": "Learn strategies and compete in chess tournaments",
            "schedule": "Fridays, 3:30 PM - 5:00 PM",
            "max_participants": 12,
            "participants": ["michael@mergington.edu", "daniel@mergington.edu"]
        },
        "Programming Class": {
            "description": "Learn programming fundamentals and build software projects",
            "schedule": "Tuesdays and Thursdays, 3:30 PM - 4:30 PM",
            "max_participants": 20,
            "participants": ["emma@mergington.edu", "sophia@mergington.edu"]
        },
        "Gym Class": {
            "description": "Physical education and sports activities",
            "schedule": "Mondays, Wednesdays, Fridays, 2:00 PM - 3:00 PM",
            "max_participants": 30,
            "participants": ["john@mergington.edu", "olivia@mergington.edu"]
        },
        "Basketball Team": {
            "description": "Competitive basketball team for students interested in basketball",
            "schedule": "Mondays and Wednesdays, 4:00 PM - 5:30 PM",
            "max_participants": 15,
            "participants": ["lucas@mergington.edu", "ryan@mergington.edu"]
        },
        "Tennis Club": {
            "description": "Tennis skills development and friendly matches",
            "schedule": "Tuesdays and Fridays, 3:30 PM - 5:00 PM",
            "max_participants": 10,
            "participants": ["isabella@mergington.edu"]
        },
        "Art Studio": {
            "description": "Explore painting, drawing, and sculpture techniques",
            "schedule": "Mondays and Thursdays, 3:30 PM - 5:00 PM",
            "max_participants": 15,
            "participants": ["grace@mergington.edu", "zoe@mergington.edu"]
        },
        "Music Ensemble": {
            "description": "Play musical instruments and perform in ensemble groups",
            "schedule": "Wednesdays and Fridays, 4:00 PM - 5:00 PM",
            "max_participants": 20,
            "participants": ["alexander@mergington.edu"]
        },
        "Debate Team": {
            "description": "Develop public speaking and argumentation skills through competitive debate",
            "schedule": "Tuesdays and Thursdays, 4:30 PM - 5:30 PM",
            "max_participants": 16,
            "participants": ["noah@mergington.edu", "ava@mergington.edu"]
        },
        "Science Club": {
            "description": "Conduct experiments and explore advanced scientific concepts",
            "schedule": "Mondays and Fridays, 4:00 PM - 5:00 PM",
            "max_participants": 18,
            "participants": ["liam@mergington.edu"]
        }
    }
    
    # Reset activities dictionary
    activities.clear()
    activities.update(original_state)
    
    yield


@pytest.fixture
def sample_email():
    """Sample email for testing."""
    return "test.student@mergington.edu"


@pytest.fixture
def valid_activity():
    """Valid activity name for testing."""
    return "Chess Club"
