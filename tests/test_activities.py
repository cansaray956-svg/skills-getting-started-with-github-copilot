"""Tests for activity-related endpoints using AAA (Arrange-Act-Assert) pattern."""

import pytest


class TestGetActivities:
    """Tests for GET /activities endpoint."""

    def test_get_activities_returns_200(self, client):
        """Test that getting activities returns status 200."""
        # Arrange
        endpoint = "/activities"
        
        # Act
        response = client.get(endpoint)
        
        # Assert
        assert response.status_code == 200

    def test_get_activities_returns_dict(self, client):
        """Test that activities are returned as a dictionary."""
        # Arrange
        endpoint = "/activities"
        
        # Act
        response = client.get(endpoint)
        data = response.json()
        
        # Assert
        assert isinstance(data, dict)

    def test_get_activities_contains_expected_activities(self, client):
        """Test that the response contains all expected activities."""
        # Arrange
        endpoint = "/activities"
        expected_activities = [
            "Chess Club",
            "Programming Class",
            "Gym Class",
            "Basketball Team",
            "Tennis Club",
            "Art Studio",
            "Music Ensemble",
            "Debate Team",
            "Science Club"
        ]
        
        # Act
        response = client.get(endpoint)
        data = response.json()
        
        # Assert
        for activity in expected_activities:
            assert activity in data

    def test_get_activities_has_required_fields(self, client):
        """Test that each activity has required fields."""
        # Arrange
        endpoint = "/activities"
        required_fields = {"description", "schedule", "max_participants", "participants"}
        
        # Act
        response = client.get(endpoint)
        data = response.json()
        
        # Assert
        for activity_name, activity_data in data.items():
            assert isinstance(activity_data, dict)
            assert required_fields.issubset(activity_data.keys())

    def test_get_activities_participants_is_list(self, client):
        """Test that participants field is a list."""
        # Arrange
        endpoint = "/activities"
        
        # Act
        response = client.get(endpoint)
        data = response.json()
        
        # Assert
        for activity_name, activity_data in data.items():
            assert isinstance(activity_data["participants"], list)
