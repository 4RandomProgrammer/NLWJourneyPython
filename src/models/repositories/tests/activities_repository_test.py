from datetime import datetime, timedelta
import	pytest

from src.models.repositories.activities_repository import ActivitiesRepository
from src.models.repositories.trips_repository import TripsRepository
from src.models.settings.db_connection_handler import db_connection_handler

class TestActivitiesRepository:
    def test_registry_link(self, trip_id, activity_id, result_activity):
        conn = db_connection_handler.get_connection()

        trip_repository = TripsRepository(conn)
        activities_repository = ActivitiesRepository(conn)

        trips_infos = {
            "id": trip_id,
            "destination": "Osasco",
            "start_date": datetime.strptime("02-01-2024", "%d-%m-%Y"),
            "end_date": datetime.strptime("02-01-2024", "%d-%m-%Y") + timedelta(days=5),
            "owner_name": "Osvaldo",
            "owner_email": "osvaldo@email.com",
        }

        activity_info = {
            "id": activity_id,
            "trip_id": trip_id,
            "title": "Festa na Floresta",
            "occurs_at": datetime.strptime("02-01-2024", "%d-%m-%Y") + timedelta(days=2),
        }

        trip_repository.create_trip(trips_infos=trips_infos)
        activities_repository.registry_activity(activity_info)
        activities = activities_repository.find_activities_from_trip(trip_id)
        
        assert result_activity == activities
    
    def test_find_activities_from_trip(self, trip_id, activity_id, result_activity):
        conn = db_connection_handler.get_connection()

        trip_repository = TripsRepository(conn)
        activities_repository = ActivitiesRepository(conn)

        trips_infos = {
            "id": trip_id,
            "destination": "Osasco",
            "start_date": datetime.strptime("02-01-2024", "%d-%m-%Y"),
            "end_date": datetime.strptime("02-01-2024", "%d-%m-%Y") + timedelta(days=5),
            "owner_name": "Osvaldo",
            "owner_email": "osvaldo@email.com",
        }

        activity_info = {
            "id": activity_id,
            "trip_id": trip_id,
            "title": "Festa na Floresta",
            "occurs_at": datetime.strptime("02-01-2024", "%d-%m-%Y") + timedelta(days=2),
        }

        trip_repository.create_trip(trips_infos=trips_infos)
        activities_repository.registry_activity(activity_info)
        activities = activities_repository.find_activities_from_trip(trip_id)
        
        assert result_activity == activities
        assert isinstance(activities, list)
        assert isinstance(activities[0], tuple)
