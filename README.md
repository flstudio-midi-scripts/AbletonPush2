# FL Studio MIDI script for Ableton Push 2

Given the limited set of features implemented so far, at this stage this script should be considered for educational purposes only :)

## Features

- [X] Press Play button to play/pause (press Shift + Play button to stop, LED blinks in green/orange when playing in song/pattern mode respectively)
- [X] Press Record button to toggle record
- [X] Press Double Loop button to toggle song/pattern mode
- [X] Press Quantize button to toggle snap on/off (press Shift + Quantize button to select snap mode)
- [X] Press Device/Mix/Browse/Clip/Note button to show/hide/focus channel rack/mixer/browser/playlist/piano roll
- [X] When playlist is focused, press pad to jump to a pattern (flashing red), grid shows up to 64 patterns using 64-pad mode layout, LED matches pattern color the best it can
- [X] When mixer is focused, press one or more pads to select/deselect the corresponding track (flashing green), grid shows up to 64 tracks using 64-pad mode layout, LED matches track color the best it can
- [X] When channel rack is focused, press one or more pads to select/deselect the corresponding channel(s) (flashing green), grid shows up to 64 channels using 64-pad mode layout, LED matches channel color the best it can
- [X] When mixer/channel rack is focused, press Mute button + one or more pads to mute/unmute the corresponding track/channel(s) (flashing red)
- [X] Rotate Tempo encoder to change selected track (press Shift + Tempo button to change tempo by 1 BPM)
- [X] Rotate Master encoder to change master volume (press Shift button to change pan)
- [X] When mixer is focused, rotate encoder 1-8 to change track 1-8 volume (white upper button 1) or pan (white upper button 2) where track 1 is the first selected track (press Shift button + touch encoder to reset volume or pan)
- [X] When channel rack is focused, rotate encoder 1-8 to change channel 1-8 volume (orange upper button 1) or pan (orange upper button 2) where channel 1 is the first selected channel (press Shift button + touch encoder to reset volume or pan)
- [ ] Pretty much everything remains to be implemented (particularly the implementation of performance pad mode as on the launchpads)!

## References

* [FL Studio MIDI Scripting Device API Reference](https://www.image-line.com/support/flstudio_online_betamanual/html/midi_scripting.htm)
* [FL Studio MIDI Controller Scripting Forum](https://forum.image-line.com/viewforum.php?f=1994)
* [MIDI Reference Tables](https://www.midi.org/specifications-old/category/reference-tables)
* [Ableton Push 2 MIDI and Display Interface Manual](https://github.com/Ableton/push-interface/blob/master/doc/AbletonPush2MIDIDisplayInterface.asc)
* [Launchpad Pro Programmers Reference Guide](https://fael-downloads-prod.focusrite.com/customer/prod/s3fs-public/novation/downloads/10598/launchpad-pro-programmers-reference-guide_0.pdf)
* https://github.com/ffont/push2-python
* https://github.com/soundwrightpro/FLIN

