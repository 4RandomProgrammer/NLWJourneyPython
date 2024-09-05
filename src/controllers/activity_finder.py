import uuid
from typing import Dict, Tuple

from src.models.repositories.activities_repository import ActivitiesRepository


class ActivityFinder:
	def __init__(self, activities_repository: ActivitiesRepository) -> None:
		self.__activities_repository = activities_repository

	def find(self, trip_id: str) -> Tuple:
		try:
			activity_dict = {}
			activities = self.__activities_repository.find_activities_from_trip(trip_id)
			formatted_activities = []

			for activity in activities:
				date = activity[3].strftime("%Y-%m-%d")

				if not activity_dict.get(date):
					activity_dict[date] = []

				activity_dict[date].append(
					{
						"id": activity[0],
						"title": activity[2],
						"occurs_at": activity[3].strftime("%H:%M"),
					}
				)

			for date_key in activity_dict:
				formatted_activities.append(
					{"date": date_key, "activities": activity_dict[date_key]}
				)

			return {"body": {"activities": formatted_activities}, "status_code": 200}

		except Exception as exception:
			return {
				"body": {"error": "Bad Request", "message": str(exception)},
				"status_code": 400,
			}
