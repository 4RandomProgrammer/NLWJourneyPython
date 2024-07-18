import uuid
from datetime import datetime, timedelta

import pytest


@pytest.fixture
def trip_id():
	return str(uuid.uuid4())


@pytest.fixture
def email_id():
	return str(uuid.uuid4())


@pytest.fixture
def link_id():
	return str(uuid.uuid4())


@pytest.fixture
def participant_id():
	return str(uuid.uuid4())


@pytest.fixture
def activity_id():
	return str(uuid.uuid4())


@pytest.fixture
def result_trip(trip_id):
	return (
		trip_id,
		"Osasco",
		datetime.strptime("02-01-2024", "%d-%m-%Y"),
		datetime.strptime("02-01-2024", "%d-%m-%Y") + timedelta(days=5),
		"Osvaldo",
		"osvaldo@email.com",
		None,
	)


@pytest.fixture
def result_trip_with_confirmation(trip_id):
	return (
		trip_id,
		"Osasco",
		datetime.strptime("02-01-2024", "%d-%m-%Y"),
		datetime.strptime("02-01-2024", "%d-%m-%Y") + timedelta(days=5),
		"Osvaldo",
		"osvaldo@email.com",
		1,
	)


@pytest.fixture
def result_link(trip_id, link_id):
	return [(link_id, trip_id, "aaaaaa.com", "Hotel")]


@pytest.fixture
def result_email(trip_id, email_id):
	return [(email_id, trip_id, "olamundo@email.com")]


@pytest.fixture
def result_participant(participant_id):
	return [(participant_id, "Heraldo", None, "heraldo@email.com")]


@pytest.fixture
def result_confirmed_participant(participant_id):
	return [(participant_id, "Heraldo", 1, "heraldo@email.com")]


@pytest.fixture
def result_activity(activity_id, trip_id):
	return [
		(
			activity_id,
			trip_id,
			"Festa na Floresta",
			datetime.strptime("02-01-2024", "%d-%m-%Y") + timedelta(days=2),
		)
	]
