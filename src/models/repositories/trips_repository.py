from typing import Tuple

import psycopg2


class TripsRepository:
	def __init__(self, conn: psycopg2.extensions.connection) -> None:
		self.__conn = conn

	def create_trip(self, trips_infos: dict) -> None:
		cursor = self.__conn.cursor()
		query = """
                INSERT INTO "NLWJourney".trips
                    (id, destination, start_date, end_date, owner_name, owner_email)
                VALUES ('%(id)s', '%(destination)s','%(start_date)s', '%(end_date)s', '%(owner_name)s', '%(owner_email)s')
        """ % (
			trips_infos
		)
		cursor.execute(query)
		self.__conn.commit()

	def find_trip_by_id(self, trip_id: str) -> Tuple:
		cursor = self.__conn.cursor()

		query = f"""SELECT * FROM "NLWJourney".trips WHERE id = '{trip_id}'"""
		cursor.execute(query)
		trip = cursor.fetchone()

		return trip

	def update_trip_status(self, trip_id: str) -> None:
		cursor = self.__conn.cursor()

		query = f"""
            UPDATE "NLWJourney".trips 
                SET status = 1
            WHERE 
                id = '{trip_id}'
        """
		cursor.execute(query)

		self.__conn.commit()

	def update_trip_destination_and_date(self, trip_id: str, destination: str, date: str) -> None:
		cursor = self.__conn.cursor()

		query = f"""
            UPDATE "NLWJourney".trips 
                SET status = 1
            WHERE 
                id = '{trip_id}'
        """
		cursor.execute(query)

		self.__conn.commit()
