import requests
import json

WEB_URL = 'https://medium.com'

def fetch_json(url):
    res = requests.get(url)
    return clean_json_response(res)

def clean_json_response(response):
    return json.loads(response.text.split('])}while(1);</x>')[1])

def get_user_posts(id_):
    return get_paged_response(id_, 'users/' + id_, data_path=['references', 'Post'], limit=1000)

def get_author_list(id_):
    return get_paged_response(id_, 'collections/' + id_, data_path=['references', 'User'], limit=200)

def get_list_of_followings(user_id):
    next_id = False
    all_data = []
    while True:
        if next_id:
            # If this is not the first page of the followings list
            url = WEB_URL + '/_/api/users/' + user_id + '/following?limit=8&to=' + next_id
        else:
            # If this is the first page of the followings list
            url = WEB_URL + '/_/api/users/' + user_id + '/following'
        response = requests.get(url)
        response_dict = clean_json_response(response)
        payload = response_dict['payload']
        for user in payload['value']:
            all_data.append(user['username'])
        try:
            # If the "to" key is missing, we've reached the end
            # of the list and an exception is thrown
            next_id = payload['paging']['next']['to']
            if next_id == 'null':
                break
        except:
            break
    return all_data

def get_paged_response(id, api_endpoint, data_path=['references', 'User'], limit=200):
    next_id = False
    all_data = {}
    while True:
        if next_id:
            # if this is not the first page
            url = WEB_URL + '/_/api/' + api_endpoint + '/stream?limt=8&to=' + next_id
        else:
            # if this is the first page
            url = WEB_URL + '/_/api/' + api_endpoint + '/stream'
            response = requests.get(url)
            response_dict = clean_json_response(response)
            payload = response_dict['payload']
            try:
                # Break out of the loop if we hit the limit, or we reach the end of the list
                all_data.update(payload[data_path[0]][data_path[1]])
                if len(all_data) >= limit:
                    break
                next_id = payload['paging']['next']['to']
                if next_id == 'null':
                    break
            except Exception:
                break
    return all_data



