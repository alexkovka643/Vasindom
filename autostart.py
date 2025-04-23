import requests
import time

# Заменить на свой ATERNOS_SESSION
cookies = {
    "ATERNOS_SESSION": "tIDSgnEMrWjpusHMDhCzM2FIpNbs6irXEVGFslO9nf0DbQDKY6eS95DfMqFYHEEzKhbQoqrulzXxnu91Mfxn2hs5LU0ao3EUoXLt"
}

headers = {
    "User-Agent": "Mozilla/5.0"
}

# Получаем информацию о сервере
r = requests.get("https://aternos.org/servers/", cookies=cookies, headers=headers)
if "server" not in r.text:
    print("Не удалось получить доступ к серверу. Проверь ATERNOS_SESSION.")
    exit()

print("Успешно вошли. Ищем ID сервера...")

# Запрос для получения стартовой страницы сервера
r = requests.get("https://aternos.org/server/", cookies=cookies, headers=headers)
if "btn btn-success" not in r.text:
    print("Сервер, возможно, уже запущен или в очереди.")
    exit()

print("Отправляем запрос на запуск сервера...")

# Отправляем POST-запрос на старт
start = requests.post("https://aternos.org/server/start", cookies=cookies, headers=headers)
if start.status_code == 200:
    print("Сервер запускается.")
else:
    print("Ошибка при запуске сервера.")
