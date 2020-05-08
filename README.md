# FL Studio MIDI script for Ableton Push 2

Given the limited set of features implemented so far, at this stage this script should be considered for educational purposes only :)

## Features

- [X] Press Play button -> play/stop (blinking green/orange when playing in song/pattern mode)
- [X] Press Record button -> toggle record
- [X] Press Double Loop button -> song/pattern mode
- [X] Press Quantize button -> snap on/off (press Shift + Quantize button -> select snap mode)
- [X] Press Device/Mix/Browse/Clip button -> show/hide channel rack/mixer/browser/piano roll
- [X] 8x8 pad grid shows up to 64 patterns and hitting the pad selects the corresponding pattern
- [X] Rotate Tempo encoder -> change selected track (TODO: press Shift button to change tempo)
- [X] Rotate Master encoder -> change master volume (press Shift button to change pan)
- [X] Rotate encoder 1-8 -> change track 1-8 volume (press Shift button to change pan) where track 1 is the selected track
- [ ] Pretty much everything remains to be implemented (particularly the implementation of performance pad mode as on the launchpads)!

## References

* [FL Studio MIDI Scripting Device API Reference](https://www.image-line.com/support/flstudio_online_betamanual/html/midi_scripting.htm)
* [FL Studio MIDI Controller Scripting Forum](https://forum.image-line.com/viewforum.php?f=1994)
* [MIDI Reference Tables](https://www.midi.org/specifications-old/category/reference-tables)
* [Ableton Push 2 MIDI and Display Interface Manual](https://github.com/Ableton/push-interface/blob/master/doc/AbletonPush2MIDIDisplayInterface.asc)
* [Launchpad Pro Programmers Reference Guide](https://fael-downloads-prod.focusrite.com/customer/prod/s3fs-public/novation/downloads/10598/launchpad-pro-programmers-reference-guide_0.pdf)
* https://github.com/ffont/push2-python
* https://github.com/soundwrightpro/FLIN

