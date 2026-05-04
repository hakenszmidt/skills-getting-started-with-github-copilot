import pytest
from httpx import AsyncClient
from src.app import app

@pytest.mark.asyncio
async def test_get_activities():
    # Arrange
    async with AsyncClient(app=app, base_url="http://test") as ac:
        # Act
        response = await ac.get("/activities")
    # Assert
    assert response.status_code == 200
    assert isinstance(response.json(), dict)

@pytest.mark.asyncio
async def test_signup_and_unregister():
    # Arrange
    test_email = "testuser@mergington.edu"
    activity = "Chess Club"
    async with AsyncClient(app=app, base_url="http://test") as ac:
        # Act: Sign up
        signup_resp = await ac.post(f"/activities/{activity}/signup?email={test_email}")
        # Assert: Signup
        assert signup_resp.status_code in (200, 400)
        # Act: Unregister
        unregister_resp = await ac.delete(f"/activities/{activity}/signup?email={test_email}")
        # Assert: Unregister
        assert unregister_resp.status_code in (200, 404)
