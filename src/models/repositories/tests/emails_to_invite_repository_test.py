import uuid
from datetime import datetime, timedelta

import pytest

from src.models.repositories.trips_repository import TripsRepository
from src.models.settings.db_connection_handler import db_connection_handler

from ..emails_to_invite_repository import EmailsToInviteRepository

db_connection_handler.connect()


class TestEmailRepository:
	def test_registry_email(self, email_id, trip_id, result_email):
		conn = db_connection_handler.get_connection()
		emails_to_invite_repository = EmailsToInviteRepository(conn)
		trip_repository = TripsRepository(conn)

		trips_infos = {
			"id": trip_id,
			"destination": "Osasco",
			"start_date": datetime.strptime("02-01-2024", "%d-%m-%Y"),
			"end_date": datetime.strptime("02-01-2024", "%d-%m-%Y") + timedelta(days=5),
			"owner_name": "Osvaldo",
			"owner_email": "osvaldo@email.com",
		}

		email_info = {
			"id": email_id,
			"trip_id": trip_id,
			"email": "olamundo@email.com",
		}

		trip_repository.create_trip(trips_infos=trips_infos)
		emails_to_invite_repository.registry_email(emails_infos=email_info)
		emails = emails_to_invite_repository.find_emails_from_trip(trip_id)

		assert result_email == emails

	def test_find_emails_from_trip(self, trip_id, email_id, result_email):
		conn = db_connection_handler.get_connection()
		emails_to_invite_repository = EmailsToInviteRepository(conn)
		trip_repository = TripsRepository(conn)

		trips_infos = {
			"id": trip_id,
			"destination": "Osasco",
			"start_date": datetime.strptime("02-01-2024", "%d-%m-%Y"),
			"end_date": datetime.strptime("02-01-2024", "%d-%m-%Y") + timedelta(days=5),
			"owner_name": "Osvaldo",
			"owner_email": "osvaldo@email.com",
		}

		email_info = {
			"id": email_id,
			"trip_id": trip_id,
			"email": "olamundo@email.com",
		}

		trip_repository.create_trip(trips_infos=trips_infos)
		emails_to_invite_repository.registry_email(emails_infos=email_info)

		emails = emails_to_invite_repository.find_emails_from_trip(trip_id)

		assert isinstance(emails, list)
		assert isinstance(emails[0], tuple)
		assert result_email == emails
