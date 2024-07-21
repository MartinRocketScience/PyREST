import os
import requests

def before_all(context):
    """
    This function is executed before all tests. It sets up the base URL, default headers,
    and retrieves the OAuth2 token.
    
    :param context: Behave context object
    """
    context.base_url = os.getenv('BASE_URL', 'https://jsonplaceholder.typicode.com/')
    context.headers = {"Content-Type": "application/json"}
    # context.oauth_token = get_oauth_token()

def after_all(context):
    """
    This function is executed after all tests.
    
    :param context: Behave context object
    """
    # Any cleanup operations can be performed here
    pass
    
def before_scenario(context, scenario):
    """
    This function is executed before each scenario.
    
    :param context: Behave context object
    :param scenario: Current scenario being executed
    """
    context.scenario_name = scenario.name

def after_scenario(context, scenario):
    """
    This function is executed after each scenario.
    
    :param context: Behave context object
    :param scenario: Current scenario that has been executed
    """
    pass

def get_oauth_token():
    """
    This function retrieves an OAuth2 token using client credentials.
    
    :return: OAuth2 token as a string
    """
    url = os.getenv('OAUTH_TOKEN_URL', 'http://yourauthserver.com/oauth/token')
    payload = {
        'grant_type': 'client_credentials',
        'client_id': os.getenv('CLIENT_ID', 'your_client_id'),
        'client_secret': os.getenv('CLIENT_SECRET', 'your_client_secret')
    }
    response = requests.post(url, data=payload)
    response.raise_for_status()  # Raise an exception for HTTP errors
    token = response.json().get('access_token')
    return token
