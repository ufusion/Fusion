import os
import json
import urllib.request
import zipfile
import shutil
import time

class Update:
    def __init__(self):
        self.update_url = "https://github.com/ufusion/your-repo/raw/main/update/"
        self.local_version_file = "version.json"
        self.check_and_download_update()

    def check_and_download_update(self):
        try:
            with urllib.request.urlopen(self.update_url + 'version.json') as url:
                remote_version = json.loads(url.read().decode())
                with open(self.local_version_file, 'r') as f:
                    local_version = json.load(f)

                if remote_version['version'] > local_version['version']:
                    print("An update is available!")
                    print(f"Version: {remote_version['version']}")
                    time.sleep(3)
                    # Prompt the user to download the update
                    confirm = input("Do you want to download and install the update? (y/n): ")
                    if confirm.lower() == "y":
                        self.download_update(remote_version)
                        print("Update downloaded and installed successfully.")
                        time.sleep(3)
                else:
                    print("You have the latest version.")
                    time.sleep(3)
        except:
            print("Failed to check for updates.")
            time.sleep(3)

    def download_update(self, version):
        try:
            with urllib.request.urlopen(self.update_url + version['filename']) as url:
                with open('update.zip', 'wb') as f:
                    f.write(url.read())

            with zipfile.ZipFile('update.zip', 'r') as zip_ref:
                zip_ref.extractall('update')

            os.remove('update.zip')

        except:
            print("Failed to download and install the update.")

# Example usage
if __name__ == "__main__":
    update_system = Update()
