from discord import SyncWebhook
from credentials import webhook_url


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.

    def __init__(self):
        self.webhook = SyncWebhook.from_url(webhook_url)

    def send_notification(self, message):
        self.webhook.send(message)
        print("Sent message to Discord channel")
