import json

def fromJSON(json_file):
    """load json with utf8 encoding"""
    with open(str(json_file),"r", encoding='utf8') as fp:
        return json.load(fp)