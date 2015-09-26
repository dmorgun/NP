__author__ = 'daria'

import requests
import pytest
import json

url='http://qainterview.cogniance.com/'
payload={	"name": "Lester Kester", 	"position": "Senior QA" }
headers={'content-type': 'application/json'}

def test_get_candidates():
    r = requests.get(url+'candidates')
    assert r.status_code == 200

def test_get_candidate_by_id():
    r = requests.get(url+'candidates/40')
    assert r.status_code == 200
    response = r.json()
    print response

def test_adding_candidate():
    r = requests.post(url+'candidates', data=json.dumps(payload), headers=headers)
    assert r.status_code == 201

def test_deleting_candidate():
    r = requests.delete(url+'candidates/30')
    assert r.status_code == 200


if __name__ == '__main__':
    pytest.main([__file__, '-v'])

test_get_candidates()
test_get_candidate_by_id()
test_adding_candidate()
test_deleting_candidate()