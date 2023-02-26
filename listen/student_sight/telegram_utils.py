import requests


class sight_bot():
    def __init__(self):
        self.token = '6189029678:AAGBTb0tXthQtQqjittOsGCW8FglN8qxDEY'  ## bot token 
        self.chatID = '1413414282'  ## https://medium.com/@ManHay_Hong/how-to-create-a-telegram-bot-and-send-messages-with-python-4cf314d9fa3e

    def send_message(self, message):
        send_text = 'https://api.telegram.org/bot' + self.token + '/sendMessage?chat_id=' + self.chatID + '&parse_mode=Markdown&text=' + message

        response = requests.get(send_text)

        return response.json()
