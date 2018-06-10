import requests

from gql import Client as GraphQLClient, gql
from gql.transport.requests import RequestsHTTPTransport

class FlashbotClient:
    def __init__(self, apiKey, url='http://localhost:9020/graphql'):
        self.apiKey = apiKey
        self.gqlClient = GraphQLClient(
            retries=3,
            transport=RequestsHTTPTransport(url=url)
        )

    def bots(self):
        pass

    def bot(self, id):
        pass

