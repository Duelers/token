import yaml

config_path = '/var/config/token.yaml'


def get_config(path):
    with open(path) as f:
        config = yaml.safe_load(f)
    try:
        with open(config["keys"]["location"]) as f:
            config["keys"]["public"] = f.read()
    except:
        raise FileNotFoundError("No public key file provided")
    return config


config = get_config(config_path)
