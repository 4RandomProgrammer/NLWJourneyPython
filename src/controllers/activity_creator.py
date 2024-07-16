import uuid
from typing import Dict
from src.models.repositories.activities_repository import ActivitiesRepository


class ActivityCreator:
	def __init__(self, activities_repository: ActivitiesRepository) -> None:
		self.__activities_repository = activities_repository

	def create(self, body: Dict, trip_id: str) -> Dict:
		try:
			id = str(uuid.uuid4())

			activity_info = {
				"id": id,
				"trip_id": trip_id,
				"title": body.get("title"),
				"occurs_at": body.get("occurs_at"),
			}

			self.__activities_repository.registry_activity(activity_info)

			return {"body": {"activity_id": id}, "status_code": 201}

		except Exception as exception:
			return {
				"body": {"error": "Bad Request", "message": str(exception)},
				"status_code": 400,
			}
