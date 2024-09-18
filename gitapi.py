import os
import requests
from dotenv import load_dotenv

load_dotenv('.env')

username = os.getenv("GITHUB_USER_NAME")
access_token = os.getenv('GITHUB_ACCESS_TOKEN')
repo_name = os.getenv("REPO_NAME")
repo_descr = "New repo created using the Python GitHub API."

BASE_URL = "https://api.github.com"

HEADERS = {
    "Authorization": f"token {access_token}",
    "Accept": "application/vnd.github.v3+json"
}

def get_user_repos(username):
    """
    Получение списка репозиториев пользователя.
    """
    url = f"{BASE_URL}/users/{username}/repos"
    response = requests.get(url, headers=HEADERS)

    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to retrieve repositories. Status code: {response.status_code}")
        return None

def create_repo(repo_name, repo_descr=None, private=False):
    """
    Создание нового репозитория.
    """
    url = f"{BASE_URL}/user/repos"
    data = {
        "name": repo_name,
        "description": repo_descr,
        "private": private
    }

    response = requests.post(url, headers=HEADERS, json=data)

    if response.status_code == 201:
        print(f"Repository '{repo_name}' created successfully.")
        return response.json()
    else:
        print(f"Failed to create repository. Status code: {response.status_code}, Message: {response.text}")
        return None

def delete_repo(username, repo_name):
    """
    Удаление репозитория по имени.
    """
    url = f"{BASE_URL}/repos/{username}/{repo_name}"
    response = requests.delete(url, headers=HEADERS)

    if response.status_code == 204:
        print(f"Repository '{repo_name}' deleted successfully.")
    elif response.status_code == 404:
        print(f"Repository '{repo_name}' not found.")
    else:
        print(f"Failed to delete repository. Status code: {response.status_code}, Message: {response.text}")


repos = get_user_repos(username)
if repos:
    print(f"Repositories of {username}:")
    for repo in repos:
        print(repo["name"])

new_repo = create_repo(repo_name, repo_descr)

delete_repo(username, repo_name)
