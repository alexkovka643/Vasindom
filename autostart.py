import requests
import time

# Вставь свой ATERNOS_SESSION
cookies = {
    "ATERNOS_SESSION": "tIDSgnEMrWjpusHMDhCzM2FIpNbs6irXEVGFslO9nf0DbQDKY6eS95DfMqFYHEEzKhbQoqrulzXxnu91Mfxn2hs5LU0ao3EUoXLt"
}

headers = {
    "User-Agent": "Mozilla/5.0"
}

# Шаг 1: Получение токена и ID сервера
def get_server_info():
    r = requests.get("https://aternos.org/servers/", cookies=cookies, headers=headers)
    if "id" not in r.text:
        print("Не удалось получить сервер. Проверь cookie.")
        return None, None
    server_id = r.text.split("id: \"")[1].split("\"")[0]
    token = r.text.split("token: \"")[1].split("\"")[0]
    return server_id, token

# Шаг 2: Запуск сервера
def start_server(server_id, token):
    start_url = f"https://aternos.org/server/start"
    response = requests.post(
        start_url,
        cookies=cookies,
        headers=headers,
        data={"id": server_id, "token": token}
    )
    if response.status_code == 200:
        print("Сервер запускается!")
    else:
        print("Не удалось запустить сервер.")

# Запуск
if __name__ == "__main__":
    server_id, token = get_server_info()
    if server_id and token:
        start_server(server_id, token)
    else:
        print("Ошибка получения данных о сервере.")
