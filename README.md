# FL Studio MIDI script for Ableton Push 2

Given the limited set of features implemented so far, at this stage this script should be considered for educational purposes only :)

## Features

- [X] Press Play button to play/pause (press Shift + Play button to stop, LED blinks in green/orange when playing in song/pattern mode respectively).
- [X] Press Record button to toggle record.
- [X] Press Double Loop button to toggle song/pattern mode.
- [X] Press Quantize button to toggle snap on/off (press Shift + Quantize button to select snap mode).
- [X] Press Device, Mix or Clip button to activate the Channel Rack, Mixer or Playlist respectively (press Shift + Device/Mix/Clip button to toggle window on/off).
- [X] When Channel Rack is active, grid shows up to 64 channels using 64-pad mode layout. Press one pad to select the corresponding channel (flashing green), press Select button + one or more pads to select the corresponding channels.
- [X] When Mixer is active, grid shows up to 64 tracks using 64-pad mode layout. Press one pad to select the corresponding track (flashing green), press Select button + one or more pads to select the corresponding tracks.
- [X] When Playlist is active, grid shows up to 64 patterns using 64-pad mode layout. Press one pad to jump to the corresponding pattern (flashing green/red).
- [X] When Channel Rack or Mixer is active, press Mute button + one or more pads to mute/unmute the corresponding channel/track(s) (flashing red)
- [X] Rotate Tempo encoder to change selected track (press Shift + Tempo button to change tempo by 1 BPM)
- [X] Rotate Master encoder to change master volume (press Shift button + touch encoder to reset volume)
- [X] When Mixer is active, rotate encoder 1-8 to change track 1-8 volume (white upper button 1) or pan (white upper button 2) where track 1 is the first selected track (press Shift button + touch encoder to reset volume or pan)
- [X] When Channel Rack is active, rotate encoder 1-8 to change channel 1-8 volume (orange upper button 1) or pan (orange upper button 2) where channel 1 is the first selected channel (press Shift button + touch encoder to reset volume or pan)
- [ ] Pretty much everything remains to be implemented (particularly the implementation of performance pad mode as on the launchpads)!

## References

* [FL Studio MIDI Scripting Device API Reference](https://www.image-line.com/support/flstudio_online_betamanual/html/midi_scripting.htm)
* [FL Studio MIDI Controller Scripting Forum](https://forum.image-line.com/viewforum.php?f=1994)
* [MIDI Reference Tables](https://www.midi.org/specifications-old/category/reference-tables)
* [Ableton Push 2 MIDI and Display Interface Manual](https://github.com/Ableton/push-interface/blob/master/doc/AbletonPush2MIDIDisplayInterface.asc)
* [Launchpad Pro Programmers Reference Guide](https://fael-downloads-prod.focusrite.com/customer/prod/s3fs-public/novation/downloads/10598/launchpad-pro-programmers-reference-guide_0.pdf)
* https://github.com/ffont/push2-python
* https://github.com/soundwrightpro/FLIN

