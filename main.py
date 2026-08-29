from pathlib import Path
import os

def isNumber(letter):
    return letter.isdigit()

def moveAddonFile(path_to_steamcmd, addon_id):
    while True:
        extract = input("Move folder with addon to your folder(y/n): ").lower()
        if extract == 'y':
            path_to_output = Path(input("Enter path to folder(example: /home/neatink/Desktop/steamfolder/): "))
            downloadAddon(path_to_steamcmd, addon_id, path_to_output)
        elif extract == 'n':
            downloadAddon(path_to_steamcmd, addon_id)
        else:
            print("Enter 'y' or 'n'!")
        return;
            
def downloadAddon(path_to_steamcmd, addon_id, path_to_output = None):
    os.system(f"{path_to_steamcmd} {f"+force_install_dir {path_to_output}" if path_to_output else ""} +login anonymous +workshop_download_item 4000 {addon_id} +quit")
    print("Successfully. Have a good day!")

def start():
    while True:
        path_to_steamcmd = input("Enter absolute path to SteamCmd file(example: /home/neatink/steamCmd/steamcmd.sh): ").strip("'")
        if Path(path_to_steamcmd).is_file():
            break
        else:
            print("File not found. Try again!")
    while True:
        try:
            addon_id = input("Enter addon id(or url(example: https://steamcommunity.com/sharedfiles/filedetails/?id=731572743)): ")
            if addon_id.startswith("https://steamcommunity.com/sharedfiles/filedetails"):
                addon_id = addon_id.split("/")
                addon_id = ''.join(tuple(filter(isNumber, addon_id[len(addon_id) - 1])))
                moveAddonFile(path_to_steamcmd, addon_id)
            elif addon_id.isdigit():
                moveAddonFile(path_to_steamcmd, addon_id)
            else:
                print("Enter valid id!")
        except Exception as err:
            print(f"Unknown error: {err}")
    
if __name__ == "__main__":
    start()