import json
import os
import pickle

from Utils.UserSetting import UserSetting


class Setting:
    def __init__(self):
        self.user: dict[str, UserSetting] = {}

    def load(self):
        try:
            jsonFile = open("data/setting.pickle", "rb").read()
            tmp: Setting = pickle.loads(jsonFile)
            self.user = tmp.user
        except KeyError:
            print("[ERROR] The formatting of setting.pickle is wrong, reset to default...")
            self.setDefault()
        except FileNotFoundError:
            print("[ERROR] setting.pickle not found, reset to default...")
            self.setDefault()
        except TypeError:
            print("[ERROR] Wrong values were parsed, reset to default...")
            self.setDefault()

    def create_recursive_dir(self, dir_path):
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)

    def setDefault(self):
        self.create_recursive_dir("data")
        setting = Setting()
        with open("data/setting.pickle", "wb") as f:
            f.write(pickle.dumps(setting))

    def save(self):
        self.create_recursive_dir("data")
        with open("data/setting.pickle", "wb") as f:
            f.write(pickle.dumps(self))

    def resetToDefault(self, name):
        try:
            userSetting = self.user[name]
            userSetting.One = "L,"
            userSetting.Two = "R,"
            userSetting.Three = "U,"
            userSetting.Open = "D,"
            userSetting.Close = "D,"

        except AttributeError or KeyError:
            pass

    def add(self, name):
        self.user[name] = UserSetting()
        self.resetToDefault(name)


if __name__ == "__main__":
    setting = Setting()
    # setting.load()
    wutSetting = UserSetting()
    wutSetting.Close = "L"
    setting.user["Wut"] = wutSetting
    setting.save()
    # setting.user["Wut"] =
    # setattr(setting.user["Wut"], "palm", "a")
