import json


with open('C:\Users\Manish Kumar\Documents\SDM PROD\JSON\SOURCE\instruments.json') as json_file:
    source_data =json.load(json_file)

with open('C:\Users\Manish Kumar\Documents\SDM PROD\JSON\TARGET\instruments.json') as json_file:
    target_data =json.load(json_file)


def compare_extra_fields(target_record, source_record):
    if(target_record['fields']['name'] == source_record['fields']['name']) & \
            (target_record['fields']['facility'] == source_record['fields']['facility']):
        return True



data = []
for inst in source_data:
    # find if source instrument exist in target
    match = next((item for item in target_data if item['pk'] == inst['pk']), None)
    if match is None:
        print ("instrument with pk %s not found in target db" % (inst['pk']))
        data.append(inst)
    else:
        # check if name and facilty_id matches
        is_match = compare_extra_fields(match, inst)
        if is_match:
            print ("Skipping ... Instrument with PK %s exist in source and target dbs " % inst['pk'])
        else:
            print ("need to create record with different id")


# write to file
with open('instrument_data_to_serialize.json', 'w') as outfile:
    json.dump(data, outfile)


