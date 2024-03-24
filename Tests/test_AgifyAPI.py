import unittest
import sys
from unittest.mock import patch
import requests

sys.path.append('../ApiConnect')

from EstimateAge import AgifyAPI


class TestAgifyAPI(unittest.TestCase):

    @patch('requests.get')
    def test_get_estimated_age_success(self, mock_get):
        """
        Tests successful retrieval of estimated age from the API.

        This test mocks the `requests.get` function to simulate a successful API response
        with a status code of 200 and a valid JSON response containing the age key.
        """
        # Mock the requests.get function to return a successful response
        mock_response = mock_get.return_value
        mock_response.status_code = 200
        mock_response.json.return_value = {'age': 35}

        # Create an AgifyAPI instance
        api = AgifyAPI('Carl')

        # Call get_estimated_age and assert the returned value
        estimated_age = api.get_estimated_age()
        self.assertEqual(estimated_age, 35)

    @patch('requests.get')
    def test_get_estimated_age_status_code_error(self, mock_get):
        """
        Tests handling of non-200 status code from the API.

        This test mocks the `requests.get` function to simulate a non-200 status code
        (404 in this case) from the API. It verifies that the `get_estimated_age` function
        handles the exception raised by `requests.get` and returns None.
        """
        # Mock the requests.get function to return a non-200 status code
        mock_response = mock_get.return_value
        mock_response.status_code = 404
        mock_response.raise_for_status.side_effect = requests.exceptions.RequestException('Request failed')

        # Create an AgifyAPI instance
        api = AgifyAPI('Paul')

        # Call get_estimated_age and assert None is returned
        estimated_age = api.get_estimated_age()
        self.assertIsNone(estimated_age)

    @patch('requests.get')
    def test_get_estimated_age_json_error(self, mock_get):
        """
        Tests handling of invalid JSON response from the API.

        This test mocks the `requests.get` function to simulate an invalid JSON response
        from the API. It verifies that the `get_estimated_age` function handles the `ValueError`
        raised when parsing the JSON and returns None.
        """
        # Mock the requests.get function to return an invalid JSON response
        mock_response = mock_get.return_value
        mock_response.status_code = 200
        mock_response.json.side_effect = ValueError('Invalid JSON data')

        # Create an AgifyAPI instance
        api = AgifyAPI('James')

        # Call get_estimated_age and assert None is returned
        estimated_age = api.get_estimated_age()
        self.assertIsNone(estimated_age)


if __name__ == '__main__':
    unittest.main()