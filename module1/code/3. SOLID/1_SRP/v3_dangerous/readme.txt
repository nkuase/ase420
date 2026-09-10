This version demonstrates an SRP code smell:
To persist data with an external framework (simulated by jsonlibrary),
the Employee domain class was modified to import jsonlibrary and use @jsonlibrary.jsonserializable.
This couples Employee directly to a third-party persistence dependency, violating SRP. 