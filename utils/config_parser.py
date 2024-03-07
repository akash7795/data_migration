
YAML_CONFIG_EXTS = ('yml', 'yaml')
JSON_CONFIG_EXTS = ('json')

def read_config_file(config_file_path):
    """
        Returns a dict containig configurations read from the config file present at path
        Allowed file type: json, yaml
        :param path: absolute path to config file
        :type path: string
    """
    if config_file_path.lower().endswith(YAML_CONFIG_EXTS):
        from yaml import load
        with open(config_file_path, 'r') as f:
            configs_as_string = f.read()
            return load(configs_as_string)

    elif config_file_path.lower().endswith(JSON_CONFIG_EXTS):
        from json import loads
        with open(config_file_path, 'r') as f:
            configs_as_string = f.read()
            return loads(configs_as_string)
