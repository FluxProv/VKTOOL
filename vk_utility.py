import vk_api

# Функция для аутентификации и получения объекта API
def auth_vk(token):
    try:
        vk_session = vk_api.VkApi(token=token)
        vk_session.auth()
        return vk_session.get_api()
    except vk_api.AuthError as e:
        print(f"Ошибка аутентификации: {e}")
        return None

# Функция для получения информации о текущем пользователе
def get_user_info(api):
    try:
        user_info = api.users.get()
        print("Информация о текущем пользователе:")
        print(f"Имя: {user_info[0]['first_name']}")
        print(f"Фамилия: {user_info[0]['last_name']}")
        print(f"ID: {user_info[0]['id']}")
    except vk_api.VkApiError as e:
        print(f"Ошибка при получении информации о пользователе: {e}")

# Функция для отправки сообщения указанному пользователю
def send_message(api, user_id, message):
    try:
        api.messages.send(user_id=user_id, message=message)
        print(f"Сообщение отправлено пользователю с ID {user_id}.")
    except vk_api.VkApiError as e:
        print(f"Ошибка при отправке сообщения: {e}")

# Основная функция для демонстрации работы утилиты
def main():
    # Введите ваш токен доступа
    token = 'YOUR_ACCESS_TOKEN'

    # Аутентификация и получение объекта API
    api = auth_vk(token)
    if not api:
        return

    # Получение информации о текущем пользователе
    get_user_info(api)

    # Отправка приветственного сообщения
    send_message(api, user_id=123456789, message="Привет, это тестовое сообщение!")

if __name__ == "__main__":
    main()
