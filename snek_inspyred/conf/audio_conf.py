from configparser import ConfigParser
from pathlib import Path
from snek_inspyred.conf.errors import AudioConfExistsError


class Audio(object):
    def __init__(self):
        self.Config = self.__Config()
        self.SoundLib == self.__SoundLib()

    class __Config(ConfigParser):
        def __init__(self):
            super().__init__()
            self.default_conf_path = Path('../game/audio/conf/conf_files/audio.ini')
            self.state = self.read('../game/audio/conf/conf_files/audio.ini')

        @staticmethod
        def get_default():
            lib = {
                'DEFAULT': {
                    'volume': 100,
                    'play_when_paused': True
                }
            }

            return lib

    class __SoundLib(ConfigParser):
        def __init__(self):
            super().__init__()
            self.default_lib_path = Path('../game/audio/conf/conf_files/sounds.lib')
            self.state = self.read('../game/audio/conf/conf_files/sounds.lib')


        @staticmethod
        def get_default():
            conf = {
                'DEFAULT': {
                    'eat-food': 'eat_food_1',
                    'begin-game': 'start_fanfare_1'
                }
            }

            return conf

        def load(self):
            pass


        def save(self, file_path: str = None, overwrite: bool = False):
            if file_path is None:
                file_path = '../game/audio/conf/conf_files/audio.ini'
            file_path = Path(file_path).expanduser()
            if file_path.exists():
                if not overwrite:
                    raise AudioConfExistsError(file_path)

            with open(file_path, 'w') as fp:
                self.write(fp)

       def create_default(self, overwrite_existing=False):
           self.read_dict(self.get_default())
           self.save(self, )