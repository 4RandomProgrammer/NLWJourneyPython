import uuid
from datetime import datetime, timedelta

import pytest

from src.models.settings.db_connection_handler import db_connection_handler

from ..links_repository import LinksRepository
from ..trips_repository import TripsRepository

db_connection_handler.connect()


class TestLinkRepository:
	def test_registry_link(self, trip_id, link_id, result_link):
		conn = db_connection_handler.get_connection()

		trip_repository = TripsRepository(conn)
		links_repository = LinksRepository(conn)

		trips_infos = {
			"id": trip_id,
			"destination": "Osasco",
			"start_date": datetime.strptime("02-01-2024", "%d-%m-%Y"),
			"end_date": datetime.strptime("02-01-2024", "%d-%m-%Y") + timedelta(days=5),
			"owner_name": "Osvaldo",
			"owner_email": "osvaldo@email.com",
		}

		link_info = {
			"id": link_id,
			"trip_id": trip_id,
			"link": "aaaaaa.com",
			"title": "Hotel",
		}

		trip_repository.create_trip(trips_infos=trips_infos)
		links_repository.registry_link(links_infos=link_info)
		links = links_repository.find_links_from_trip(trip_id)

		assert result_link == links

	def test_find_links_from_trip(self, link_id, trip_id, result_link):
		conn = db_connection_handler.get_connection()
		links_repository = LinksRepository(conn)

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

		links_repository = LinksRepository(conn)

		link_info = {
			"id": link_id,
			"trip_id": trip_id,
			"link": "aaaaaa.com",
			"title": "Hotel",
		}

		links_repository.registry_link(links_infos=link_info)

		links = links_repository.find_links_from_trip(trip_id)

		assert isinstance(links, list)
		assert isinstance(links[0], tuple)
		assert result_link == links
