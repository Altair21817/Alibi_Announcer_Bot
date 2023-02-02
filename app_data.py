from dotenv import load_dotenv
import os

load_dotenv()

TELEGRAM_BOT_TOKEN: str = os.getenv('TELEGRAM_BOT_TOKEN')
VK_TOKEN: str = os.getenv('VK_TOKEN')
VK_TOKEN_ADMIN: str = os.getenv('VK_ADMIN_TOKEN')
VK_USER_ME: str = os.getenv('VK_USER_ME')
VK_CHAT_TARGET: int = 40914100
VK_GROUP_TARGET: int = 40914100
