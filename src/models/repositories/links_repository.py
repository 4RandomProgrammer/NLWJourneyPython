from typing import List, Tuple

import psycopg2


class LinksRepository:
	def __init__(self, conn: psycopg2.extensions.connection) -> None:
		self.__conn = conn

	def registry_link(self, links_infos: dict) -> None:
		cursor = self.__conn.cursor()
		query = """
                INSERT INTO "NLWJourney".links
                    (id, trip_id, link, title)
                VALUES ('%(id)s', '%(trip_id)s','%(link)s', '%(title)s')
        """ % (
			links_infos
		)
		cursor.execute(query)
		self.__conn.commit()

	def find_links_from_trip(self, trip_id: str) -> List[Tuple]:
		cursor = self.__conn.cursor()

		query = f"""SELECT * FROM "NLWJourney".links WHERE trip_id = '{trip_id}'"""
		cursor.execute(query)
		links = cursor.fetchall()

		return links
