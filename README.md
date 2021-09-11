# Planet Selection Listener Plugin for DeepCore

## About

This repository contains the `selected-planet-listener` plugin used in Empire at War Expanded.
You must have [DeepCore](https://github.com/SvenMarcus/deepcore-standalone) installed for this to work.

## Generating the required planet selection story events

The following steps are necessary in order for the plugin to work. You cannot skip them.
To function properly the plugin needs xml story events for every planet in your mod.
The following steps allow you to generate a file with all the events automatically.
If you don't have Python 3.6 or new installed or don't want to run it locally follow the steps in the section below.
If you have a compatible Python version installed you can also perform the necessary steps yourself. For this go to section [If you have Python (>= 3.6) installed](#if-you-have-python--36-installed)

### If you don't have Python (>= 3.6) installed on your PC

1. Create a fork of this repository.
2. Clone your fork to your PC:
   ```bash
   git clone https://github.com/YOURUSERNAME/deepcore-selected-planet-listener
   ```
3. Replace the file `xml/Planets.xml` with your mod's `Planets.xml` (can also be multiple files).
4. Commit & push your changes.
5. Goto https://github.com/YOURUSERNAME/deepcore-selected-planet-listener
6. A GitHub Action should have been run automatically. Download its artifact.
7. Continue with [Installing the plugin](#installing-the-plugin)


### If you have Python (>= 3.6) installed
1. Clone the repository to your PC:
   ```bash
   git clone https://github.com/SvenMarcus/deepcore-selected-planet-listener
   ```
2. Create & activate a virtual environment
3. Install the requirements
   ```bash
   pip install -r python/requirements.txt
   ```
3. Replace the file `xml/Planets.xml` with your mod's `Planets.xml` (can also be multiple files).
4. Run `main.py` from the top level folder of the repository.
   ```bash
   python3 python/main.py
   ```
5. Continue with [Installing the plugin](#installing-the-plugin)

### Installing the plugin
1. Drop the `PlanetSelectionEvents.xml` file into your mod's `XML` folder.
2. Link `PlanetSelectionEvents.xml` in your galactic conquest plot files.
3. Drop the `selected-planet-listener` directory into your mod's deepcore plugin folder.
4. If your plugin folder is not called `plugins` go into `selected-planet-listener/init.lua` and adjust the path of the `require` call:
   ```lua
   require("YOUR_PLUGINFOLDER_NAME/selected-planet-listener/SelectedPlanetChangedEvent")
   ```
5. Add `selected-planet-listener` to your `InstalledPlugins.lua` file or pass it to the `deepcore` initializer:
   ```lua
   DeepCoreRunner = deepcore:galactic {
      plugin_folder = "plugins"
      plugins = {
         "your-other-plugins",
         "selected-planet-listener"
      }
   }
   ```
