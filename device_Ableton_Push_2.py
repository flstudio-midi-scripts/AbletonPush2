# name=Ableton Push 2
# url=https://github.com/flstudio-midi-scripts/AbletonPush2

import playlist
import channels
import mixer
import patterns
import arrangement
import transport
import device
import general
import launchMapPages

import ui
import midi
import utils

from constants import *

def updateLED(control, color = None, animation = 0):
    if device.isAssigned():
        control_type, control_name, control_id, control_note_or_color = control.split(".")
        control_id = int(control_id)
        control_note_or_color = int(control_note_or_color)
        is_rgb = bool(control_note_or_color)
        if color is None:
            if is_rgb:
                color = colors.RGB_DARK_GRAY
            else:
                color = colors.BW_DARK_GRAY
        status = midi.MIDI_CONTROLCHANGE + animation if control_type == "Button" else midi.MIDI_NOTEON + animation
        data1 = eval(f"{hex(control_id)} << 8")
        data2 = eval(f"{hex(color)} << 16")
        device.midiOutMsg(status + data1 + data2)

class AbletonPush():
    def __init__(self):
        self.isButtonShiftPressed = False

    def OnInit(self):
        for control in controls.values():
            updateLED(control)

    def OnDeInit(self):
        for control in controls.values():
            updateLED(control, 0)

    def OnMidiIn(self, event):
        if event.status == midi.MIDI_ACTIVESENSING: event.handled = True

    def OnRefresh(self, flags):
        if flags & midi.HW_Dirty_LEDs:
            self.updateLEDs()

    def OnMidiMsg(self, event):
        for control in controls.values():
            control_type, control_name, control_id, control_note_or_color = control.split(".")
            control_id = int(control_id)
            control_note_or_color = int(control_note_or_color)
            if control_type == "Button" and event.status == midi.MIDI_CONTROLCHANGE and event.data1 == control_id and event.data2 == 127:
                self.dispatch(f'On{control_type}{control_name}Pressed')
            elif control_type == "Button" and event.status == midi.MIDI_CONTROLCHANGE and event.data1 == control_id and event.data2 == 0:
                self.dispatch(f'On{control_type}{control_name}Released')
            elif control_type == "Pad" and event.status == 144 and event.data1 == control_id:
                self.dispatch(f'On{control_type}{control_name}Pressed')
            elif control_type == "Pad" and event.status == 128 and event.data1 == control_id:
                self.dispatch(f'On{control_type}{control_name}Released')
            elif control_type == "Encoder" and event.status == midi.MIDI_CONTROLCHANGE and event.data1 == control_id and event.data2 == 1:
                self.dispatch(f'On{control_type}{control_name}Increased')
            elif control_type == "Encoder" and event.status == midi.MIDI_CONTROLCHANGE and event.data1 == control_id and event.data2 == 127:
                self.dispatch(f'On{control_type}{control_name}Decreased')
            elif control_type == "Encoder" and event.status == midi.MIDI_NOTEON and event.data1 == control_note_or_color and event.data2 == 127:
                self.dispatch(f'On{control_type}{control_name}Touched')
            elif control_type == "Encoder" and event.status == midi.MIDI_NOTEON and event.data1 == control_note_or_color and event.data2 == 0:
                self.dispatch(f'On{control_type}{control_name}Released')
            elif control_type == "Touchstrip" and event.status == midi.MIDI_PITCHBEND:
                self.dispatch(f'OnPitchbend')
            elif control_type == "Touchstrip" and event.status == midi.MIDI_CONTROLCHANGE and event.data1 == control_id:
                self.dispatch(f'OnModwheel')
            elif control_type == "Touchstrip" and event.status == midi.MIDI_NOTEON and event.data1 == control_note_or_color and event.data2 == 127:
                self.dispatch(f'OnTouchstripTouched')
            elif control_type == "Touchstrip" and event.status == midi.MIDI_NOTEON and event.data1 == control_note_or_color and event.data2 == 0:
                self.dispatch(f'OnTouchstripReleased')
        event.handled = True
        print(event.status, event.data1, event.data2)

    def OnButtonPlayPressed(self):
        if transport.isPlaying():
            transport.stop()
        else:
            transport.start()

    def OnButtonDoubleLoopPressed(self):
        transport.setLoopMode()

    def OnEncoderMasterIncreased(self):
        vol = round(mixer.getTrackVolume(0), 3)
        vol = vol + 0.005 if vol < 1.0 else 1.0
        mixer.setTrackVolume(0, vol)

    def OnEncoderMasterDecreased(self):
        vol = round(mixer.getTrackVolume(0), 3)
        vol = vol - 0.005 if vol > 0.0 else 0.0
        mixer.setTrackVolume(0, vol)

    def OnEncoderMasterTouched(self):
        if self.isButtonShiftPressed: mixer.setTrackVolume(0, 1.0)

    def OnButtonRecordPressed(self):
        transport.record()

    def OnButtonShiftPressed(self):
        self.isButtonShiftPressed = True
        updateLED(controls.BUTTON_SHIFT, colors.BW_WHITE)

    def OnButtonShiftReleased(self):
        self.isButtonShiftPressed = False
        updateLED(controls.BUTTON_SHIFT)

    def dispatch(self, func):
        if hasattr(self, func):
            getattr(self, func)()
        else:
            print(f'Call to {func} not yet implemented!')

    def updateLEDs(self):
        if device.isAssigned():
            # play
            if transport.isPlaying() and transport.getLoopMode():
                updateLED(controls.BUTTON_PLAY, colors.RGB_GREEN)
            elif transport.isPlaying():
                updateLED(controls.BUTTON_PLAY, colors.RGB_ORANGE)
            else:
                updateLED(controls.BUTTON_PLAY)

            # record
            if transport.isRecording():
                updateLED(controls.BUTTON_RECORD, colors.RGB_RED)
            else:
                updateLED(controls.BUTTON_RECORD)

            # loop
            if transport.getLoopMode():
                updateLED(controls.BUTTON_DOUBLE_LOOP)
            else:
                updateLED(controls.BUTTON_DOUBLE_LOOP, colors.BW_WHITE)


ap = AbletonPush()

def OnInit():
    ap.OnInit()

def OnDeInit():
    ap.OnDeInit()

def OnIdle():
    pass

def OnMidiIn(event):
    ap.OnMidiIn(event)

def OnMidiMsg(event):
    ap.OnMidiMsg(event)

# def OnMidiOutMsg(event):
#     pass

# def OnNoteOn(event):
#     pass

# def OnNoteOff(event):
#     pass

# def OnControlChange(event):
#     pass

# def OnProgramChange(event):
#     pass

# def OnPitchBend(event):
#     pass

# def OnKeyPressure(event):
#     pass

# def OnChannelPressure(event):
#     pass

# def OnSysEx(event):
#     pass

def OnRefresh(flags):
    ap.OnRefresh(flags)

# def OnDoFullRefresh():
#     pass

# def OnUpdateBeatIndicator(value):
#     pass

# def OnDisplayZone():
#     pass

# def OnUpdateLiveMode(lastTrack):
#     pass

# def OnDirtyMixerTrack():
#     pass

# def OnUpdateMeters():
#     pass

# def OnWaitingForInput():
#     pass

# def OnSendTempMsg(message, duration):
#     pass
