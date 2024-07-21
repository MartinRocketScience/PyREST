import requests
from requests.auth import HTTPBasicAuth

class CommonMethods:
    def send_get_request(self, context, endpoint):
        """
        Sends a GET request to the specified endpoint.
        
        Args:
            context: Behave context object that holds the response.
            endpoint (str): The endpoint to send the GET request to.
        """
        context.response = requests.get(context.base_url + endpoint)

    def send_get_request_auth(self, context, endpoint, username, password):
        """
        Sends an authenticated GET request to the specified endpoint.
        
        Args:
            context: Behave context object that holds the response.
            endpoint (str): The endpoint to send the GET request to.
            username (str): The username for authentication.
            password (str): The password for authentication.
        """
        context.response = requests.get(context.base_url + endpoint, auth=HTTPBasicAuth(username, password))

    def send_post_request(self, context, endpoint, body):
        """
        Sends a POST request to the specified endpoint with the provided body.
        
        Args:
            context: Behave context object that holds the response.
            endpoint (str): The endpoint to send the POST request to.
            body (dict): The body of the POST request.
        """
        context.response = requests.post(context.base_url + endpoint, json=body)

    def send_post_request_auth(self, context, endpoint, body, username, password):
        """
        Sends an authenticated POST request to the specified endpoint with the provided body.
        
        Args:
            context: Behave context object that holds the response.
            endpoint (str): The endpoint to send the POST request to.
            body (dict): The body of the POST request.
            username (str): The username for authentication.
            password (str): The password for authentication.
        """
        context.response = requests.post(context.base_url + endpoint, json=body, auth=HTTPBasicAuth(username, password))

    def send_put_request(self, context, endpoint, body):
        """
        Sends a PUT request to the specified endpoint with the provided body.
        
        Args:
            context: Behave context object that holds the response.
            endpoint (str): The endpoint to send the PUT request to.
            body (dict): The body of the PUT request.
        """
        context.response = requests.put(context.base_url + endpoint, json=body)

    def send_put_request_auth(self, context, endpoint, body, username, password):
        """
        Sends an authenticated PUT request to the specified endpoint with the provided body.
        
        Args:
            context: Behave context object that holds the response.
            endpoint (str): The endpoint to send the PUT request to.
            body (dict): The body of the PUT request.
            username (str): The username for authentication.
            password (str): The password for authentication.
        """
        context.response = requests.put(context.base_url + endpoint, json=body, auth=HTTPBasicAuth(username, password))

    def send_patch_request(self, context, endpoint, body):
        """
        Sends a PATCH request to the specified endpoint with the provided body.
        
        Args:
            context: Behave context object that holds the response.
            endpoint (str): The endpoint to send the PATCH request to.
            body (dict): The body of the PATCH request.
        """
        context.response = requests.patch(context.base_url + endpoint, json=body)

    def send_patch_request_auth(self, context, endpoint, body, username, password):
        """
        Sends an authenticated PATCH request to the specified endpoint with the provided body.
        
        Args:
            context: Behave context object that holds the response.
            endpoint (str): The endpoint to send the PATCH request to.
            body (dict): The body of the PATCH request.
            username (str): The username for authentication.
            password (str): The password for authentication.
        """
        context.response = requests.patch(context.base_url + endpoint, json=body, auth=HTTPBasicAuth(username, password))

    def send_delete_request(self, context, endpoint):
        """
        Sends a DELETE request to the specified endpoint.
        
        Args:
            context: Behave context object that holds the response.
            endpoint (str): The endpoint to send the DELETE request to.
        """
        context.response = requests.delete(context.base_url + endpoint)

    def send_delete_request_auth(self, context, endpoint, username, password):
        """
        Sends an authenticated DELETE request to the specified endpoint.
        
        Args:
            context: Behave context object that holds the response.
            endpoint (str): The endpoint to send the DELETE request to.
            username (str): The username for authentication.
            password (str): The password for authentication.
        """
        context.response = requests.delete(context.base_url + endpoint, auth=HTTPBasicAuth(username, password))

    def check_response_status(self, context, status_code):
        """
        Asserts that the response status code is equal to the specified status code.
        
        Args:
            context: Behave context object that holds the response.
            status_code (int): The expected status code of the response.
        """
        assert context.response.status_code == status_code
