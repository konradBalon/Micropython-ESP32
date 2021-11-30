from wifi_connect import WifiConnection

def make_connection():
    con = WifiConnection(essid='<wifi SSID>',password='<wifi password>')
    con.do_connect()
    con.http_get('http://developer.mozilla.org/')
