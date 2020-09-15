""" This module integrates the MonkeyLearn API to analyse the data
Requires internet connectivity 
No need to install monkeylearn library
This module uses python requests library to send HTTP Requests to the monkeylearn server
For more info about monkeylearn API: https://monkeylearn.com/api/v3/#introduction
"""

import requests
import json
from monkeylearn1.scraper import data

def grafana_post(data):
    """ This function sends a HTTP POST REQUEST to monkeylearn server using their public token
        The response has the basic sentiment about the statement and has confidence index.
    """
    try:
        response = requests.post("%s" % ("https://api.monkeylearn.com/v3/classifiers/cl_pi3C7JiL/classify/"),
                                 headers = {"Authorization": "Token 7eda867d9f75c6dc1379a9798af8bb47d993ffaa"},
                                 json=data)
        return response
    except:
        print("Could not connect to the monkeylearn server. Terminating POST operation...")
        raise Exception("Could not connect to the monkeylearn server. Terminating POST operation...")


# Statements to be analysed, in the format of a dict
# where the key is data and the value is a list where each element is a statement
# data = ["This is a great tool!", "Horray! I love it.", "I hate it."]
# monkeylearn supports upto 500 statements at a time

response = grafana_post({"data": data})
res_data = json.loads(response.content)
# Response Content is of type list with each element corresponding to each statement sent.
# print(response.status_code)
# print(response.text)

# Printing the result
# for elem in res_data:
#     print("\n%s\ttag: %s\tconfidence: %s"% (elem['text'], elem['classifications'][0]['tag_name'], elem['classifications'][0]['confidence']))
# print("\n")
