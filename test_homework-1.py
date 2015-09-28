__author__ = 'daria'

import requests
import pytest
import json

url='http://qainterview.cogniance.com/'
payload={	"name": "Chupacabra", 	"position": "Senior QA" }
payload_no_position = { "name": "GuyThatCanDoAnything" }
payload_blank_name = { "name": "", "position": "CEO" }
headers={'content-type': 'application/json'}

def test_get_candidates():
    r = requests.get(url+'candidates')
    assert r.status_code == 200

def test_adding_candidate():
    r = requests.post(url+'candidates', data=json.dumps(payload), headers=headers)
    assert r.status_code == 201
    response = r.json()
    # print response
    global new_id # declaring a global variable so that it can be accessible from other functions
    new_id = response['candidate']['id']
    # print new_id

# This test fails, it's a bug
def test_get_candidate_by_id():
    r = requests.get(url+'candidates/'+str(new_id)) # converting int to str
    assert r.status_code == 200, "Return status code 200 if candidate with provided id exists"
    response = r.json()
    print response
    assert response['candidate']['id'] == new_id, "Assert that candidate id received from server matches the requested candidate id"

def test_get_candidate_by_id_that_does_not_exist():
    r = requests.get(url+'candidates/'+str(new_id+100500))
    assert r.status_code == 404, "Return status code 404 if candidate with provided id doesn't exist"
    response = r.json()
    # print response
    error = response['error']
    assert error == "Incorrect URL"
    # print error

def test_deleting_candidate():
    r = requests.delete(url+'candidates/'+str(new_id))
    assert r.status_code == 200, "Return status code 200 if candidate has been successfully deleted"

def test_adding_candidate_without_body_and_name():
    r = requests.post(url+'candidates')
    assert r.status_code == 400, "Return status code 400 if header Content-Type AND name are absent"

def test_adding_candidate_without_position():
    r = requests.post(url+'candidates', data=json.dumps(payload_no_position), headers=headers)
    assert r.status_code == 201

# This test fails and I think it's a bug
def test_adding_candidate_with_blank_name():
    r = requests.post(url+'candidates', data=json.dumps(payload_blank_name), headers=headers)
    assert r.status_code == 400, "Return status code 400 if user tries to add candidate with blank 'name'"

def

if __name__ == '__main__':
    pytest.main([__file__, '-v'])
