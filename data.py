import requests

request = requests.get(url="https://opentdb.com/api.php?amount=10&type=boolean")
request.raise_for_status()
question_data = request.json()
