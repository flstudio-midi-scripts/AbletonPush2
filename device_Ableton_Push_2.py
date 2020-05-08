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

def getClosestColor(Int):
    # TODO Create and send custom color palette to Push to match the colors in the FL project (https://github.com/Ableton/push-interface/issues/2)

    # http://www.shodor.org/stella2java/rgbint.html
    # def Int2RGBA(Int):
    #     blue = Int & 255
    #     green = (Int >> 8) & 255
    #     red = (Int >> 16) & 255
    #     alpha = (Int >> 24) & 255
    #     return red, green, blue, alpha
    #
    # def RGBA2Int(RGBA):
    #     red = RGBA[0]
    #     green = RGBA[1]
    #     blue = RGBA[2]
    #     alpha = RGBA[3]
    #     Int = (alpha<<24) + (red<<16) + (green<<8) + blue
    #     return Int

    a1 = (Int >> 24) & 255
    r1 = (Int >> 16) & 255
    g1 = (Int >> 8) & 255
    b1 = Int & 255

    rgba = (r1, g1, b1, a1)

    d = {}

    # https://stackoverflow.com/questions/1847092/given-an-rgb-value-what-would-be-the-best-way-to-find-the-closest-match-in-the-d
    # https://matplotlib.org/api/colors_api.html
    for color, RGBA in RGB_MAP.items():
        r2 = RGBA[0]
        g2 = RGBA[1]
        b2 = RGBA[2]
        a2 = RGBA[3]
        # d[color] = ((r2-r1)*0.30)**2 + ((g2-g1)*0.59)**2 + ((b2-b1)*0.11)**2
        d[color] = (r2-r1)**2 + (g2-g1)**2 + (b2-b1)**2
    return min(d, key=d.get)

