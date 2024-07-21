from behave import step
from json_model.sample_model import *

@step('the response body should contain the title "{title}"')
def step_impl(context, title):
    SampleModel().check_json_key_title_value(context, title)
    