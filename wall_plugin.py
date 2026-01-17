# wall_plugin.py
"""
Exteragram Wall Plugin
This plugin integrates a wall feature allowing for comments, synchronization
with user accounts, and seamless UI updates.
"""

import json
import requests

class ExteragramWall:
    def __init__(self):
        self.posts = []

    def add_post(self, user_id, content):
        """Add a new post to the wall."""
        post = {
            'user_id': user_id,
            'content': content,
            'comments': []
        }
        self.posts.append(post)
        self.sync_wall()

    def add_comment(self, post_id, user_id, comment):
        """Add a comment to a post."""
        if post_id < len(self.posts):
            self.posts[post_id]['comments'].append({
                'user_id': user_id,
                'comment': comment
            })
            self.sync_wall()

    def sync_wall(self):
        """Synchronize wall data with the server."""
        # Example server endpoint
        server_url = "https://yourserver.com/api/wall"
        response = requests.post(server_url, json=self.posts)
        return response.status_code

    def get_wall(self):
        """Fetch the wall posts and comments."""
        return json.dumps(self.posts, indent=4)

# Example usage
if __name__ == "__main__":
    wall = ExteragramWall()
    wall.add_post("user123", "This is my first post!")
    wall.add_comment(0, "user456", "Great post!")
    print(wall.get_wall())
