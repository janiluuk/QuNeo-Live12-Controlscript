# QuNeo-Live12-Controlscript

QuNeo controller support for Ableton Live 12+.

This repository contains a custom Ableton Live control script for the KMI QuNeo controller. It provides session and clip control, mixer navigation, transport functions, and device-focused interaction designed for Live 12 and newer.

![KMI QuNeo controller](https://keithmcmillen.com/wp-content/uploads/2014/12/QuNeoRED_angle_72dpiRGB-scaled.jpg)

## Installation

1. Download or clone this repository.
2. Copy the `QuNeo` folder into Ableton Live's MIDI Remote Scripts directory.
   - Windows: `C:\Users\<YourUser>\Music\Ableton\Remote Scripts` or the custom user folder used by your Ableton installation.
   - macOS: `~/Music/Ableton/Remote Scripts/`
3. Restart Ableton Live.
4. Open Live Preferences > Link MIDI.
5. Select the QuNeo as a control surface and enable the correct input/output ports for your device.
6. In the MIDI Remote Scripts list, confirm that `QuNeo` appears and is selected.

If the script does not appear, make sure the folder name matches exactly `QuNeo` and that the files inside are not nested one level deeper than expected.

## Quick Start / Usage

After the script is selected in Ableton:

- Use the QuNeo pads for clip launching and session navigation.
- Use the controller's buttons for transport control such as play, stop, and recording.
- Use the mixer and bank controls to adjust track levels and navigation.
- Check the `QuNeo` source files for the exact controller mapping and any custom behavior.

This script is designed to work as a MIDI Remote Script for the QuNeo and is intended for use with Ableton Live 12 and newer.

## Troubleshooting

- If the controller is not detected, verify that the device is connected and recognized by your computer.
- If the script does not appear in Live, confirm that the `QuNeo` directory is placed directly in the Remote Scripts folder and not inside another folder.
- If Live reports an error, restart the application and reload the script after confirming the folder structure.
- If the mapping feels wrong, check the MIDI port assignments in Live Preferences > Link MIDI.

## Notes

This project is built for the KMI QuNeo and is intended to extend Ableton Live with hardware control tailored to the controller's pad and button layout.
