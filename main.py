import requests, json, time

def main():
    session = requests.Session()

    def checkversion():
        url = "https://clientsettings.roblox.com/v2/client-version/WindowsPlayer/channel/LIVE"
        response = session.get(url)
        decoded = json.loads(response.text)

        return decoded["clientVersionUpload"]

    currentversion = checkversion()

    while True:
        if currentversion != checkversion():
            print("roblox has updated nigga" + f"https://setup.rbxcdn.com/{currentversion}-RobloxPlayerInstaller.exe")
            currentversion = checkversion()

        time.sleep(60)

if __name__ == "__main__":
    main()
