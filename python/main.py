from planetcollector import get_all_planet_data_from_directory
from generate_events import generate_event_file


def main():
    planet_data = get_all_planet_data_from_directory("xml")
    generate_event_file(planet_data)


if __name__ == "__main__":
    main()