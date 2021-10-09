from dataclasses import dataclass
from typing import List, Optional

import requests

DATAHUB_URL = 'http://datahub.yc.pbd.ai:9002/'
LOGIN = 'datahub'
PASSWORD = 'datahub'
GET_DATASET_Q = """
query getSearchResults($input: SearchInput!) {
  search(input: $input) {
    start
    count
    total
    searchResults {
      entity {
        urn
        type
        ... on Dataset {
          name
          origin
          description
          uri
          platform {
            name
            info {
              logoUrl
            }
          }
          properties {
            customProperties {
              key
              value
            }
          }
          ownership {
            ...ownershipFields
          }
        }
      }
    }
    facets {
      field
      aggregations {
        value
        count
      }
    }
  }
}
fragment ownershipFields on Ownership {
  owners {
    owner {
      ... on CorpUser {
        urn
        type
        username
        info {
          active
          displayName
          title
          email
          firstName
          lastName
          fullName
        }
      }
    }
    type
  }
  lastModified {
    time
  }
}
"""
GET_DATASET_VAR = {
  "input": {
    "count": None,
    "filters": None,
    "query": None,
    "start": None,
    "type": "DATASET"
  }
}


@dataclass
class DataHubUser:
    urn: str
    username: str
    email: str
    first_name: str
    last_name: str


@dataclass
class DataHubDataset:
    urn: str
    name: str
    description: Optional[str]
    logo_uri: Optional[str]
    owners: List[DataHubUser]


class DataHubError(Exception):

    def __init__(self, msg):
        self.msg = msg


class DataHubConnector:

    def __init__(self):
        self._session = requests.Session()
        self.is_logged_in = False

    def _login(self):
        self._session.post(f'{DATAHUB_URL}logIn', json={"username": LOGIN, "password": PASSWORD})

    def _search_parse(self, response):
        search_results = response['data']['search']['searchResults']
        result = []
        for search_result in search_results:
            entity = search_result['entity']
            datahub_dataset = DataHubDataset(
                urn=entity["urn"],
                name=entity["name"],
                description=entity["description"],
                logo_uri=entity["platform"].get("info", {}).get("logoUrl"),
                owners=[]
            )
            raw_owners = entity["ownership"]["owners"]
            for raw_owner in raw_owners:
                datahub_user = DataHubUser(
                    urn=raw_owner["owner"]["urn"],
                    username=raw_owner["owner"]["username"],
                    email=raw_owner["owner"]["info"]["email"],
                    first_name=raw_owner["owner"]["info"]["firstName"],
                    last_name=raw_owner["owner"]["info"]["lastName"]
                )
                datahub_dataset.owners.append(datahub_user)
            result.append(datahub_dataset)
        return result



    def search(self, query='*', offset=0, limit=3):
        if not self.is_logged_in:
            self._login()
        vars = {
              "input": {
                "count": limit,
                "filters": None,
                "query": query,
                "start": offset,
                "type": "DATASET"
              }
            }

        r = self._session.post(f'{DATAHUB_URL}api/v2/graphql', json={"query": GET_DATASET_Q, "variables": vars})
        if r.status_code != 200:
            raise DataHubError(f"Ответ от datahub {r.status_code} {r.text}")
        return self._search_parse(r.json())

if __name__ == '__main__':
    connector = DataHubConnector()
    print(connector.search())