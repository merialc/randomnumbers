import random
from pprint import pprint

import requests


def send_message(req):
    prepped = req.prepare()
    session = requests.Session()
    response = session.send(prepped)
    return response



for i in range(10):
    r2 = requests.Request(
        method="POST",
        url='http://localhost:3000/tasks',
        json={
            'name': 'rn:' + str(random.random())

        }
    )
    send_message(r2)

