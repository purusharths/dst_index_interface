import json

def convert_to_dict(**kwargs):
	contents = kwargs.get('string_list')
	converted_dict = {}
	for content in contents:
		converted_dict[content[0]] = json.loads(content[1])
	return converted_dict