from typing import Dict, Tuple
from src.models.repositories.links_repository import LinksRepository
import uuid


class LinkFinder:
	def __init__(self, link_repository: LinksRepository) -> None:
		self.__link_repository = link_repository

	def find(self, trip_id: str) -> Tuple:
		try:
			links = self.__link_repository.find_links_from_trip(trip_id)
			formatted_links = []
			for link in links:
				formatted_links.append({"id": link[0], "url": link[2], "title": link[3]})
			return {"body": {"links": formatted_links}, "status_code": 200}

		except Exception as exception:
			return {
				"body": {"error": "Bad Request", "message": str(exception)},
				"status_code": 400,
			}
