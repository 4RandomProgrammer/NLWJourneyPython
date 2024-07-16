from datetime import datetime, timedelta
import pytest
import uuid

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
def result_trip(trip_id):
    return (
        trip_id,
        'Osasco',
        datetime.strptime("02-01-2024", "%d-%m-%Y"),
		datetime.strptime("02-01-2024", "%d-%m-%Y") + timedelta(days=5),
        'Osvaldo', 
        'osvaldo@email.com', 
        None
    )

@pytest.fixture
def result_trip_with_confirmation(trip_id):
    return (
        trip_id,
        'Osasco',
        datetime.strptime("02-01-2024", "%d-%m-%Y"),
		datetime.strptime("02-01-2024", "%d-%m-%Y") + timedelta(days=5),
        'Osvaldo', 
        'osvaldo@email.com', 
        1
    )

@pytest.fixture
def result_link(trip_id, link_id):
    return [(link_id, trip_id, 'aaaaaa.com', 'Hotel')]

@pytest.fixture
def result_email(trip_id, email_id):
    return [(email_id, trip_id, 'olamundo@email.com')]