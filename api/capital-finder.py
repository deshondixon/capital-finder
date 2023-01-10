# http.server from standard library for handling HTTP requests
from http.server import BaseHTTPRequestHandler
# datetime from standard library for handling dates
from urllib import parse
import requests


# new subclass called handler that extends BaseHTTPRequestHandler
class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        s = self.path
        url_components = parse.urlsplit(s)
        query_string_list = parse.parse_qsl(url_components.query)
        dic = dict(query_string_list)

        if "country" in dic:
            url = "https://restcountries.com/v3.1/name/"
            r = requests.get(url + dic["country"])
            data = r.json()
            capital = data[0]["capital"][0]
            message = f"The capital of {dic['country']} is {str(capital)}."

        elif "capital" in dic:
            url = "https://restcountries.com/v3.1/capital/"
            r = requests.get(url + dic["capital"])
            data = r.json()
            country = data[0]["name"]["common"]
            message = f"{dic['capital']} is the capital of {str(country)}."
        else:
            message = "Give me a country to define the capital of please."

        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()

        self.wfile.write(message.encode())

        return
