import pywifi

wifi = pywifi.PyWiFi()
iface = wifi.interfaces()[0]

iface.scan()
result = iface.scan_results()
for i in range(len(result)):
    print(result[i].ssid, result[i].signal)

