class icd_params:
    INDEX_MESSAGE_COUNTER = 0
    INDEX_MESSAGE_TYPE = 4
    INDEX_RESERVED_0 = 8
    INDEX_MESSAGE_SIZE = 12
    INDEX_UPDATE_TIME_TAG = 16
    INDEX_CHUNK_NUMBER = 24
    INDEX_TOTAL_NUMBER_OF_REPORTED_TRACKS = 26
    INDEX_RESERVED_1 = 28
    INDEX_NUMBER_OF_TRACKS_IN_THIS_MESSAGE = 30
    INDEX_TRACKS_TIME_TAG_YEAR = 32
    INDEX_TRACKS_TIME_TAG_MONTH = 34
    INDEX_TRACKS_TIME_TAG_DAY_OF_MONTH = 36
    INDEX_TRACKS_TIME_TAG_HOUR = 38
    INDEX_TRACKS_TIME_TAG_MINUTE = 40
    INDEX_TRACKS_TIME_TAG_SECOND = 42
    INDEX_TRACKS_TIME_TAG_MILLISECONDS = 44
    INDEX_RESERVED_2 = 46
    INDEX_TRACK_ID = 48
    INDEX_TRACK_TARGET_TYPE = 52
    INDEX_TRACK_POO_LATITUDE = 56
    INDEX_TRACK_POO_LONGITUDE = 64
    INDEX_TRACK_POO_ALTITUDE = 72
    INDEX_TRACK_POI_ALTITUDE = 76
    INDEX_TRACK_POI_LATITUDE = 80
    INDEX_TRACK_POI_LONGITUDE = 88
    INDEX_TRACK_LATITUDE = 96
    INDEX_TRACK_LONGITUDE = 104
    INDEX_TRACK_ALTITUDE = 112
    INDEX_TRACK_DOPPLER_VELOCITY = 116
    INDEX_TRACK_RADAR_CROSS_SECTION = 120
    INDEX_TRACK_RESERVED_0 = 124
    INDEX_TRACK_POO_CEP = 128
    INDEX_TRACK_POI_CEP = 132
    INDEX_TRACK_POO_ERROR_ELLIPSE_MAJOR_AXIS = 136
    INDEX_TRACK_POO_ERROR_ELLIPSE_MINOR_AXIS = 140
    INDEX_TRACK_POO_ERROR_ELLIPSE_HEADING = 144
    INDEX_TRACK_POI_ERROR_ELLIPSE_MAJOR_AXIS = 148
    INDEX_TRACK_POI_ERROR_ELLIPSE_MINOR_AXIS = 152
    INDEX_TRACK_POI_ERROR_ELLIPSE_HEADING = 156
    INDEX_TRACK_MUZZLE_VELOCITY = 160
    INDEX_TRACK_IMPACT_VELOCITY = 164
    INDEX_TRACK_STATUS_FLAGS = 168
    INDEX_TRACK_RESERVED_1 = 170
    INDEX_TRACK_TIME_TO_POO = 172
    INDEX_TRACK_TIME_TO_POI = 176
    INDEX_TRACK_TOTAL_NUMBER_OF_ASSOCIATED_PLOTS = 180
    INDEX_TRACK_TIME_SINCE_LAST_ASSOCIATION = 184
    INDEX_TRACK_AGE = 188
    INDEX_TRACK_POSITION_X = 192
    INDEX_TRACK_POSITION_Y = 196
    INDEX_TRACK_POSITION_Z = 200
    INDEX_TRACK_VELOCITY_X = 204
    INDEX_TRACK_VELOCITY_Y = 208
    INDEX_TRACK_VELOCITY_Z = 212
    INDEX_TRACK_POSITION_ERROR_X = 216
    INDEX_TRACK_POSITION_ERROR_Y = 220
    INDEX_TRACK_POSITION_ERROR_Z = 224
    INDEX_TRACK_VELOCITY_ERROR_X = 228
    INDEX_TRACK_VELOCITY_ERROR_Y = 232
    INDEX_TRACK_VELOCITY_ERROR_Z = 236
    INDEX_TRACK_TEST_PARAMETER_0 = 240
    INDEX_TRACK_TEST_PARAMETER_1 = 244
    INDEX_TRACK_TEST_PARAMETER_2 = 248
    INDEX_TRACK_TEST_PARAMETER_3 = 252
    INDEX_TRACK_TEST_PARAMETER_4 = 256
    INDEX_TRACK_TEST_PARAMETER_5 = 260
    INDEX_TRACK_TEST_PARAMETER_6 = 264
    INDEX_TRACK_TEST_PARAMETER_7 = 268
    INDEX_TRACK_TEST_PARAMETER_8 = 272
    INDEX_TRACK_TEST_PARAMETER_9 = 276

    # TRACKS_EXTENDED_message extra features
    INDEX_TRACK_ASSOCIATED_PLOT_RANGE = 2368
    INDEX_TRACK_ASSOCIATED_PLOT_RANGE_STANDARD_DEVIATION = 2372
    INDEX_TRACK_ASSOCIATED_PLOT_DOPPLER_VELOCITY = 2376
    INDEX_TRACK_ASSOCIATED_PLOT_DOPPLER_VELOCITY_STANDARD_DEVIATION = 2380
    INDEX_TRACK_ASSOCIATED_PLOT_AZIMUTH = 2384
    INDEX_TRACK_ASSOCIATED_PLOT_AZIMUTH_STANDARD_DEVIATION = 2388
    INDEX_TRACK_ASSOCIATED_PLOT_ELEVATION = 2392
    INDEX_TRACK_ASSOCIATED_PLOT_ELEVATION_STANDARD_DEVIATION = 2396
    INDEX_TRACK_ASSOCIATED_PLOT_SIGNAL_TO_NOISE_RATIO = 2400
    INDEX_TRACK_ASSOCIATED_PLOT_RADAR_CROSS_SECTION = 2404
    INDEX_TRACK_RESERVED_2 = 2408

    # TRACKS_EXTENDED_message_2 extra features
    INDEX_TRACK_ACCELERATION_X = 2368
    INDEX_TRACK_ACCELERATION_Y = 2372
    INDEX_TRACK_ACCELERATION_Z = 2376
    INDEX_TRACK_POH_LATITUDE = 2380
    INDEX_TRACK_POH_LONGITUDE = 2388
    INDEX_TRACK_POH_ALTITUDE = 2396
    INDEX_TRACK_POE_LATITUDE = 2400
    INDEX_TRACK_POE_LONGITUDE = 2408
    INDEX_TRACK_POE_ALTITUDE = 2416

    # A radar sends only one of TRACKS, TRACKS_EXTENDED (ref. §4.4.3.6 ),
    # or TRACKS_EXTENDED_2 (ref. §4.4.3.7 ) messages.
    # This selection is defined by the specific radar configuration.
    # Here are the size of message for each kind of message the radar sends.
    TRACKS_MESSAGE_SIZE = 2368
    TRACKS_EXTENDED_MESSAGE_SIZE = 2808
    TRACKS_EXTENDED_2_MESSAGE_SIZE = 2888

    # For each track_id in a plot, the constants below describe the size of information of each track_id.
    # TRACK_ID_ASSOCIATED_PLOT_DATA_SIZE is the size of the more information for track_id that can be found in
    # TRACKS_EXTENDED message, in byte 2368 and so on
    TRACK_ID_BASIC_DATA_SIZE = 232
    TRACK_ID_EXTEND_DATA_SIZE = 44
    TRACK_ID_EXTEND_2_DATA_SIZE = 52

    NUMBER_OF_TRACKS_IN_MESSAGE = 10

    # research futures:
    ELEVATION = "Elevation"

    AZIMUTH = "Azimuth"

    VEL_DOPP = "VelDopp"

    RANGE = "Range"

    EXT_ID = "ExtID"

    ASSOC = "Assoc"

    ID = "ID"

    DATE_TIME = "DateTime"

    ALT = "Alt"

    POS_NORTH = "PosNorth"

    RCS = "RCS"

    ACCEL_UP = "AccelUp"

    ACCEL_WEST = "AccelWest"

    ACCEL_NORTH = "AccelNorth"

    ASPECT = "Aspect"

    VEL_UP = "VelUp"

    VEL_WEST = "VelWest"

    VEL_NORTH = "VelNorth"

    POS_UP = "PosUp"

    POS_WEST = "PosWest"

    TRACK_TIME = "TrackTime"

    default_columns = [
        TRACK_TIME,
        ID,
        ASSOC,
        EXT_ID,
        RANGE,
        VEL_DOPP,
        AZIMUTH,
        ELEVATION,
        ALT,
        POS_NORTH,
        POS_WEST,
        POS_UP,
        VEL_NORTH,
        VEL_WEST,
        VEL_UP,
        ASPECT,
        RCS,
        "TgtRange",
        "TgtRangeStd",
        "TgtVel",
        "TgtVelStd",
        "TgtAz",
        "TgtAzStd",
        "TgtEl",
        "TgtElStd",
        "TgtSNR",
        "TgtRCSAct",
    ]