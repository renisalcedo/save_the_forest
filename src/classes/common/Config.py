class Configuration:
    def __init__(self):
        self.config = {'SCREEN_WIDTH': 1280, 'SCREEN_HEIGHT': 720,
                           'CENTERX': 1280 / 2, 'CENTERY': 736 / 2}
        self.custom = {}

    def add_config(self, key, val):
        self.custom[key] = val

    def get_custom(self, key):
        return self.custom[key]

    def get_config(self, key):
        return self.config[key]

    def get_all_config(self):
        return (self.config['SCREEN_WIDTH'], self.config['SCREEN_HEIGHT'],
                self.config['CENTERX'], self.config['CENTERY'])