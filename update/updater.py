import requests
import json
import time
import base64
import os
import shutil
import zipfile

class Update:
    def __init__(self):
        self.repo_url = "ufusion/Fusion"
        self.check_for_updates()

    def check_for_updates(self):
        try:
            api_url = f"https://api.github.com/repos/{self.repo_url}/contents/update/version.json"
            response = requests.get(api_url)
            if response.status_code == 200:
                data = response.json()
                content = data["content"]
                remote_version = json.loads(base64.b64decode(content).decode())["version"]
                with open("update/version.json") as f:
                    local_version = json.load(f)["version"]

                if remote_version > local_version:
                    print("An update is available. Do you want to download and install it? (y/n): ", end="")
                    choice = input().strip().lower()
                    if choice == "y":
                        repo_name = self.repo_url.split("/")[-1]
                        zip_filename = f"Fusion_v{remote_version}.zip"
                        self.download_repository(self.repo_url, zip_filename)
                        self.remove_old_files(repo_name)
                        self.extract_repository(zip_filename)
                        print("Update downloaded and installed successfully.")
                        time.sleep(5)
                else:
                    print("No updates available.")
                    time.sleep(5)
            else:
                print("Failed to fetch version.json from the repository.")
                time.sleep(5)
        except Exception as e:
            print(f"Failed to check for updates.\n{e}")
            time.sleep(5)

    def download_repository(self, repo_url, zip_filename):
        try:
            api_url = f"https://api.github.com/repos/{repo_url}/zipball"
            response = requests.get(api_url, stream=True)
            if response.status_code == 200:
                with open(zip_filename, "wb") as f:
                    f.write(response.content)
                print(f"Repository '{repo_url}' downloaded as '{zip_filename}'.")
            else:
                print(f"Failed to download repository '{repo_url}'.")
        except Exception as e:
            print(f"Failed to download repository.\n{e}")
            time.sleep(5)

    def remove_old_files(self, repo_name):
        try:
            shutil.rmtree(repo_name, ignore_errors=True)
            print("Old files and folders removed.")
            time.sleep(5)
        except Exception as e:
            print(f"Failed to remove old files and folders.\n{e}")
            time.sleep(5)

    def extract_repository(self, zip_filename):
        try:
            with zipfile.ZipFile(zip_filename, "r") as zip_file:
                zip_file.extractall(".")
            print("Repository extracted.")
        except Exception as e:
            print(f"Failed to extract repository.\n{e}")
            time.sleep(5)

