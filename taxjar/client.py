import requests


class Client:
    def __init__(self, token, *args, **kwargs):
        self.API_BASE = 'https://api.taxjar.com/v2'
        self.token = token
        self.headers = {}

        self.set_auth_header()

    def set_auth_header(self):
        self.headers['Authorization'] = 'Bearer {}'.format(self.token)

    def GET_request(self, endpoint, in_url_parameter=None, extra_parameters=None):
        if in_url_parameter:
            url = "{}/{}/{}".format(self.API_BASE, endpoint, in_url_parameter)
        else:
            url = "{}/{}/".format(self.API_BASE, endpoint)

        return requests.get(url, params=extra_parameters, headers=self.headers)

    def POST_request(self, endpoint, in_url_parameter, post_parameter):
        return requests.post("{}/{}/{}".format(self.API_BASE, endpoint, in_url_parameter), data=post_parameter, headers=self.headers)
