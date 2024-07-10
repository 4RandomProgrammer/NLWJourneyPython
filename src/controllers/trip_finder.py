from typing import Dict
from src.models.repositories.trips_repository import TripsRepository


class TripFinder:
	def __init__(self, trip_repository: TripsRepository) -> None:
		self.__trip_repository = trip_repository

	def find_trip_detail(self, trip_id: str) -> Dict:
		try:

			trip = self.__trip_repository.find_trip_by_id(trip_id)

			if not trip:
				raise Exception("No Trip Found")

			return {
				"body": {
					"trip": {
						"id": trip[0],
						"destination": trip[1],
						"starts_at": trip[2],
						"ends_at": trip[3],
						"status": trip[6],
					},
				},
				"status_code": 201,
			}

		except Exception as exception:
			return {
				"body": {"error": "Bad Request", "message": str(exception)},
				"status_code": 400,
			}
