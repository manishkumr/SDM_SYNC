import json
"""
users = User.objects.filter(id__gt=2194).order_by('id')
from django.core import serializers
json_data = serializers.serialize("json", users)
with open ('users_new.json', 'w') as users_file: 
  users_file.write(json_data)
"""

with open('C:\Users\Manish Kumar\Documents\SDM PROD\JSON\SOURCE\users_new.json') as json_file:
    source_data =json.load(json_file)

with open('C:\Users\Manish Kumar\Documents\SDM PROD\JSON\TARGET\users_new.json') as json_file:
    target_data =json.load(json_file)


def compare_extra_fields(target_record, source_record):
    if(target_record['fields']['username'] == source_record['fields']['username']) & \
            (target_record['fields']['email'] == source_record['fields']['email']):
        return True


def get_last_id(data):
    return data[-1]['pk']


data = []
last_id = get_last_id(target_data)
for user in source_data:
    # find if source instrument exist in target
    match = next((item for item in target_data if item['pk'] == user['pk']), None)
    if match is None:
        print ("user with pk %s not found in target db" % (user['pk']))
        data.append(user)
    else:
        # check if name and facilty_id matches
        is_match = compare_extra_fields(match, user)
        if is_match:
            print ("Skipping ... User with PK %s exist in source and target dbs " % user['pk'])
        else:
            print("PK conflict in user record, updating PK to next available")
            last_id = last_id + 1
            user['pk'] = last_id
            data.append(user)




# write to file
with open('user_data_to_serialize.json', 'w') as outfile:
    json.dump(data, outfile)
