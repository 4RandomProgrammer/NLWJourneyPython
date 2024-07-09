import pytest
import uuid
from .links_repository import LinksRepository
from src.models.settings.db_connection_handler import db_connection_handler

db_connection_handler.connect()
trip_id = 'c36025dd-d00c-47a4-bae0-149da977fc7f'

@pytest.mark.skip(reason='Interação com o banco')
def test_registry_email():
	conn = db_connection_handler.get_connection()
	links_repository = LinksRepository(conn)

	link_info = {
		"id": str(uuid.uuid4()),
		"trip_id": trip_id,
		"link": 'aaaaaa.com',
	}

	links_repository.registry_link(links_infos=link_info)

@pytest.mark.skip(reason='Interação com o banco')
def test_find_links_from_trip():
    conn = db_connection_handler.get_connection()
    links_repository = LinksRepository(conn)
    
    links = links_repository.find_links_from_trip(trip_id)
    print(links)
