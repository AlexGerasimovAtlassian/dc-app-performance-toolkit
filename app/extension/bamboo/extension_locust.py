import re
from locustio.common_utils import init_logger, bamboo_measure, run_as_specific_user  # noqa F401

logger = init_logger(app_type='bamboo')


@bamboo_measure("locust_generate_lighthouse_events_action")
@run_as_specific_user(username='admin', password='i2fhvn.h8NOstjtTXUHLQlrX')  # run as specific user
def app_specific_action(locust):
    r = locust.get('/rest/lighthouse/1.0/alerts/create', catch_response=True)  # call app-specific GET endpoint
    content = r.content.decode('utf-8')   # decode response content

    assert 'success' in content  # assertion after POST request
