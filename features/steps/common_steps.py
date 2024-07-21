from behave import step
from common_helpers.common_methods import CommonMethods

@step('I send a GET request to "{endpoint}"')
def step_impl(context, endpoint):
    CommonMethods().send_get_request(context, endpoint)

@step('I send a AUTH GET request to "{endpoint}"')
def step_impl(context, endpoint):
    username = context.config.userdata.get('username')
    password = context.config.userdata.get('password')
    CommonMethods().send_get_request_auth(context, endpoint, username, password)

@step('I send a POST request to "{endpoint}" with body:')
def step_impl(context, endpoint):
    CommonMethods().send_post_request(context, endpoint, context.text)

@step('I send a AUTH POST request to "{endpoint}" with body:')
def step_impl(context, endpoint):
    username = context.config.userdata.get('username')
    password = context.config.userdata.get('password')
    CommonMethods().send_post_request_auth(context, endpoint, context.text, username, password)

@step('I send a PUT request to "{endpoint}" with body:')
def step_impl(context, endpoint):
    CommonMethods().send_put_request(endpoint, context.text)

@step('I send a AUTH PUT request to "{endpoint}" with body:')
def step_impl(context, endpoint):
    username = context.config.userdata.get('username')
    password = context.config.userdata.get('password')
    CommonMethods().send_put_request_auth(context, endpoint, context.text, username, password)

@step('I send a PATCH request to "{endpoint}" with body:')
def step_impl(context, endpoint):
    CommonMethods().send_patch_request(context, endpoint, context.text)

@step('I send a AUTH PATCH request to "{endpoint}" with body:')
def step_impl(context, endpoint):
    username = context.config.userdata.get('username')
    password = context.config.userdata.get('password')
    CommonMethods().send_patch_request_auth(context, endpoint, context.text, username, password)

@step('I send a DELETE request to "{endpoint}"')
def step_impl(context, endpoint):
    CommonMethods().send_delete_request(context, endpoint)

@step('I send a AUTH DELETE request to "{endpoint}"')
def step_impl(context, endpoint):
    username = context.config.userdata.get('username')
    password = context.config.userdata.get('password')
    CommonMethods().send_delete_request_auth(context, endpoint, username, password)

@step('the response status should be {status_code:d}')
def step_impl(context, status_code):
    CommonMethods().check_response_status(context, status_code)
