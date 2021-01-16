# Python Aamplitude Export
Python client implementation for [Amplitude Export API](https://developers.amplitude.com/docs/export-api)

```bash
pip install python-amplitude-export
```

```python
from amplitude import AmplitudeExport

API_KEY = ""
SECRET_KEY = ""

client = AmplitudeExport(API_KEY, SECRET_KEY)
data = client.export("20210101T00", "20210101T23")
```
