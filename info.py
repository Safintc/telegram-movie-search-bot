import re
from os import environ

id_pattern = re.compile(r'^.\d+$')

# Bot information
SESSION = environ.get('SESSION', 'Media_search')
USER_SESSION = environ.get('USER_SESSION', 'API_ID')
API_ID = int(environ['21116415'])
API_HASH = environ['8e23c9d97d71d525741e33f6b3584f45']
BOT_TOKEN = environ['8420823401:AAF5SEgM6vwB5swBQRbUjfdlmU6RU8nv5yY']
USERBOT_STRING_SESSION = environ.get('BQFCNf8AcDnhigMZt643WfY7AyghykoeTug7yZiUK6o6HPAbxBjN5CrB1lJy5OYs6nzhvYnJLtKqhI9JgorINnGnGX1KIjlQGugPLnVTOa-uZpfbe9_HVP1fgHJKfrmsafZCjjUdO9xYIlHNyFyM62KbNtTQ-b-Uis5bHWH289jcmiynpy-FngQubWuuHs4nM4UThcpcfKJoreT0bB05jecX3nzRvf2Dtd9KdyGNrRKSnDvaPejWJWAiZxuwb74cAaar9z6Z5jNQGftaVW4xFrNApKDSaWMtl7hG_J0ROLWJhsjB14quwnptiHyqDKW0fW83d63iZHmrZryNPBkxLdknTAyJWAAAAABQP9SDAA')

# Bot settings
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', False))

# Admins, Channels & Users
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ['21116415'].split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ[' -1002577824824'].split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '21116415').split()]
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
auth_channel = environ.get('-1002584950282')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else auth_channel

# MongoDB information
DATABASE_URI = environ['mongodb+srv://safin:x0EwcqRWeyafnQIo@cluster0.1qpfh4t.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0']
DATABASE_NAME = environ['Cluster0']
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')

# Messages
default_start_msg = """
**Hi, I'm Media Search bot**

Here you can search files in inline mode. Just press following buttons and start searching.
"""

START_MSG = environ.get('START_MSG', default_start_msg)
SHARE_BUTTON_TEXT = 'Checkout {username} for searching files'
INVITE_MSG = environ.get('INVITE_MSG', 'Please join @.... to use this bot')
