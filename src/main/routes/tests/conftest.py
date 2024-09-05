import uuid

import pytest
from pytest_mock import MockFixture

from src.main.server.server import app


@pytest.fixture
def trip_to_create_info():
	return {
		"destination": "Joinville",
		"start_date": "2024-07-12",
		"end_date": "2024-07-17",
		"owner_name": "Fernando",
		"owner_email": "trips@email.com",
		"emails_to_invite": [],
	}


@pytest.fixture
def link_to_create_info():
	return {"url": "Hotel.com", "title": "Hotel"}


@pytest.fixture
def activity_to_create_info():
	return {"title": "Jogar um freefas", "occurs_at": "2024-04-14"}


@pytest.fixture
def participant_to_create_info():
	return {"email": ["teste@email.com"], "name": "Giocondo das Trevas"}


@pytest.fixture
def client():
	app.config.update({"TESTING": True})

	with app.test_client() as client:
		yield client
