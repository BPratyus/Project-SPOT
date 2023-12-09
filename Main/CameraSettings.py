import requests

# ESP32 URL
# URL = "http://192.168.137.133"
AWB = True

def set_resolution(url: str, index: int=8):
    #  resolutions = "10: UXGA(1600x1200)\n
    # 9: SXGA(1280x1024)\n
    # 8: XGA(1024x768)\n
    # 7: SVGA(800x600)\n
    # 6: VGA(640x480)\n
    # 5: CIF(400x296)\n
    # 4: QVGA(320x240)\n
    # 3: HQVGA(240x176)\n
    # 0: QQVGA(160x120)"
    try:
        if index in [10, 9, 8, 7, 6, 5, 4, 3, 0]:
            requests.get(url + "/control?var=framesize&val={}".format(index))
            # print("Resolution set successfully.")
        else:
            print("Wrong index")
    except:
        print("SET_RESOLUTION: something went wrong")

def set_brightness(url: str, value: int=2):
    try:
        if -2 <= value <= 2:
            requests.get(url + "/control?var=brightness&val={}".format(value))
            # print("Brightness set successfully.")
        else:
            print("Invalid brightness value. It should be between -2 and 2.")
    except:
        print("SET_BRIGHTNESS: something went wrong")

def set_quality(url: str, value: int=6):
    try:
        if 4 <= value <= 63:
            requests.get(url + "/control?var=quality&val={}".format(value))
            # print("Quality set successfully.")
        else:
            print("Invalid quality value. It should be between 10 and 63.")
    except:
        print("SET_QUALITY: something went wrong")

def set_ae_level(url: str, level: int=0):
    try:
        if -2 <= level <= 2:
            requests.get(url + "/control?var=ae_level&val={}".format(level))
            # print("AE Level set successfully.")
        else:
            print("Invalid AE Level value. It should be between 0 and 120.")
    except:
        print("SET_AE_LEVEL: something went wrong")

def set_gain_ceiling(url: str, ceiling: int=8):
    # 0 1 2 3 4 5 6
    # 2 4 8 16 32 64
    try:
        if ceiling in [2, 4, 8, 16, 32, 64, 128]:
            requests.get(url + "/control?var=gainceiling&val={}".format(ceiling))
            # print("Gain Ceiling set successfully.")
        else:
            print("Invalid Gain Ceiling value. It should be a power of 2 (2, 4, 8, 16, 32, 64).")
    except:
        print("SET_GAIN_CEILING: something went wrong")

def set_awb(url: str, awb: int=1):
    try:
        # awb = not awb
        requests.get(url + "/control?var=awb&val={}".format(1 if awb else 0))
        # print("AWB set successfully.")
    except:
        print("SET_QUALITY: something went wrong")
    return awb

def setCamera(URL):
    set_resolution(URL)
    set_brightness(URL)
    set_quality(URL)
    set_ae_level(URL)
    set_gain_ceiling(URL)
    set_awb(URL, AWB)

# setCamera(192.168.137.232)