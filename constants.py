class AttrDict(dict):
    __getattr__ = dict.__getitem__
    __setattr__ = dict.__setitem__

VOL_INC = 0.0066
PAN_INC = 0.0066

ENCODERS_TARGET = AttrDict()
ENCODERS_TARGET.CHANNEL_VOL = 1
ENCODERS_TARGET.CHANNEL_PAN = 2
ENCODERS_TARGET.CHANNEL_TRACK = 3
ENCODERS_TARGET.TRACK_VOL = 1
ENCODERS_TARGET.TRACK_PAN = 2
ENCODERS_TARGET.TRACK_SEND_1 = 3
ENCODERS_TARGET.TRACK_SEND_2 = 4
ENCODERS_TARGET.TRACK_SEND_3 = 5
ENCODERS_TARGET.TRACK_SEND_4 = 6
ENCODERS_TARGET.TRACK_SEND_5 = 7
ENCODERS_TARGET.TRACK_SEND_6 = 8
ENCODERS_TARGET.CLIP_VOL = 1

colors = AttrDict()
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

# https://cycling74.com/forums/push-2-color-codes
# https://www.colorhexa.com/
RGB_MAP = {
    # 0 : (0,0,0), # RGB_BLACK
    # 3 : (100,65,0), # RGB_ORANGE
    # 8 : (100,100,0), # RGB_YELLOW
    # 15 : (25,88,82), # RGB_TURQUOISE
    # 22 : (50,0,50), # RGB_PURPLE
    # 25 : (100,75,80), # RGB_PINK
    # 122 : (204,204,204), # RGB_WHITE
    # 123 : (64,64,64), # RGB_LIGHT_GRAY
    # 124 : (20,20,20), # RGB_DARK_GRAY
    # 125 : (0,0,255), # RGB_BLUE
    # 126 : (0,255,0), # RGB_GREEN
    # 127 : (255,0,0) # RGB_RED
    0 : (0,0,0,0),
    1 : (255,64,50,2),
    2 : (1,4,0,4),
    3 : (147,60,0,6),
    4 : (89,31,0,8),
    5 : (25,80,24,10),
    6 : (73,24,4,12),
    7 : (245,185,59,14),
    8 : (255,139,22,16),
    9 : (109,255,14,18),
    10 : (121,255,24,20),
    11 : (52,133,22,22),
    12 : (79,21,4,24),
    13 : (98,255,85,26),
    14 : (41,125,83,28),
    15 : (38,61,114,30),
    16 : (49,91,255,32),
    17 : (54,99,249,34),
    18 : (26,52,255,36),
    19 : (28,12,205,38),
    20 : (21,57,51,40),
    21 : (57,55,255,42),
    22 : (87,34,255,44),
    23 : (47,43,255,46),
    24 : (11,33,120,48),
    25 : (255,16,50,50),
    26 : (255,43,169,52),
    27 : (77,52,33,54),
    28 : (51,86,40,56),
    29 : (15,103,0,58),
    30 : (33,5,31,60),
    31 : (74,15,0,62),
    32 : (0,127,18,64),
    33 : (24,83,101,66),
    34 : (98,75,91,68),
    35 : (115,58,103,70),
    36 : (241,121,95,72),
    37 : (255,55,118,74),
    38 : (255,127,95,76),
    39 : (179,95,113,78),
    40 : (255,233,1,80),
    41 : (127,117,105,80),
    42 : (121,153,17,81),
    43 : (93,255,51,81),
    44 : (124,187,63,82),
    45 : (19,105,125,82),
    46 : (1,231,255,83),
    47 : (122,157,249,83),
    48 : (104,67,167,84),
    49 : (11,31,133,85),
    50 : (119,85,229,85),
    51 : (155,119,201,86),
    52 : (223,23,97,86),
    53 : (11,59,25,87),
    54 : (107,117,110,87),
    55 : (9,33,55,88),
    56 : (106,112,117,88),
    57 : (17,11,59,89),
    58 : (108,106,117,90),
    59 : (59,11,57,90),
    60 : (116,106,116,91),
    61 : (57,59,11,91),
    62 : (116,117,106,92),
    63 : (59,9,9,92),
    64 : (117,106,106,93),
    65 : (102,25,20,93),
    66 : (33,8,6,94),
    67 : (70,3,0,94),
    68 : (40,0,0,95),
    69 : (93,23,0,96),
    70 : (32,13,0,96),
    71 : (71,12,0,97),
    72 : (28,8,0,97),
    73 : (59,43,20,98),
    74 : (28,19,10,98),
    75 : (37,14,5,99),
    76 : (13,6,2,99),
    77 : (100,88,23,100),
    78 : (32,28,7,101),
    79 : (102,78,8,101),
    80 : (33,25,2,102),
    81 : (72,102,5,102),
    82 : (23,33,1,103),
    83 : (48,102,9,103),
    84 : (15,33,3,104),
    85 : (20,77,8,104),
    86 : (6,25,2,105),
    87 : (31,55,1,106),
    88 : (10,17,0,106),
    89 : (39,102,34,107),
    90 : (12,33,11,107),
    91 : (20,62,41,108),
    92 : (8,25,16,108),
    93 : (0,77,54,109),
    94 : (0,24,14,109),
    95 : (19,69,102,110),
    96 : (6,22,33,110),
    97 : (21,39,100,111),
    98 : (7,12,32,112),
    99 : (10,20,102,112),
    100 : (3,6,33,113),
    101 : (11,4,92,113),
    102 : (3,1,29,114),
    103 : (10,28,76,114),
    104 : (4,11,30,115),
    105 : (22,22,102,115),
    106 : (7,7,33,116),
    107 : (34,13,102,117),
    108 : (11,4,33,117),
    109 : (60,17,102,118),
    110 : (19,5,33,118),
    111 : (53,13,48,119),
    112 : (17,4,15,119),
    113 : (102,6,20,120),
    114 : (33,2,6,120),
    115 : (102,17,84,121),
    116 : (33,5,27,122),
    117 : (0,0,0,122),
    118 : (89,89,89,123),
    119 : (26,26,26,123),
    120 : (255,255,255,124),
    121 : (89,89,89,124),
    122 : (153,153,153,125),
    123 : (64,64,64,125),
    124 : (20,20,20,126),
    125 : (0,0,255,126),
    126 : (0,255,0,127),
    127 : (255,0,0,1)
}

