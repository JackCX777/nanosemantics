import pathlib
import yaml


BASE_DIR = pathlib.Path(__file__).parent.parent
config_path = BASE_DIR / 'config' / 'nanosemantics_web_service.yaml'


def get_config(path):
    with open(path) as yaml_file:
        config = yaml.safe_load(yaml_file)
    return config


config = get_config(config_path)
