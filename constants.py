class AttributeDict(dict):
    def __getattr__(self, key):
        return self[key]
    def __setattr__(self, key, value):
        self[key] = value

colors = AttributeDict()
colors.RGB_BLACK = 0
colors.RGB_WHITE = 122
colors.RGB_LIGHT_GRAY = 123
colors.RGB_DARK_GRAY = 124
colors.RGB_BLUE = 125
colors.RGB_GREEN = 126
colors.RGB_RED = 127
colors.RGB_ORANGE = 3
colors.RGB_YELLOW = 8
colors.RGB_TURQUOISE = 15
colors.RGB_PURPLE = 22
colors.RGB_PINK = 25

colors.BW_BLACK = 0
colors.BW_DARK_GRAY = 16
colors.BW_LIGHT_GRAY = 48
colors.BW_WHITE = 127

# https://www.colorhexa.com/
colors.RGB_MAP = {
    0 : (0,0,0), # RGB_BLACK
    122 : (204,204,204), # RGB_WHITE
    123 : (64,64,64), # RGB_LIGHT_GRAY
    124 : (20,20,20), # RGB_DARK_GRAY
    125 : (0,0,255), # RGB_BLUE
    126 : (0,255,0), # RGB_GREEN
    127 : (255,0,0), # RGB_RED
    3 : (100,65,0), # RGB_ORANGE
    8 : (100,100,0), # RGB_YELLOW
    15 : (25,88,82), # RGB_TURQUOISE
    22 : (50,0,50), # RGB_PURPLE
    25 : (100,75,80), # RGB_PINK
}

animations = AttributeDict()
animations.STOP = 0
animations.ONESHOT_24TH = 1
animations.ONESHOT_16TH = 2
animations.ONESHOT_8TH = 3
animations.ONESHOT_QUARTER = 4
animations.ONESHOT_HALF = 5
animations.PULSING_24TH = 6
animations.PULSING_16TH = 7
animations.PULSING_8TH = 8
animations.PULSING_QUARTER = 9
animations.BLINKING_HALF = 10
animations.BLINKING_24TH = 6
animations.BLINKING_16TH = 7
animations.BLINKING_8TH = 8
animations.BLINKING_QUARTER = 9
animations.BLINKING_HALF = 10

