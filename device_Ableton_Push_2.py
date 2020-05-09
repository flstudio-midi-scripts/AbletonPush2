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

def getClosestColor(color):
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

    RGB = utils.ColorToRGB(color)

    R1 = RGB[0]
    G1 = RGB[1]
    B1 = RGB[2]

    d = {}

    # https://stackoverflow.com/questions/1847092/given-an-rgb-value-what-would-be-the-best-way-to-find-the-closest-match-in-the-d
    # https://matplotlib.org/api/colors_api.html
    for color, RGB in RGB_MAP.items():
        R2 = RGB[0]
        G2 = RGB[1]
        B2 = RGB[2]
        d[color] = (R2-R1)**2 + (G2-G1)**2 + (B2-B1)**2

    return min(d, key=d.get)

class AbletonPush():
    def __init__(self):
        self.controls = AttrDict()
        self.controls.isButtonShiftPressed = False
        self.mixer = AttrDict()
        self.mixer.encodersTarget = ENCODERS_TARGET.TRACK_VOL
        self.channels = AttrDict()
        self.channels.encodersTarget = ENCODERS_TARGET.CHANNEL_VOL

    def OnInit(self):
        for control in controls.values():
            self.updateLED(control)

    def OnDeInit(self):
        for control in controls.values():
            self.updateLED(control, 0)

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
                if control_name in ["Upper" + str(i) for i in range(1,9)]:
                    self.dispatch(f'On{control_type}UpperPressed', control, event)
                else:
                    self.dispatch(f'On{control_type}{control_name}Pressed', control, event)
            elif control_type == "Button" and event.status == midi.MIDI_CONTROLCHANGE and event.data1 == control_id and event.data2 == 0:
                if control_name in ["Upper" + str(i) for i in range(1,9)]:
                    self.dispatch(f'On{control_type}UpperReleased', control, event)
                else:
                    self.dispatch(f'On{control_type}{control_name}Released', control, event)
            elif control_type == "Pad" and event.status == 144 and event.data1 == control_id:
                self.dispatch(f'On{control_type}Pressed', control, event)
            elif control_type == "Pad" and event.status == 128 and event.data1 == control_id:
                self.dispatch(f'On{control_type}Released', control, event)
            elif control_type == "Encoder" and event.status == midi.MIDI_CONTROLCHANGE and event.data1 == control_id and event.data2 == 1:
                if control_name in [str(i) for i in range(1,9)]:
                    self.dispatch(f'On{control_type}Increased', control, event)
                else:
                    self.dispatch(f'On{control_type}{control_name}Increased', control, event)
            elif control_type == "Encoder" and event.status == midi.MIDI_CONTROLCHANGE and event.data1 == control_id and event.data2 == 127:
                if control_name in [str(i) for i in range(1,9)]:
                    self.dispatch(f'On{control_type}Decreased', control, event)
                else:
                    self.dispatch(f'On{control_type}{control_name}Decreased', control, event)
            elif control_type == "Encoder" and event.status == midi.MIDI_NOTEON and event.data1 == control_note_or_color and event.data2 == 127:
                if control_name in [str(i) for i in range(1,9)]:
                    self.dispatch(f'On{control_type}Touched', control, event)
                else:
                    self.dispatch(f'On{control_type}{control_name}Touched', control, event)
            elif control_type == "Encoder" and event.status == midi.MIDI_NOTEON and event.data1 == control_note_or_color and event.data2 == 0:
                if control_name in [str(i) for i in range(1,9)]:
                    self.dispatch(f'On{control_type}Released', control, event)
                else:
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

    # play button
    def OnButtonPlayPressed(self, control, event):
        # stop if Shift button is pressed else pause
        if self.controls.isButtonShiftPressed:
                transport.stop()
        else:
            transport.start()

    # record button
    def OnButtonRecordPressed(self, control, event):
        transport.record()

    # double loop button
    def OnButtonDoubleLoopPressed(self, control, event):
        transport.setLoopMode()

    # metronome button
    def OnButtonMetronomePressed(self, control, event):
        transport.globalTransport(midi.FPT_Metronome, event.pmeFlags)

    # tap tempo button TODO + shift -> cycle through the preset tempos
    def OnButtonTapTempoPressed(self, control, event):
        updateLED(controls.BUTTON_TAP_TEMPO, colors.BW_WHITE)
        transport.globalTransport(midi.FPT_TapTempo, event.pmeFlags)

    def OnButtonTapTempoReleased(self, control, event):
        updateLED(controls.BUTTON_TAP_TEMPO)

    # tempo encoder
    def OnEncoderTempoIncreased(self, control, event):
        if self.controls.isButtonShiftPressed:
            transport.globalTransport(midi.FPT_TempoJog, 10)
        else:
            if ui.getFocused(midi.widChannelRack):
                pass # TODO move channel rack grid down
            else:
                if mixer.trackNumber() < mixer.trackCount():
                    mixer.setTrackNumber(mixer.trackNumber() + 1)

    def OnEncoderTempoDecreased(self, control, event):
        if self.controls.isButtonShiftPressed:
            transport.globalTransport(midi.FPT_TempoJog, -10)
        else:
            if ui.getFocused(midi.widChannelRack):
                pass # TODO move channel rack grid up
            else:
                if mixer.trackNumber() > 0:
                    mixer.setTrackNumber(mixer.trackNumber() - 1)

    # master encoder
    def OnEncoderMasterIncreased(self, control, event):
        mixer.setTrackVolume(0, mixer.getTrackVolume(0) + VOL_INC)

    def OnEncoderMasterDecreased(self, control, event):
        mixer.setTrackVolume(0, mixer.getTrackVolume(0) - VOL_INC)

    def OnEncoderMasterTouched(self, control, event):
        if self.controls.isButtonShiftPressed:
            mixer.setTrackVolume(0, 1)

    # numbered encoder
    def OnEncoderIncreased(self, control, event):
        control_type, control_name, control_id, control_note_or_color = control.split(".")
        control_number = int(control_name)
        if ui.getFocused(midi.widMixer):
            index = mixer.trackNumber() + control_number - 1
            if self.mixer.encodersTarget == ENCODERS_TARGET.TRACK_VOL:
                mixer.setTrackVolume(index, mixer.getTrackVolume(index) + VOL_INC)
            elif self.mixer.encodersTarget == ENCODERS_TARGET.TRACK_PAN:
                mixer.setTrackPan(index, mixer.getTrackPan(index) + PAN_INC)
        elif ui.getFocused(midi.widChannelRack) and control_number <= channels.channelCount():
            index = channels.channelNumber() + control_number - 1
            if self.channels.encodersTarget == ENCODERS_TARGET.CHANNEL_VOL:
                channels.setChannelVolume(index, channels.getChannelVolume(index) + VOL_INC)
            elif self.channels.encodersTarget == ENCODERS_TARGET.CHANNEL_PAN:
                channels.setChannelPan(index, channels.getChannelPan(index) + PAN_INC)

    def OnEncoderDecreased(self, control, event):
        control_type, control_name, control_id, control_note_or_color = control.split(".")
        control_number = int(control_name)
        if ui.getFocused(midi.widMixer):
            index = mixer.trackNumber() + control_number - 1
            if self.mixer.encodersTarget == ENCODERS_TARGET.TRACK_VOL:
                mixer.setTrackVolume(index, mixer.getTrackVolume(index) - VOL_INC)
            elif self.mixer.encodersTarget == ENCODERS_TARGET.TRACK_PAN:
                mixer.setTrackPan(index, mixer.getTrackPan(index) - PAN_INC)
        elif ui.getFocused(midi.widChannelRack) and control_number <= channels.channelCount():
            index = channels.channelNumber() + control_number - 1
            if self.channels.encodersTarget == ENCODERS_TARGET.CHANNEL_VOL:
                channels.setChannelVolume(index, channels.getChannelVolume(index) - VOL_INC)
            elif self.channels.encodersTarget == ENCODERS_TARGET.CHANNEL_PAN:
                channels.setChannelPan(index, channels.getChannelPan(index) - PAN_INC)

    def OnEncoderTouched(self, control, event):
        control_type, control_name, control_id, control_note_or_color = control.split(".")
        control_number = int(control_name)
        if self.controls.isButtonShiftPressed:
            if ui.getFocused(midi.widMixer):
                index = mixer.trackNumber() + control_number - 1
                if self.mixer.encodersTarget == ENCODERS_TARGET.TRACK_VOL:
                    mixer.setTrackVolume(index, 1)
                elif self.mixer.encodersTarget == ENCODERS_TARGET.TRACK_PAN:
                    mixer.setTrackPan(index, 0)
            elif ui.getFocused(midi.widChannelRack) and control_number <= channels.channelCount():
                index = channels.channelNumber() + control_number - 1
                if self.channels.encodersTarget == ENCODERS_TARGET.CHANNEL_VOL:
                    channels.setChannelVolume(index, 1)
                elif self.channels.encodersTarget == ENCODERS_TARGET.CHANNEL_PAN:
                    channels.setChannelPan(index, 0)

    # numbered upper button
    def OnButtonUpperPressed(self, control, event):
        control_type, control_name, control_id, control_note_or_color = control.split(".")
        control_number = int(control_name.replace("Upper", ""))
        if ui.getFocused(midi.widMixer) and control_number <= 2:
            self.mixer.encodersTarget = control_number
        elif ui.getFocused(midi.widChannelRack) and control_number <= 2:
            self.channels.encodersTarget = control_number
        self.updateLEDs()

    # quantize/snap button
    def OnButtonQuantizePressed(self, control, event):
        if self.controls.isButtonShiftPressed:
            ui.snapMode(1)
        else:
            ui.snapOnOff()

    # undo button
    def OnButtonUndoPressed(self, control, event):
        updateLED(controls.BUTTON_UNDO, colors.BW_WHITE)
        if self.controls.isButtonShiftPressed:
            general.undoDown()
        else:
            general.undoUp()

    def OnButtonUndoReleased(self, control, event):
        updateLED(controls.BUTTON_UNDO)

    # shift button
    def OnButtonShiftPressed(self, control, event):
        updateLED(controls.BUTTON_SHIFT, colors.BW_WHITE)
        self.controls.isButtonShiftPressed = True

    def OnButtonShiftReleased(self, control, event):
        updateLED(controls.BUTTON_SHIFT)
        self.controls.isButtonShiftPressed = False

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

    # update LED
    def updateLED(self, control, color = None, animation = 0):
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

    # update LEDs
    def updateLEDs(self):
        if device.isAssigned():
            # play button
            if transport.isPlaying() and transport.getLoopMode():
                self.updateLED(controls.BUTTON_PLAY, colors.RGB_GREEN, animations.BLINKING_QUARTER)
            elif transport.isPlaying():
                self.updateLED(controls.BUTTON_PLAY, colors.RGB_ORANGE, animations.BLINKING_QUARTER)
            else:
                self.updateLED(controls.BUTTON_PLAY)

            # record button
            if transport.isRecording():
                self.updateLED(controls.BUTTON_RECORD, colors.RGB_RED)
            else:
                self.updateLED(controls.BUTTON_RECORD)

            # double loop [song/pattern] button
            if transport.getLoopMode():
                self.updateLED(controls.BUTTON_DOUBLE_LOOP)
            else:
                self.updateLED(controls.BUTTON_DOUBLE_LOOP, colors.BW_WHITE)

            # metronome button
            if ui.isMetronomeEnabled():
                self.updateLED(controls.BUTTON_METRONOME, colors.BW_WHITE)
            else:
                self.updateLED(controls.BUTTON_METRONOME)

            # device [channel rack] button
            if ui.getFocused(midi.widChannelRack):
                self.updateLED(controls.BUTTON_DEVICE, colors.BW_WHITE)
            else:
                self.updateLED(controls.BUTTON_DEVICE)

            # mix [mixer] button
            if ui.getFocused(midi.widMixer):
                self.updateLED(controls.BUTTON_MIX, colors.BW_WHITE)
            else:
                self.updateLED(controls.BUTTON_MIX)

            # clip [piano roll] button
            if ui.getFocused(midi.widPianoRoll):
                self.updateLED(controls.BUTTON_CLIP, colors.BW_WHITE)
            else:
                self.updateLED(controls.BUTTON_CLIP)

            # browse [browser] button
            if ui.getFocused(midi.widBrowser):
                self.updateLED(controls.BUTTON_BROWSE, colors.BW_WHITE)
            else:
                self.updateLED(controls.BUTTON_BROWSE)

            # quantize/snap button
            if ui.getSnapMode() != 3:
                self.updateLED(controls.BUTTON_QUANTIZE, colors.BW_WHITE)
            else:
                self.updateLED(controls.BUTTON_QUANTIZE)


            # numbered upper buttons
            for idx, button in enumerate(BUTTONS_UPPER, 1):
                if ui.getFocused(midi.widMixer):
                    if (idx == self.mixer.encodersTarget):
                        self.updateLED(button, colors.RGB_WHITE)
                    else:
                        self.updateLED(button)
                elif ui.getFocused(midi.widChannelRack):
                    if (idx == self.channels.encodersTarget):
                        self.updateLED(button, colors.RGB_ORANGE)
                    else:
                        self.updateLED(button)
                else:
                    self.updateLED(button)

            # pads
            for idx, pad in enumerate(PADS_64, 1):
                if idx <= patterns.patternCount():
                    if (idx == patterns.patternNumber()):
                        if transport.isPlaying():
                            self.updateLED(pad, 0)
                            self.updateLED(pad, getClosestColor(patterns.getPatternColor(idx)), animations.BLINKING_QUARTER)
                        else:
                            self.updateLED(pad, 0)
                            self.updateLED(pad, getClosestColor(patterns.getPatternColor(idx)), animations.PULSING_HALF)
                    else:
                        self.updateLED(pad, getClosestColor(patterns.getPatternColor(idx)))
                else:
                    self.updateLED(pad, 0)

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
