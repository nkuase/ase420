import json

def jsonserializable(cls):
    """Simulated third-party serialization decorator.
    Marks the class as serializable by the external framework.
    """
    cls._json_serializable = True
    return cls

def save(filename, obj):
    """Simulated third-party serialization save function.
    Requires that the target object/class be marked with @jsonserializable.
    """
    is_serializable = getattr(obj, "_json_serializable", False) or getattr(type(obj), "_json_serializable", False)
    if not is_serializable:
        raise TypeError(
            f"Object of type {type(obj).__name__} has no serializable attributes. "
            "Decorate class with @jsonserializable"
        )

    data = {
        "name": getattr(obj, "name", ""),
        "salary": getattr(obj, "salary", 0)
    }
    with open(filename, "w") as f:
        json.dump(data, f, indent=2)
