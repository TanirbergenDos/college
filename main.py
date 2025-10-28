import git
import os
import random
import sys

EMOJIS = ["🚀", "🧠", "🔧", "🔥", "💻", "✨", "🧑‍💻", "🔍", "⚡"]

def get_random_emoji():
    return random.choice(EMOJIS)

def check_for_todo_in_files(repo_path):
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
                except Exception as e:
                    print(f"⚠️ Не удалось прочитать файл {file_path}: {e}")
    return todo_files

def commit_changes_with_emoji_and_todo_check(repo_path, commit_message):
    repo = git.Repo(repo_path)
    todos = check_for_todo_in_files(repo_path)
    if todos:
        print("\n🚫 Коммит отменён! Найдены комментарии TODO:\n")
        for file_path, line_number, line_text in todos:
            print(f"  📄 {file_path}:{line_number} → {line_text}")
        print("\nУдалите или выполните TODO перед коммитом.\n")
        sys.exit(1)
    repo.git.add(A=True)
    message_with_emoji = f"{commit_message} {get_random_emoji()}"
    repo.index.commit(message_with_emoji)
    print(f"✅ Коммит выполнен с сообщением: {message_with_emoji}")
    origin = repo.remote(name='origin')
    try:
        origin.push()
        print("📤 Изменения успешно отправлены в удалённый репозиторий.")
    except git.GitCommandError:
        current_branch = repo.active_branch.name
        repo.git.push('--set-upstream', 'origin', current_branch)
        print(f"🌿 Установлена upstream-ветка для {current_branch} и выполнен push.")

if __name__ == "__main__":
    repo_path = r"C:\Users\Администратор\Desktop\2810"
    commit_message = "Добавил новую функцию"
    commit_changes_with_emoji_and_todo_check(repo_path, commit_message)