controls = AttributeDict()
controls.BUTTON_TAP_TEMPO = 'Button.TapTempo.3.0'
controls.BUTTON_METRONOME = 'Button.Metronome.9.0'
controls.BUTTON_DELETE = 'Button.Delete.118.0'
controls.BUTTON_UNDO = 'Button.Undo.119.0'
controls.BUTTON_MUTE = 'Button.Mute.60.1'
controls.BUTTON_SOLO = 'Button.Solo.61.1'
controls.BUTTON_STOP = 'Button.Stop.29.1'
controls.BUTTON_CONVERT = 'Button.Convert.35.0'
controls.BUTTON_DOUBLE_LOOP = 'Button.DoubleLoop.117.0'
controls.BUTTON_QUANTIZE = 'Button.Quantize.116.0'
controls.BUTTON_DUPLICATE = 'Button.Duplicate.88.0'
controls.BUTTON_NEW = 'Button.New.87.0'
controls.BUTTON_FIXED_LENGTH = 'Button.FixedLength.90.0'
controls.BUTTON_AUTOMATE = 'Button.Automate.89.1'
controls.BUTTON_RECORD = 'Button.Record.86.1'
controls.BUTTON_PLAY = 'Button.Play.85.1'
controls.BUTTON_UPPER_1 = 'Button.Upper1.102.1'
controls.BUTTON_UPPER_2 = 'Button.Upper2.103.1'
controls.BUTTON_UPPER_3 = 'Button.Upper3.104.1'
controls.BUTTON_UPPER_4 = 'Button.Upper4.105.1'
controls.BUTTON_UPPER_5 = 'Button.Upper5.106.1'
controls.BUTTON_UPPER_6 = 'Button.Upper6.107.1'
controls.BUTTON_UPPER_7 = 'Button.Upper7.108.1'
controls.BUTTON_UPPER_8 = 'Button.Upper8.109.1'
controls.BUTTON_LOWER_1 = 'Button.Lower1.20.1'
controls.BUTTON_LOWER_2 = 'Button.Lower2.21.1'
controls.BUTTON_LOWER_3 = 'Button.Lower3.22.1'
controls.BUTTON_LOWER_4 = 'Button.Lower4.23.1'
controls.BUTTON_LOWER_5 = 'Button.Lower5.24.1'
controls.BUTTON_LOWER_6 = 'Button.Lower6.25.1'
controls.BUTTON_LOWER_7 = 'Button.Lower7.26.1'
controls.BUTTON_LOWER_8 = 'Button.Lower8.27.1'
controls.BUTTON_32T = 'Button.32T.43.1'
controls.BUTTON_32 = 'Button.32.42.1'
controls.BUTTON_16T = 'Button.16T.41.1'
controls.BUTTON_16 = 'Button.16.40.1'
controls.BUTTON_8T = 'Button.8T.39.1'
controls.BUTTON_8 = 'Button.8.38.1'
controls.BUTTON_4T = 'Button.4T.37.1'
controls.BUTTON_4 = 'Button.4.36.1'
controls.BUTTON_SETUP = 'Button.Setup.30.0'
controls.BUTTON_USER = 'Button.User.59.0'
controls.BUTTON_ADD_DEVICE = 'Button.AddDevice.52.0'
controls.BUTTON_ADD_TRACK = 'Button.AddTrack.53.0'
controls.BUTTON_DEVICE = 'Button.Device.110.0'
controls.BUTTON_BROWSE = 'Button.Browse.111.0'
controls.BUTTON_MIX = 'Button.Mix.112.0'
controls.BUTTON_CLIP = 'Button.Clip.113.0'
controls.BUTTON_MASTER = 'Button.Master.28.0'
controls.BUTTON_LEFT = 'Button.Left.44.0'
controls.BUTTON_RIGHT = 'Button.Right.45.0'
controls.BUTTON_UP = 'Button.Up.46.0'
controls.BUTTON_DOWN = 'Button.Down.47.0'
controls.BUTTON_REPEAT = 'Button.Repeat.56.0'
controls.BUTTON_ACCENT = 'Button.Accent.57.0'
controls.BUTTON_SCALE = 'Button.Scale.58.0'
controls.BUTTON_LAYOUT = 'Button.Layout.31.0'
controls.BUTTON_NOTE = 'Button.Note.50.0'
controls.BUTTON_SESSION = 'Button.Session.51.0'
controls.BUTTON_PAGE_LEFT = 'Button.PageLeft.62.0'
controls.BUTTON_PAGE_RIGHT = 'Button.PageRight.63.0'
controls.BUTTON_OCTAVE_UP = 'Button.OctaveUP.55.0'
controls.BUTTON_OCTAVE_DOWN = 'Button.OctaveDown.54.0'
controls.BUTTON_SHIFT = 'Button.Shift.49.0'
controls.BUTTON_SELECT = 'Button.Select.48.0'
controls.TOUCHSTRIP = 'Touchstrip.Touchstrip.1.12'
controls.ENCODER_TEMPO = 'Encoder.Tempo.14.10'
controls.ENCODER_SWING = 'Encoder.Swing.15.9'
controls.ENCODER_1 = 'Encoder.1.71.0'
controls.ENCODER_2 = 'Encoder.2.72.1'
controls.ENCODER_3 = 'Encoder.3.73.2'
controls.ENCODER_4 = 'Encoder.4.74.3'
controls.ENCODER_5 = 'Encoder.5.75.4'
controls.ENCODER_6 = 'Encoder.6.76.5'
controls.ENCODER_7 = 'Encoder.7.77.6'
controls.ENCODER_8 = 'Encoder.8.78.7'
controls.ENCODER_MASTER = 'Encoder.Master.79.8'
controls.PAD_81 = 'Pad.81.36.1'
controls.PAD_82 = 'Pad.82.37.1'
controls.PAD_83 = 'Pad.83.38.1'
controls.PAD_84 = 'Pad.84.39.1'
controls.PAD_85 = 'Pad.85.40.1'
controls.PAD_86 = 'Pad.86.41.1'
controls.PAD_87 = 'Pad.87.42.1'
controls.PAD_88 = 'Pad.88.43.1'
controls.PAD_71 = 'Pad.71.44.1'
controls.PAD_72 = 'Pad.72.45.1'
controls.PAD_73 = 'Pad.73.46.1'
controls.PAD_74 = 'Pad.74.47.1'
controls.PAD_75 = 'Pad.75.48.1'
controls.PAD_76 = 'Pad.76.49.1'
controls.PAD_77 = 'Pad.77.50.1'
controls.PAD_78 = 'Pad.78.51.1'
controls.PAD_61 = 'Pad.61.52.1'
controls.PAD_62 = 'Pad.62.53.1'
controls.PAD_63 = 'Pad.63.54.1'
controls.PAD_64 = 'Pad.64.55.1'
controls.PAD_65 = 'Pad.65.56.1'
controls.PAD_66 = 'Pad.66.57.1'
controls.PAD_67 = 'Pad.67.58.1'
controls.PAD_68 = 'Pad.68.59.1'
controls.PAD_51 = 'Pad.51.60.1'
controls.PAD_52 = 'Pad.52.61.1'
controls.PAD_53 = 'Pad.53.62.1'
controls.PAD_54 = 'Pad.54.63.1'
controls.PAD_55 = 'Pad.55.64.1'
controls.PAD_56 = 'Pad.56.65.1'
controls.PAD_57 = 'Pad.57.66.1'
controls.PAD_58 = 'Pad.58.67.1'
controls.PAD_41 = 'Pad.41.68.1'
controls.PAD_42 = 'Pad.42.69.1'
controls.PAD_43 = 'Pad.43.70.1'
controls.PAD_44 = 'Pad.44.71.1'
controls.PAD_45 = 'Pad.45.72.1'
controls.PAD_46 = 'Pad.46.73.1'
controls.PAD_47 = 'Pad.47.74.1'
controls.PAD_48 = 'Pad.48.75.1'
controls.PAD_31 = 'Pad.31.76.1'
controls.PAD_32 = 'Pad.32.77.1'
controls.PAD_33 = 'Pad.33.78.1'
controls.PAD_34 = 'Pad.34.79.1'
controls.PAD_35 = 'Pad.35.80.1'
controls.PAD_36 = 'Pad.36.81.1'
controls.PAD_37 = 'Pad.37.82.1'
controls.PAD_38 = 'Pad.38.83.1'
controls.PAD_21 = 'Pad.21.84.1'
controls.PAD_22 = 'Pad.22.85.1'
controls.PAD_23 = 'Pad.23.86.1'
controls.PAD_24 = 'Pad.24.87.1'
controls.PAD_25 = 'Pad.25.88.1'
controls.PAD_26 = 'Pad.26.89.1'
controls.PAD_27 = 'Pad.27.90.1'
controls.PAD_28 = 'Pad.28.91.1'
controls.PAD_11 = 'Pad.11.92.1'
controls.PAD_12 = 'Pad.12.93.1'
controls.PAD_13 = 'Pad.13.94.1'
controls.PAD_14 = 'Pad.14.95.1'
controls.PAD_15 = 'Pad.15.96.1'
controls.PAD_16 = 'Pad.16.97.1'
controls.PAD_17 = 'Pad.17.98.1'
controls.PAD_18 = 'Pad.18.99.1'

