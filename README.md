# FL Studio MIDI script for Ableton Push 2

Given the limited set of features implemented so far, at this stage this script should be considered for educational purposes only :)

## Features

- [X] Press Play button to play/pause (press Shift + Play button to stop, LED blinks in green/orange when playing in song/pattern mode respectively)
- [X] Press Record button to toggle record
- [X] Press Double Loop button to toggle song/pattern mode
- [X] Press Quantize button to toggle snap on/off (press Shift + Quantize button to select snap mode)
- [X] Press Device/Mix/Browse/Clip button to show/hide channel rack/mixer/browser/piano roll
- [X] Press Pad to select corresponding pattern (grid shows up to 64 patterns using the 64-pad mode layout, LED matches the best it can the pattern color)
- [X] Rotate Tempo encoder to change selected track (press Shift + Tempo button to change tempo by 1 BPM)
- [X] Rotate Master encoder to change master volume (press Shift button to change pan)
- [X] Rotate encoder 1-8 to change track or channel 1-8 volume (upper button 1) or pan (upper button 2) where track/channel 1 is the selected track/channel and depending on whether mixer or channel rack is focused (press Shift button and touch encoder to reset volume or pan)
- [ ] Pretty much everything remains to be implemented (particularly the implementation of performance pad mode as on the launchpads)!

## References

* [FL Studio MIDI Scripting Device API Reference](https://www.image-line.com/support/flstudio_online_betamanual/html/midi_scripting.htm)
* [FL Studio MIDI Controller Scripting Forum](https://forum.image-line.com/viewforum.php?f=1994)
* [MIDI Reference Tables](https://www.midi.org/specifications-old/category/reference-tables)
* [Ableton Push 2 MIDI and Display Interface Manual](https://github.com/Ableton/push-interface/blob/master/doc/AbletonPush2MIDIDisplayInterface.asc)
* [Launchpad Pro Programmers Reference Guide](https://fael-downloads-prod.focusrite.com/customer/prod/s3fs-public/novation/downloads/10598/launchpad-pro-programmers-reference-guide_0.pdf)
* https://github.com/ffont/push2-python
* https://github.com/soundwrightpro/FLIN