animations = AttrDict()
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
animations.PULSING_HALF = 10
animations.BLINKING_24TH = 6
animations.BLINKING_16TH = 7
animations.BLINKING_8TH = 8
animations.BLINKING_QUARTER = 9
animations.BLINKING_HALF = 10

controls = AttrDict()
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
controls.BUTTON_SCENE_1 = 'Button.Scene1.43.1'
controls.BUTTON_SCENE_2 = 'Button.Scene2.42.1'
controls.BUTTON_SCENE_3 = 'Button.Scene3.41.1'
controls.BUTTON_SCENE_4 = 'Button.Scene4.40.1'
controls.BUTTON_SCENE_5 = 'Button.Scene5.39.1'
controls.BUTTON_SCENE_6 = 'Button.Scene6.38.1'
controls.BUTTON_SCENE_7 = 'Button.Scene7.37.1'
controls.BUTTON_SCENE_8 = 'Button.Scene8.36.1'
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

PADS_H = 8
PADS_W = 8
PADS_N = 64

PADS = [value for (key, value) in sorted(controls.items()) if key.startswith("PAD")]
BUTTONS = [value for (key, value) in sorted(controls.items()) if key.startswith("BUTTON")]
BUTTONS_UPPER = [value for (key, value) in sorted(controls.items()) if key.startswith("BUTTON_UPPER")]
BUTTONS_LOWER = [value for (key, value) in sorted(controls.items()) if key.startswith("BUTTON_LOWER")]
ENCODERS = [value for (key, value) in sorted(controls.items()) if key.startswith("ENCODER")]

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
