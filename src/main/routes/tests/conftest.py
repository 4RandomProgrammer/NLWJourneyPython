from src.main.server.server import app

import pytest
from pytest_mock import MockFixture
import uuid

@pytest.fixture
def trip_to_create_info():
    return {
            "destination":"Joinville",
            "start_date":"12/07/2024",
            "end_date":"17/07/2024",
            "owner_name":"Fernando",
            "owner_email": "trips@email.com",
            "emails_to_invite":[]
        }

@pytest.fixture
def client():
    app.config.update({"TESTING": True})

    with app.test_client() as client:
        yield client