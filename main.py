import git
import os
import random

# -----------------------------
# Настройки и данные
# -----------------------------
EMOJIS = ["🚀", "🧠", "🔧", "🔥", "💻", "✨", "🧑‍💻", "🔍", "⚡"]

def get_random_emoji():
    """Возвращает случайный эмодзи для коммита."""
    return random.choice(EMOJIS)

# -----------------------------
# Проверка на TODO
# -----------------------------
def check_for_todo_in_files(repo_path):
    """Проверяет файлы в репозитории на наличие комментариев TODO."""
    todo_files = []
    for root, _, files in os.walk(repo_path):
        for file in files:
            if file.endswith(".py"):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, "r", encoding="utf-8") as f:
                        for line_number, line in enumerate(f, start=1):
                            if "TODO" in line:
                                todo_files.append((file_path, line_number, line.strip()))
                except Exception:
                    pass  # Пропускаем файлы, которые не удается прочитать
    return todo_files

# -----------------------------
# Основная функция Git-автоматизации
# -----------------------------
def commit_changes_with_emoji(repo_path, commit_message):
    repo = git.Repo(repo_path)

    # Проверка на TODO перед коммитом
    todos = check_for_todo_in_files(repo_path)
    if todos:
        print("⚠️ Обнаружены комментарии TODO в коде:")
        for file_path, line_number, line_text in todos:
            print(f"  {file_path}:{line_number} → {line_text}")
        print("Проверьте TODO перед коммитом!\n")

    # Добавляем изменения
    repo.git.add(A=True)

    # Формируем сообщение коммита с эмодзи
    message_with_emoji = f"{commit_message} {get_random_emoji()}"

    # Выполняем коммит
    repo.index.commit(message_with_emoji)
    print(f"✅ Коммит выполнен с сообщением: {message_with_emoji}")

    # Пушим изменения
    origin = repo.remote(name='origin')
    try:
        origin.push()
    except git.GitCommandError:
        current_branch = repo.active_branch.name
        repo.git.push('--set-upstream', 'origin', current_branch)
        print(f"Установлена upstream-ветка для {current_branch} и выполнен push.")

# -----------------------------
# Пример использования
# -----------------------------
if __name__ == "__main__":
    repo_path = r"C:\Users\Администратор\Desktop\2810"  # Укажите путь к вашему репозиторию
    commit_message = "Добавил новую функцию"
    commit_changes_with_emoji(repo_path, commit_message)
