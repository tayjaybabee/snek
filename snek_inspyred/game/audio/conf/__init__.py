from configparser import ConfigParser
from pathlib import Path
from snek_inspyred.conf.errors import AudioConfExistsError

CONF_DIR = Path(__file__).parent
ASSET_DIR = CONF_DIR.joinpath('../assets').resolve()


class Audio(object):
    def __init__(self):
        self.Config = self.__Config()
        self.SoundLib = self.__SoundLib()

    class __Config(ConfigParser):
        def __init__(self):
            super().__init__()
            self.default_conf_path = Path('../game/audio/conf/conf_files/audio.ini')

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
        def __init__(self, filepath: str = None):
            super().__init__()

            self.default_fp = CONF_DIR.joinpath('conf_files/sounds.lib')
            if filepath is not None:
                self.filepath = Path(filepath).expanduser().resolve()
            else:
                self.filepath = self.default_fp
            self.read(self.filepath)

        @staticmethod
        def get_default():
            ef_fp = ASSET_DIR.joinpath('eat_food_1.wav')
            bg_fp = ASSET_DIR.joinpath('start_fanfare_1.wav')
            conf = {
                'DEFAULT': {
                    'eat-food': str(ef_fp),
                    'begin-game': str(bg_fp)
                }
            }

            return conf

        def load(self):
            return self.read(self.filepath)

        def save(self, file_path: str = None, overwrite: bool = False):
            """

            Args:
                file_path:
                overwrite:

            Returns:

            """
            if file_path is None:
                file_path = CONF_DIR.joinpath('conf_files/sounds.lib')
            file_path = Path(file_path).expanduser().resolve()
            if file_path.exists():
                if not overwrite:
                    raise AudioConfExistsError(file_path)

            with open(file_path, 'w') as fp:
                self.write(fp)

        def purge_sections(self, exclude: list = None):
            """
            Clear all sections from the sound library (which is just a ConfigParser object, dressed-up.

            Goes through each section (except DEFAULT) and removes it, unless the section name matches one you include
            in a list which you pass to the 'exclude' parameter.

            Args:
                exclude (str|list): A list of sections you'd like to -not- remove from the sound library. (Defaults to
                NoneType)

            Returns:
                None

            """
            excluded = []
            if not isinstance(exclude, list):
                if isinstance(exclude, str):
                    if ' ' not in exclude:
                        excluded = [exclude]
                    else:
                        excluded += exclude.split(' ')
                else:
                    raise ValueError(exclude)
            else:
                excluded += exclude

            for section in self.sections():
                if section not in excluded:
                    self.remove_section(section)

        def reset(self):
            """

            Clear the settings object so a new state can be applied.

            This function goes through every section in the parser and removes it, following that with running
            'clear()' on the parser's 'default' section.py

            Returns:
                None

            """
            for section in self.sections():
                self.remove_section(section)

            self['DEFAULT'].clear()

        def create_default(self, overwrite_existing=False):
            self.reset()
            self.read_dict(self.get_default())
            self.save(overwrite=overwrite_existing)
            self.load()


AudioConf = Audio()
Config = AudioConf.Config
SoundLib = AudioConf.SoundLib
