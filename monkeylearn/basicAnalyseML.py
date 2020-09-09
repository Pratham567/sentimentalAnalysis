""" This module integrates the MonkeyLearn API to analyse the data
Requires internet connectivity 
Need to install monkeylearn library
To install:
-> pip install monkeylearn
"""

from monkeylearn import MonkeyLearn
from scraper import data 
# ml = MonkeyLearn('<<Your API key here>>')
# The following API Key is public token provided by monkeylearn server
# Each user of monkeylearn has his own API token
# which he can easily get from monkeylearn website
ml = MonkeyLearn('7eda867d9f75c6dc1379a9798af8bb47d993ffaa')

# Statements to be analysed, in the format of a list where each element is a statement
# data = ['Customer support team is great, super helpful!', 'The UI is super confusing']

# model_id = '<<Insert model ID here>>' # use this if you have trained your own model
model_id = 'cl_pi3C7JiL' # this is public model provided by monkeylearn server

# Applying the model
result = ml.classifiers.classify(model_id, data)
"""
The output woud be as follows (result.body)

[{
    'text': 'Customer support team is great',
    'classifications': [{
        'tag_name': 'Positive',
        'confidence': 0.923,
        'tag_id': 41767129
    }],
    'error': False,
    'external_id': None
}, {
    'text': 'The UI is super confusing',
    'classifications': [{
        'tag_name': 'Negative',
        'confidence': 0.916,
        'tag_id': 41767178
    }],
    'error': False,
    'external_id': None
}]
"""

# Printing the result to stdout
res = result.body
for elem in res:
    print("\n%s\t%s"% (elem['text'], elem['classifications']))
    # print(elem)
print("\n")