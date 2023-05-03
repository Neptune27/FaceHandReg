import pickle


class FASetting:
    isLoaded = False
    settings = {}

    def __init__(self):
        pass

    def __call__(self, *args, **kwargs):
        raise TypeError("Use getInstance for this.")

    @staticmethod
    def getInstance(name):
        if not FASetting.isLoaded:
            FASetting.load()

        obj = FASetting.settings.get(name)
        if obj is not None:
            return obj
        else:
            return FASetting.settings.setdefault(name, FASetting())

    @staticmethod
    def save(location: str = "data/setting.pickle"):
        with open(location, "wb") as f:
            f.write(pickle.dumps(FASetting.settings))

    @staticmethod
    def load(location: str = "data/setting.pickle"):
        FASetting.settings = pickle.loads(open(location, 'rb').read())
        FASetting.isLoaded = True

