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
        id = create_trip_data.get('id')
        
        get_trip_response = client.get(f"/trips/{id}")

        get_trip_data = get_trip_response.json
        trip = get_trip_data.get('trip')
        
        assert trip['destination'] == trip_to_create_info['destination']
        assert trip['status'] == None
        assert trip['starts_at'] == 'Fri, 12 Jul 2024 00:00:00 GMT'
        assert trip['ends_at'] == 'Wed, 17 Jul 2024 00:00:00 GMT'

    def test_confirm_trip(self, trip_to_create_info, client):
        create_trip_response = client.post("/trips", json=trip_to_create_info)

        assert create_trip_response.status_code == 201

        create_trip_data = create_trip_response.json
        id = create_trip_data.get('id')
        
        confirm_trip_response = client.get(f"/trips/{id}/confirm")
        
        assert confirm_trip_response.status_code == 204
        assert confirm_trip_response.data == b''

        get_trip_response = client.get(f"/trips/{id}")

        get_trip_data = get_trip_response.json
        trip = get_trip_data.get('trip')
        
        assert trip['destination'] == trip_to_create_info['destination']
        assert trip['status'] == 1
        assert trip['starts_at'] == 'Fri, 12 Jul 2024 00:00:00 GMT'
        assert trip['ends_at'] == 'Wed, 17 Jul 2024 00:00:00 GMT'

    @pytest.mark.skip
    def test_create_link(self, client):
        create_trip_response = client.post("/trips", json=trip_to_create_info)

        assert create_trip_response.status_code == 201

        create_trip_data = create_trip_response.json
        id = create_trip_data.get('id')
        
        get_trip_response = client.get(f"/trips/{id}")

        get_trip_data = get_trip_response.json
        trip = get_trip_data.get('trip')
        
        assert trip['destination'] == trip_to_create_info['destination']
        assert trip['status'] == None
        assert trip['starts_at'] == 'Fri, 12 Jul 2024 00:00:00 GMT'

    @pytest.mark.skip
    def test_create_activity(self, client):
        create_trip_response = client.post("/trips", json=trip_to_create_info)

        assert create_trip_response.status_code == 201

        create_trip_data = create_trip_response.json
        id = create_trip_data.get('id')
        
        get_trip_response = client.get(f"/trips/{id}")

        get_trip_data = get_trip_response.json
        trip = get_trip_data.get('trip')
        
        assert trip['destination'] == trip_to_create_info['destination']
        assert trip['status'] == None
        assert trip['starts_at'] == 'Fri, 12 Jul 2024 00:00:00 GMT'
    
    @pytest.mark.skip
    def test_create_participant(self, client):
        create_trip_response = client.post("/trips", json=trip_to_create_info)

        assert create_trip_response.status_code == 201

        create_trip_data = create_trip_response.json
        id = create_trip_data.get('id')
        
        get_trip_response = client.get(f"/trips/{id}")

        get_trip_data = get_trip_response.json
        trip = get_trip_data.get('trip')
        
        assert trip['destination'] == trip_to_create_info['destination']
        assert trip['status'] == None
        assert trip['starts_at'] == 'Fri, 12 Jul 2024 00:00:00 GMT'
        
    @pytest.mark.skip
    def test_confirm_participant(self,client):
        pass