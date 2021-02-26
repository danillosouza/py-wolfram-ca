from os.path import dirname, abspath
import os
import yaml

class YamlDoc:
    def __init__(self, node: dict):
        def _traverse(key, element):
            if isinstance(element, dict):
                return key, YamlDoc(element)
            else:
                return key, element
        
        obj = dict(_traverse(k, v) for k, v in node.items())
        self.__dict__.update(obj)


def get():
    """
    Load configuration from YAML file.
    """
    filename = 'config.yaml'
    filepath = os.path.join(dirname(dirname(abspath(__file__))), filename)

    with open(filepath, 'r') as stream:
        data = YamlDoc(yaml.safe_load(stream))

        data.colors.background = tuple(data.colors.background)
        data.colors.active = tuple(data.colors.active)
        data.colors.grid = tuple(data.colors.grid)

        return data