PADS_64 = ['Pad.81.36.1',
           'Pad.82.37.1',
           'Pad.83.38.1',
           'Pad.84.39.1',
           'Pad.71.44.1',
           'Pad.72.45.1',
           'Pad.73.46.1',
           'Pad.74.47.1',
           'Pad.61.52.1',
           'Pad.62.53.1',
           'Pad.63.54.1',
           'Pad.64.55.1',
           'Pad.51.60.1',
           'Pad.52.61.1',
           'Pad.53.62.1',
           'Pad.54.63.1',
           'Pad.41.68.1',
           'Pad.42.69.1',
           'Pad.43.70.1',
           'Pad.44.71.1',
           'Pad.31.76.1',
           'Pad.32.77.1',
           'Pad.33.78.1',
           'Pad.34.79.1',
           'Pad.21.84.1',
           'Pad.22.85.1',
           'Pad.23.86.1',
           'Pad.24.87.1',
           'Pad.11.92.1',
           'Pad.12.93.1',
           'Pad.13.94.1',
           'Pad.14.95.1',
           'Pad.85.40.1',
           'Pad.86.41.1',
           'Pad.87.42.1',
           'Pad.88.43.1',
           'Pad.75.48.1',
           'Pad.76.49.1',
           'Pad.77.50.1',
           'Pad.78.51.1',
           'Pad.65.56.1',
           'Pad.66.57.1',
           'Pad.67.58.1',
           'Pad.68.59.1',
           'Pad.55.64.1',
           'Pad.56.65.1',
           'Pad.57.66.1',
           'Pad.58.67.1',
           'Pad.45.72.1',
           'Pad.46.73.1',
           'Pad.47.74.1',
           'Pad.48.75.1',
           'Pad.35.80.1',
           'Pad.36.81.1',
           'Pad.37.82.1',
           'Pad.38.83.1',
           'Pad.25.88.1',
           'Pad.26.89.1',
           'Pad.27.90.1',
           'Pad.28.91.1',
           'Pad.15.96.1',
           'Pad.16.97.1',
           'Pad.17.98.1',
           'Pad.18.99.1']

