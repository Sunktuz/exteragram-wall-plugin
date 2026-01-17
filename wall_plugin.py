import os
import json
import requests

# Configuration
GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')  # GitHub token for authentication
REPO_OWNER = 'Sunktuz'
REPO_NAME = 'exteragram-wall-plugin'

# Initialization
class WallPlugin:
    def __init__(self):
        self.data = {}
        self.load_data()
        self.sync_with_github()

    def load_data(self):
        # Load data from a local file or any source
        try:
            with open('data.json', 'r') as f:
                self.data = json.load(f)
        except FileNotFoundError:
            self.data = {}  # Start with empty data

    def save_data(self):
        # Save data to a local file
        with open('data.json', 'w') as f:
            json.dump(self.data, f)

    def add_data(self, entry):
        self.data.append(entry)
        self.save_data()
        self.sync_with_github()

    def sync_with_github(self):
        url = f'https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/contents/data.json'
        headers = {'Authorization': f'token {GITHUB_TOKEN}', 'Content-Type': 'application/json'}
        response = requests.put(url, headers=headers, json={
            'message': 'Sync data',
            'content': self.encode_data(),
            'sha': self.get_file_sha()
        })
        if response.status_code == 201:
            print('Data synced successfully.')
        else:
            print('Failed to sync data:', response.json())

    def encode_data(self):
        return base64.b64encode(json.dumps(self.data).encode('utf-8')).decode('utf-8')

    def get_file_sha(self):
        url = f'https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/contents/data.json'
        response = requests.get(url, headers={'Authorization': f'token {GITHUB_TOKEN}'})
        if response.status_code == 200:
            return response.json()['sha']
        return None

# Example of plugin usage
if __name__ == '__main__':
    plugin = WallPlugin()  
    plugin.add_data({'message': 'Hello, world!'})  # Add sample data
