class TestCounterSmoke(unittest.TestCase):

    def setUp(self):
        connection_string = os.environ["HomerunCosmosConnection"]
        self.table_service_client = TableServiceClient.from_connection_string(conn_str=connection_string)
        self.table = table_service_client.get_table_client("homeruntable")

    def test_trigger_increments_db(self):
        # Step 1: independently read the CURRENT value, before touching the API at all
        before_entity = self.table.get_entity(partition_key="Yordan", row_key="Astros")
        before_count = before_entity["Homeruns"]

        # Step 2: hit the actual deployed Function URL like a real visitor would
        response = requests.get("https://homerunfunction-ajbbb0hpe7ajahdt.eastus-01.azurewebsites.net/api/theshow")

        # Step 3: check the HTTP response itself
        self.assertEqual(response.status_code, 200)

        # Step 4: independently re-read the table AGAIN — fresh query, not the response, not a mutated local dict
        after_entity = self.table.get_entity(partition_key="Yordan", row_key="Astros")
        after_count = after_entity["Homeruns"]

        # Step 5: assert the DB actually moved by exactly 1
        self.assertEqual(after_count, before_count + 1)

    