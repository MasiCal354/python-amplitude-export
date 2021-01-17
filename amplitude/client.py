from io import BytesIO
import requests, zipfile, gzip, json

def parse_newline_delimited_json(js):
    return json.loads("[" + js.replace("\n", ",")[:-1] + "]")

class AmplitudeExport:
    URL = "https://amplitude.com/api/2/export"

    def __init__(self, api_key, secret_key):
        self.__auth = (api_key, secret_key)

    def _response_handler(self, response):
        response.raise_for_status()
        content = zipfile.ZipFile(BytesIO(response.content))
        data = list()
        for name in content.namelist():
            with content.open(name) as gz:
                js = gzip.decompress(gz.read()).decode()
                data.extend(parse_newline_delimited_json(js))
        return data

    def export(self, start, end):
        params = {
            "start": start,
            "end": end
        }
        response = requests.get(
            self.URL,
            params=params,
            auth=self.get_auth(),
            stream=True
        )
        return self._response_handler(response)

    def get_auth(self):
        return self.__auth