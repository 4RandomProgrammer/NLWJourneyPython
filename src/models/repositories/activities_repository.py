from typing import Dict, List, Tuple
import psycopg2


class ActivitiesRepository:
    def __init__(self, conn: psycopg2.extensions.connection) -> None:
        self.__conn = conn

    def registry_activity(self, activity_info: Dict) -> None:
        cursor = self.__conn.cursor()
        query = """
                INSERT INTO "NLWJourney".activities
                    (id, trip_id, title, occurs_at)
                VALUES ('%(id)s', '%(trip_id)s','%(title)s', '%(occurs_at)s')
        """ % (
            activity_info
        )
        cursor.execute(query)
        self.__conn.commit()

    def find_activities_from_trip(self, trip_id:str) -> List[Tuple]:
        cursor = self.__conn.cursor()

        query = f"""
            SELECT *
            FROM "NLWJourney".activities as a
            WHERE a.trip_id = '{trip_id}'
        """
        cursor.execute(query)
        participants = cursor.fetchall()

        return participants

