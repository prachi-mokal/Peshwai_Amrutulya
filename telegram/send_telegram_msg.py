import requests

def send_notif_to_telegram(content,telegram_id,channel_id):
    resp = requests.get(

        'https://api.telegram.org/bot' + str(telegram_id) + '/sendMessage?chat_id=' + str(
            channel_id) + '&text=' + content + "&parse_mode=html")
    print(resp.status_code)