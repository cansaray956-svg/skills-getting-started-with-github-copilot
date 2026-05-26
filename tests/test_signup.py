"""Tests for signup endpoint using AAA (Arrange-Act-Assert) pattern."""

import pytest


class TestSignupForActivity:
    """Tests for POST /activities/{activity_name}/signup endpoint."""

    def test_signup_returns_200(self, client, valid_activity, sample_email):
        """Test that signup returns status 200 on success."""
        # Arrange
        endpoint = f"/activities/{valid_activity}/signup"
        params = {"email": sample_email}
        
        # Act
        response = client.post(endpoint, params=params)
        
        # Assert
        assert response.status_code == 200

    def test_signup_returns_success_message(self, client, valid_activity, sample_email):
        """Test that signup returns a success message."""
        # Arrange
        endpoint = f"/activities/{valid_activity}/signup"
        params = {"email": sample_email}
        
        # Act
        response = client.post(endpoint, params=params)
        data = response.json()
        
        # Assert
        assert "message" in data
        assert sample_email in data["message"]
        assert valid_activity in data["message"]

    def test_signup_adds_participant(self, client, valid_activity, sample_email):
        """Test that signup actually adds the participant to the activity."""
        # Arrange
        endpoint = f"/activities/{valid_activity}/signup"
        params = {"email": sample_email}
        
        # Act
        client.post(endpoint, params=params)
        response = client.get("/activities")
        activities = response.json()
        
        # Assert
        assert sample_email in activities[valid_activity]["participants"]

    def test_signup_nonexistent_activity_returns_404(self, client, sample_email):
        """Test that signing up for a nonexistent activity returns 404."""
        # Arrange
        activity_name = "Nonexistent Club"
        endpoint = f"/activities/{activity_name}/signup"
        params = {"email": sample_email}
        
        # Act
        response = client.post(endpoint, params=params)
        
        # Assert
        assert response.status_code == 404

    def test_signup_duplicate_signup_returns_400(self, client, valid_activity):
        """Test that signing up twice returns 400."""
        # Arrange
        email = "michael@mergington.edu"
        endpoint = f"/activities/{valid_activity}/signup"
        params = {"email": email}
        
        # Act
        response = client.post(endpoint, params=params)
        
        # Assert
        assert response.status_code == 400
        assert "already signed up" in response.json()["detail"]

    def test_signup_multiple_activities(self, client, sample_email):
        """Test that a student can sign up for multiple activities."""
        # Arrange
        activities_to_join = ["Chess Club", "Programming Class", "Art Studio"]
        
        # Act - Sign up for each activity
        for activity in activities_to_join:
            response = client.post(
                f"/activities/{activity}/signup",
                params={"email": sample_email}
            )
            assert response.status_code == 200
        
        response = client.get("/activities")
        data = response.json()
        
        # Assert - Verify student is in all activities
        for activity in activities_to_join:
            assert sample_email in data[activity]["participants"]