def updateLED(control, color = None, animation = 0):
    if device.isAssigned():
        control_type, control_name, control_id, control_note_or_color = control.split(".")
        control_id = int(control_id)
        control_note_or_color = int(control_note_or_color)
        isRGB = bool(control_note_or_color)
        if color is None:
            if isRGB:
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
        for key, control in controls.items():
            if key.startswith("PAD"):
                updateLED(control, 0)
            else:
                updateLED(control)

    def OnDeInit(self):
        for control in controls.values():
            updateLED(control, 0)

    def OnMidiIn(self, event):
        if event.status == midi.MIDI_ACTIVESENSING: event.handled = True

    def OnRefresh(self, flags):
        # if flags and midi.HW_Dirty_LEDs:
        self.updateLEDs()

    def OnDirtyMixerTrack(self, lastTrack):
        pass
        # self.updateLEDs()

    def OnMidiMsg(self, event):
        event.handled = True
        for control in controls.values():
            control_type, control_name, control_id, control_note_or_color = control.split(".")
            control_id = int(control_id)
            control_note_or_color = int(control_note_or_color)
            if control_type == "Button" and event.status == midi.MIDI_CONTROLCHANGE and event.data1 == control_id and event.data2 == 127:
                self.dispatch(f'On{control_type}{control_name}Pressed', control, event)
            elif control_type == "Button" and event.status == midi.MIDI_CONTROLCHANGE and event.data1 == control_id and event.data2 == 0:
                self.dispatch(f'On{control_type}{control_name}Released', control, event)
            elif control_type == "Pad" and event.status == 144 and event.data1 == control_id:
                self.dispatch(f'On{control_type}Pressed', control, event)
            elif control_type == "Pad" and event.status == 128 and event.data1 == control_id:
                self.dispatch(f'On{control_type}Released', control, event)
            elif control_type == "Encoder" and event.status == midi.MIDI_CONTROLCHANGE and event.data1 == control_id and event.data2 == 1:
                self.dispatch(f'On{control_type}{control_name}Increased', control, event)
            elif control_type == "Encoder" and event.status == midi.MIDI_CONTROLCHANGE and event.data1 == control_id and event.data2 == 127:
                self.dispatch(f'On{control_type}{control_name}Decreased', control, event)
            elif control_type == "Encoder" and event.status == midi.MIDI_NOTEON and event.data1 == control_note_or_color and event.data2 == 127:
                self.dispatch(f'On{control_type}{control_name}Touched', control, event)
            elif control_type == "Encoder" and event.status == midi.MIDI_NOTEON and event.data1 == control_note_or_color and event.data2 == 0:
                self.dispatch(f'On{control_type}{control_name}Released', control, event)
            elif control_type == "Touchstrip" and event.status == midi.MIDI_PITCHBEND:
                event.handled = False # self.dispatch(f'OnPitchbend', control, event)
            elif control_type == "Touchstrip" and event.status == midi.MIDI_CONTROLCHANGE and event.data1 == control_id:
                event.handled = False # self.dispatch(f'OnModwheel', control, event)
            elif control_type == "Touchstrip" and event.status == midi.MIDI_NOTEON and event.data1 == control_note_or_color and event.data2 == 127:
                self.dispatch(f'OnTouchstripTouched', control, event)
            elif control_type == "Touchstrip" and event.status == midi.MIDI_NOTEON and event.data1 == control_note_or_color and event.data2 == 0:
                self.dispatch(f'OnTouchstripReleased', control, event)
        # print(event.status, event.data1, event.data2)

    def OnButtonPlayPressed(self, control, event):
        if transport.isPlaying():
            transport.stop()
        else:
            transport.start()

    def OnButtonDoubleLoopPressed(self, control, event):
        transport.setLoopMode()

    def OnEncoderMasterIncreased(self, control, event):
        # ui.showWindow(midi.widMixer)
        vol = round(mixer.getTrackVolume(0), 3)
        vol = vol + 0.005 if vol < 1.0 else 1.0
        mixer.setTrackVolume(0, vol)

    def OnEncoderMasterDecreased(self, control, event):
        # ui.showWindow(midi.widMixer)
        vol = round(mixer.getTrackVolume(0), 3)
        vol = vol - 0.005 if vol > 0.0 else 0.0
        mixer.setTrackVolume(0, vol)

    def OnEncoderMasterTouched(self, control, event):
        # ui.showWindow(midi.widMixer)
        if self.isButtonShiftPressed: mixer.setTrackVolume(0, 1.0)

    def OnButtonRecordPressed(self, control, event):
        transport.record()

    def OnButtonMetronomePressed(self, control, event):
        pass

    def OnButtonShiftPressed(self, control, event):
        updateLED(controls.BUTTON_SHIFT, colors.BW_WHITE)
        self.isButtonShiftPressed = True

    def OnButtonShiftReleased(self, control, event):
        updateLED(controls.BUTTON_SHIFT)
        self.isButtonShiftPressed = False

    # show/hide channel rack
    def OnButtonDevicePressed(self, control, event):
        transport.globalTransport(midi.FPT_F6, event.pmeFlags)

    # show/hide mixer
    def OnButtonMixPressed(self, control, event):
        transport.globalTransport(midi.FPT_F9, event.pmeFlags)

    # show/hide piano roll
    def OnButtonClipPressed(self, control, event):
        transport.globalTransport(midi.FPT_F7, event.pmeFlags)

    # show/hide browser
    def OnButtonBrowsePressed(self, control, event):
        print("browser visible", ui.getVisible(midi.widBrowser))
        print("browser focused", ui.getFocused(midi.widBrowser))

    # select pattern corresponding to pad when pressed
    def OnPadPressed(self, control, event):
        idx = PADS_64.index(control) + 1
        patterns.jumpToPattern(idx)

    # dispatch event to appropriate control handler
    def dispatch(self, func, control, event):
        if hasattr(self, func):
            getattr(self, func)(control, event)
        else:
            print(f'Call to {func} not yet implemented!')

    # update LEDs
    def updateLEDs(self):
        if device.isAssigned():
            # play button
            if transport.isPlaying() and transport.getLoopMode():
                updateLED(controls.BUTTON_PLAY, colors.RGB_GREEN, animations.BLINKING_QUARTER)
            elif transport.isPlaying():
                updateLED(controls.BUTTON_PLAY, colors.RGB_ORANGE, animations.BLINKING_QUARTER)
            else:
                updateLED(controls.BUTTON_PLAY)

            # record button
            if transport.isRecording():
                updateLED(controls.BUTTON_RECORD, colors.RGB_RED)
            else:
                updateLED(controls.BUTTON_RECORD)

            # double loop [song/pattern] button
            if transport.getLoopMode():
                updateLED(controls.BUTTON_DOUBLE_LOOP)
            else:
                updateLED(controls.BUTTON_DOUBLE_LOOP, colors.BW_WHITE)

            # metronome button
            if ui.isMetronomeEnabled():
                updateLED(controls.BUTTON_METRONOME, colors.BW_WHITE)
            else:
                updateLED(controls.BUTTON_METRONOME)

            # device [channel rack] button
            if ui.getFocused(midi.widChannelRack):
                updateLED(controls.BUTTON_DEVICE, colors.BW_WHITE)
            else:
                updateLED(controls.BUTTON_DEVICE)

            # mix [mixer] button
            if ui.getFocused(midi.widMixer):
                updateLED(controls.BUTTON_MIX, colors.BW_WHITE)
            else:
                updateLED(controls.BUTTON_MIX)

            # clip [piano roll] button
            if ui.getFocused(midi.widPianoRoll):
                updateLED(controls.BUTTON_CLIP, colors.BW_WHITE)
            else:
                updateLED(controls.BUTTON_CLIP)

            # browse [browser] button
            if ui.getFocused(midi.widBrowser):
                updateLED(controls.BUTTON_BROWSE, colors.BW_WHITE)
            else:
                updateLED(controls.BUTTON_BROWSE)

            # pads
            for idx, pad in enumerate(PADS_64, 1):
                if idx <= patterns.patternCount():
                    if (idx == patterns.patternNumber()):
                        if transport.isPlaying():
                            updateLED(pad, 0)
                            updateLED(pad, getClosestColor(patterns.getPatternColor(idx)), animations.BLINKING_QUARTER)
                        else:
                            updateLED(pad, 0)
                            updateLED(pad, getClosestColor(patterns.getPatternColor(idx)), animations.PULSING_HALF)
                    else:
                        updateLED(pad, getClosestColor(patterns.getPatternColor(idx)))
                else:
                    updateLED(pad, 0)

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

