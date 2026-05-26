"""Tests for unregister endpoint using AAA (Arrange-Act-Assert) pattern."""

import pytest


class TestUnregisterFromActivity:
    """Tests for DELETE /activities/{activity_name}/unregister endpoint."""

    def test_unregister_returns_200(self, client, valid_activity):
        """Test that unregister returns status 200 on success."""
        # Arrange
        email = "michael@mergington.edu"
        endpoint = f"/activities/{valid_activity}/unregister"
        params = {"email": email}
        
        # Act
        response = client.delete(endpoint, params=params)
        
        # Assert
        assert response.status_code == 200

    def test_unregister_returns_success_message(self, client, valid_activity):
        """Test that unregister returns a success message."""
        # Arrange
        email = "michael@mergington.edu"
        endpoint = f"/activities/{valid_activity}/unregister"
        params = {"email": email}
        
        # Act
        response = client.delete(endpoint, params=params)
        data = response.json()
        
        # Assert
        assert "message" in data
        assert email in data["message"]
        assert valid_activity in data["message"]

    def test_unregister_removes_participant(self, client, valid_activity):
        """Test that unregister actually removes the participant."""
        # Arrange
        email = "michael@mergington.edu"
        endpoint = f"/activities/{valid_activity}/unregister"
        params = {"email": email}
        
        # Act
        response = client.delete(endpoint, params=params)
        response = client.get("/activities")
        activities = response.json()
        
        # Assert
        assert response.status_code == 200
        assert email not in activities[valid_activity]["participants"]

    def test_unregister_nonexistent_activity_returns_404(self, client, sample_email):
        """Test that unregistering from a nonexistent activity returns 404."""
        # Arrange
        activity_name = "Nonexistent Club"
        endpoint = f"/activities/{activity_name}/unregister"
        params = {"email": sample_email}
        
        # Act
        response = client.delete(endpoint, params=params)
        
        # Assert
        assert response.status_code == 404

    def test_unregister_non_participant_returns_400(self, client, valid_activity, sample_email):
        """Test that unregistering a non-participant returns 400."""
        # Arrange
        endpoint = f"/activities/{valid_activity}/unregister"
        params = {"email": sample_email}
        
        # Act
        response = client.delete(endpoint, params=params)
        
        # Assert
        assert response.status_code == 400
        assert "not signed up" in response.json()["detail"]

    def test_unregister_after_signup(self, client, valid_activity, sample_email):
        """Test the full signup and unregister flow."""
        # Arrange
        signup_endpoint = f"/activities/{valid_activity}/signup"
        unregister_endpoint = f"/activities/{valid_activity}/unregister"
        params = {"email": sample_email}
        
        # Act - Sign up
        response = client.post(signup_endpoint, params=params)
        assert response.status_code == 200
        
        # Act - Verify signup
        response = client.get("/activities")
        
        # Assert - Student is signed up
        assert sample_email in response.json()[valid_activity]["participants"]
        
        # Act - Unregister
        response = client.delete(unregister_endpoint, params=params)
        assert response.status_code == 200
        
        # Act - Verify removal
        response = client.get("/activities")
        
        # Assert - Student is removed
        assert sample_email not in response.json()[valid_activity]["participants"]
