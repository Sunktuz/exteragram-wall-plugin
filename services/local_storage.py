# Local Storage Service

class LocalStorage:
    def __init__(self, filename='local_storage.json'):
        self.filename = filename
        self.data = self.load()

    def load(self):
        try:
            with open(self.filename, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return {}
        except json.JSONDecodeError:
            return {}

    def save(self):
        with open(self.filename, 'w') as f:
            json.dump(self.data, f)

    def get(self, key):
        return self.data.get(key)

    def set(self, key, value):
        self.data[key] = value
        self.save()