def OnMidiOutMsg(event):
    print("OnMidiOutMsg")

# def OnNoteOn(event):
#     print("OnNoteOn")

# def OnNoteOff(event):
#     print("OnNoteOff")

# def OnControlChange(event):
#     print("OnControlChange")

# def OnProgramChange(event):
#     print("OnProgramChange")

# def OnPitchBend(event):
#     print("OnPitchBend")

# def OnKeyPressure(event):
#     print("OnKeyPressure")

# def OnChannelPressure(event):
#     print("OnChannelPressure")

# def OnSysEx(event):
#     print("OnSysEx")

def OnRefresh(flags):
    print("OnRefresh")
    ap.OnRefresh(flags)

def OnDoFullRefresh():
    print("OnDoFullRefresh")

# def OnUpdateBeatIndicator(value):
#     print("OnUpdateBeatIndicator")

def OnDisplayZone():
    print("OnDisplayZone")

def OnUpdateLiveMode(lastTrack):
    print("OnUpdateLiveMode")

# def OnDirtyMixerTrack():
#     print("OnDirtyMixerTrack")

# def OnUpdateMeters():
#     print("OnUpdateMeters")

# def OnWaitingForInput():
#     print("OnWaitingForInput")

# def OnSendTempMsg(message, duration):
#     print("OnSendTempMsg")
