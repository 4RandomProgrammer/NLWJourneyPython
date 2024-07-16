from typing import Dict, Tuple
from src.models.repositories.activities_repository import ActivitiesRepository
import uuid


class ActivityFinder:
	def __init__(self, activities_repository: ActivitiesRepository) -> None:
		self.__activities_repository = activities_repository

	def find(self, trip_id: str) -> Tuple:
		try:
			activities = self.__activities_repository.find_activities_from_trip(trip_id)
			formatted_activities = []
			for activity in activities:
				formatted_activities.append(
					{"id": activities[0], "title": activities[2], "occurs_at": activities[3]}
				)
			return {"body": {"activities": formatted_activities}, "status_code": 200}

		except Exception as exception:
			return {
				"body": {"error": "Bad Request", "message": str(exception)},
				"status_code": 400,
			}
