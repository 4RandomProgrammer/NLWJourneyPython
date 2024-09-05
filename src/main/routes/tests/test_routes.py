import pytest


class TestAppRoutes:
	def test_call_endpoint(self, trip_to_create_info, client):
		response = client.post("/trips", json=trip_to_create_info)
		print(response.json)
		assert response.status_code == 201

	def test_can_create_trip(self, trip_to_create_info, client):
		create_trip_response = client.post("/trips", json=trip_to_create_info)

		assert create_trip_response.status_code == 201

		create_trip_data = create_trip_response.json
		id = create_trip_data.get("id")

		get_trip_response = client.get(f"/trips/{id}")

		assert get_trip_response.status_code == 201

		get_trip_data = get_trip_response.json
		trip = get_trip_data.get("trip")

		assert trip["destination"] == trip_to_create_info["destination"]
		assert trip["status"] == None
		assert trip["starts_at"] == "Fri, 12 Jul 2024 00:00:00 GMT"
		assert trip["ends_at"] == "Wed, 17 Jul 2024 00:00:00 GMT"

	def test_confirm_trip(self, trip_to_create_info, client):
		create_trip_response = client.post("/trips", json=trip_to_create_info)

		assert create_trip_response.status_code == 201

		create_trip_data = create_trip_response.json
		id = create_trip_data.get("id")

		confirm_trip_response = client.get(f"/trips/{id}/confirm")

		assert confirm_trip_response.status_code == 204
		assert confirm_trip_response.data == b""

		get_trip_response = client.get(f"/trips/{id}")

		get_trip_data = get_trip_response.json
		trip = get_trip_data.get("trip")

		assert trip["destination"] == trip_to_create_info["destination"]
		assert trip["status"] == 1
		assert trip["starts_at"] == "Fri, 12 Jul 2024 00:00:00 GMT"
		assert trip["ends_at"] == "Wed, 17 Jul 2024 00:00:00 GMT"

	def test_create_link(self, client, trip_to_create_info, link_to_create_info):
		create_trip_response = client.post("/trips", json=trip_to_create_info)

		assert create_trip_response.status_code == 201

		create_trip_data = create_trip_response.json
		trip_id = create_trip_data.get("id")

		create_link_response = client.post(
			f"/trips/{trip_id}/links", json=link_to_create_info
		)

		assert create_link_response.status_code == 201

		get_links_response = client.get(f"/trips/{trip_id}/links")

		assert get_links_response.status_code == 200

		get_link_data = get_links_response.json
		all_links = get_link_data.get("links")

		assert all_links[0]["title"] == link_to_create_info["title"]
		assert all_links[0]["url"] == link_to_create_info["url"]

	def test_create_activity(self, client, trip_to_create_info, activity_to_create_info):
		create_trip_response = client.post("/trips", json=trip_to_create_info)
		date = activity_to_create_info.get("occurs_at")

		assert create_trip_response.status_code == 201

		create_trip_data = create_trip_response.json
		trip_id = create_trip_data.get("id")

		create_activity_response = client.post(
			f"/trips/{trip_id}/activities", json=activity_to_create_info
		)

		assert create_activity_response.status_code == 201

		get_activities_response = client.get(f"/trips/{trip_id}/activities")

		assert get_activities_response.status_code == 200

		get_activities_data = get_activities_response.json

		all_activities = get_activities_data.get("activities")

		assert all_activities[0]["activities"][0]["title"] == activity_to_create_info["title"]
		assert all_activities[0]["activities"][0]["occurs_at"] == "00:00"

	def test_create_participant(
		self, client, trip_to_create_info, participant_to_create_info
	):
		create_trip_response = client.post("/trips", json=trip_to_create_info)

		assert create_trip_response.status_code == 201

		create_trip_data = create_trip_response.json
		trip_id = create_trip_data.get("id")

		create_participant_response = client.post(
			f"/trips/{trip_id}/invites", json=participant_to_create_info
		)

		assert create_participant_response.status_code == 200

		get_participant_response = client.get(f"/trips/{trip_id}/participants")

		assert get_participant_response.status_code == 200

		get_participants_data = get_participant_response.json

		all_participants = get_participants_data.get("participants")

		assert all_participants[0]["name"] == participant_to_create_info["name"]
		assert all_participants[0]["email"] == participant_to_create_info["email"][0]
		assert all_participants[0]["is_confirmed"] == None

	def test_confirm_participant(
		self, client, trip_to_create_info, participant_to_create_info
	):
		create_trip_response = client.post("/trips", json=trip_to_create_info)

		assert create_trip_response.status_code == 201

		create_trip_data = create_trip_response.json
		trip_id = create_trip_data.get("id")

		create_participant_response = client.post(
			f"/trips/{trip_id}/invites", json=participant_to_create_info
		)

		assert create_participant_response.status_code == 200

		create_participant_data = create_participant_response.json
		participant_id = create_participant_data.get("participant_id")[0]

		confirm_participant_response = client.get(f"/participants/{participant_id}/confirm")

		assert confirm_participant_response.status_code == 204
		assert confirm_participant_response.data == b""

		get_participant_response = client.get(f"/trips/{trip_id}/participants")

		assert get_participant_response.status_code == 200

		get_participants_data = get_participant_response.json

		all_participants = get_participants_data.get("participants")

		assert all_participants[0]["name"] == participant_to_create_info["name"]
		assert all_participants[0]["email"] == participant_to_create_info["email"][0]
		assert all_participants[0]["is_confirmed"] == 1
