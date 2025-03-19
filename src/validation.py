from jsonschema import validate, ValidationError

schema = {
    "type": "object",
    "properties": {
        "name": {"type": "string", "minLength": 1},
        "os": {"type": "string", "enum": ["Ubuntu", "CentOS"]},
        "cpu": {"type": "string", "pattern": "^[0-9]+$"},
        "ram": {"type": "string", "pattern": "^[0-9]+GB$"}
    },
    "required": ["name", "os", "cpu", "ram"]
}

def validate_instance(instance):
    """Validate the instance data using jsonschema."""
    try:
        validate(instance, schema)
        return True
    except ValidationError as e:
        print(f" Validation error: {e.message}")
        return False
