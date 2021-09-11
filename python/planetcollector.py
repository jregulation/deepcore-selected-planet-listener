import os
from xml.etree import ElementTree as et

from rich import print


def get_planet_data(element: et.Element):
    return {
        "name": element.get("Name")
    }


def get_all_planet_data_from_file(file_path: str):
    tree = et.parse(file_path)
    root = tree.getroot()
    return [get_planet_data(element) for element in planets_without_backdrop(root)]


def planets_without_backdrop(root: et.Element = None):
    return filter(lambda x: x.get("Name") != "Galaxy_Core_Art_Model", root.findall("Planet"))


def get_all_planet_data_from_directory(directory_path: str):
    all_data = []
    for file_path in os.listdir(directory_path):
        all_data += get_all_planet_data_from_file(
            os.path.join(directory_path, file_path))

    return sorted(all_data, key=lambda x: x["name"])
