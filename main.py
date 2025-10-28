import git
import random

# Список эмодзи
emojis = ["🚀", "🧠", "🔧", "🔥", "💻", "✨", "🧑‍💻", "🔍", "⚡"]

# Функция для выбора случайного эмодзи
def get_random_emoji():
    return random.choice(emojis)

# Функция для добавления и коммита изменений в Git
def commit_changes_with_emoji(repo_path, commit_message):
    # Инициализация репозитория
    repo = git.Repo(repo_path)
    
    # Добавление всех изменений в staging area
    repo.git.add(A=True)
    
    # Формирование финального сообщения с эмодзи
    message_with_emoji = f"{commit_message} {get_random_emoji()}"
    
    # Выполнение commit с сообщением
    repo.index.commit(message_with_emoji)
    
    # Пуш изменений на удаленный репозиторий
    origin = repo.remote(name='origin')
    origin.push()

    print(f"Коммит выполнен с сообщением: {message_with_emoji}")

# Пример использования
repo_path = r"C:\Users\Администратор\Desktop\2810"  # Замените на путь к вашему репозиторию
commit_message = "Исправил баг"  # Замените на ваше сообщение

commit_changes_with_emoji(repo_path, commit_message)
