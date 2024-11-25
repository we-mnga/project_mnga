import json

def serialize_chain(chain):
    return json.dumps([block.to_dict() for block in chain], indent=4)

def deserialize_chain(serialized_chain):
    return json.loads(serialized_chain)