PADS_XY = [['Pad.11.92.1',
            'Pad.12.93.1',
            'Pad.13.94.1',
            'Pad.14.95.1',
            'Pad.15.96.1',
            'Pad.16.97.1',
            'Pad.17.98.1',
            'Pad.18.99.1'],
           ['Pad.21.84.1',
            'Pad.22.85.1',
            'Pad.23.86.1',
            'Pad.24.87.1',
            'Pad.25.88.1',
            'Pad.26.89.1',
            'Pad.27.90.1',
            'Pad.28.91.1'],
           ['Pad.31.76.1',
            'Pad.32.77.1',
            'Pad.33.78.1',
            'Pad.34.79.1',
            'Pad.35.80.1',
            'Pad.36.81.1',
            'Pad.37.82.1',
            'Pad.38.83.1'],
           ['Pad.41.68.1',
            'Pad.42.69.1',
            'Pad.43.70.1',
            'Pad.44.71.1',
            'Pad.45.72.1',
            'Pad.46.73.1',
            'Pad.47.74.1',
            'Pad.48.75.1'],
           ['Pad.51.60.1',
            'Pad.52.61.1',
            'Pad.53.62.1',
            'Pad.54.63.1',
            'Pad.55.64.1',
            'Pad.56.65.1',
            'Pad.57.66.1',
            'Pad.58.67.1'],
           ['Pad.61.52.1',
            'Pad.62.53.1',
            'Pad.63.54.1',
            'Pad.64.55.1',
            'Pad.65.56.1',
            'Pad.66.57.1',
            'Pad.67.58.1',
            'Pad.68.59.1'],
           ['Pad.71.44.1',
            'Pad.72.45.1',
            'Pad.73.46.1',
            'Pad.74.47.1',
            'Pad.75.48.1',
            'Pad.76.49.1',
            'Pad.77.50.1',
            'Pad.78.51.1'],
           ['Pad.81.36.1',
            'Pad.82.37.1',
            'Pad.83.38.1',
            'Pad.84.39.1',
            'Pad.85.40.1',
            'Pad.86.41.1',
            'Pad.87.42.1',
            'Pad.88.43.1']]
