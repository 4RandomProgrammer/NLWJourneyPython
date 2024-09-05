from typing import Dict

from src.models.repositories.trips_repository import TripsRepository


class TripUpdater:
	def __init__(self, trip_repository: TripsRepository) -> None:
		self.__trips_repository = trip_repository

	def update(self, body: Dict, trip_id: str) -> Dict:
		try:
			self.__trips_repository.update_trip_destination_and_date(
				trip_id, body["destination"], body["start_date"], body["end_date"]
			)

			return {"body": None, "status_code": 204}
		except Exception as exception:
			return {
				"body": {"error": "Bad Request", "message": str(exception)},
				"status_code": 400,
			}
