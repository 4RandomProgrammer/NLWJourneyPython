import pytest
import uuid
from datetime import datetime, timedelta
from ..trips_repository import TripsRepository
from src.models.settings.db_connection_handler import db_connection_handler

db_connection_handler.connect()

class TestTripRepository:
	def test_create_trip(self, trip_id, result_trip):
		conn = db_connection_handler.get_connection()
		trip_repository = TripsRepository(conn)

		trips_infos = {
			"id": trip_id,
			"destination": "Osasco",
			"start_date": datetime.strptime("02-01-2024", "%d-%m-%Y"),
			"end_date": datetime.strptime("02-01-2024", "%d-%m-%Y") + timedelta(days=5),
			"owner_name": "Osvaldo",
			"owner_email": "osvaldo@email.com",
		}

		trip_repository.create_trip(trips_infos=trips_infos)
		trip = trip_repository.find_trip_by_id(trip_id)
		assert result_trip == trip


	def test_update_trip_status(self, trip_id, result_trip_with_confirmation):
		conn = db_connection_handler.get_connection()
		trip_repository = TripsRepository(conn)
		trips_infos = {
			"id": trip_id,
			"destination": "Osasco",
			"start_date": datetime.strptime("02-01-2024", "%d-%m-%Y"),
			"end_date": datetime.strptime("02-01-2024", "%d-%m-%Y") + timedelta(days=5),
			"owner_name": "Osvaldo",
			"owner_email": "osvaldo@email.com",
		}

		trip_repository.create_trip(trips_infos=trips_infos)
		trip_repository.update_trip_status(trip_id)
		trip = trip_repository.find_trip_by_id(trip_id)
		
		assert result_trip_with_confirmation == trip
