from typing import Dict, List
from jinja2 import Template
from xml.etree import ElementTree as et


EVENT_FILE_NAME = "PlanetSelectionEvents.xml"
TEMPLATE_FILE_PATH = f"python/templates/{EVENT_FILE_NAME}"


def read_template() -> str:
    with open(TEMPLATE_FILE_PATH) as template_file:
        return template_file.read()


def generate_event_file(planets: List[Dict[str, str]]) -> None:
    with open(EVENT_FILE_NAME, "w+") as file:
        template = Template(read_template())
        result = template.render(planets=planets)
        file.write(result)
