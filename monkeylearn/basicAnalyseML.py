""" This module integrates the MonkeyLearn API to analyse the data
Requires internet connectivity 
Need to install monkeylearn library
To install:
-> pip install monkeylearn
"""

from monkeylearn import MonkeyLearn
 
ml = MonkeyLearn('<<Your API key here>>')
data = ['Customer support team is great, super helpful!', 'The UI is super confusing']
model_id = '<<Insert model ID here>>' # use this if you have trained your own model
result = ml.classifiers.classify(model_id, data)
 
print(result.body)

"""
The output woud be as follows

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