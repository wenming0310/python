"""
#! /usr/local/python3
import urllib
import http
import time
import socket

timeout = 10
socket.setdefaulttimeout(timeout)


def up_post(username, password, page):
    data = {'username': username, 'password' : password}
    url = r"http://192.168.2.8/?page" + page
    postdata = bytes(urllib.parse.urlencode(data), encoding='gbk')
    response = urllib.request.urlopen(url, data=postdata)
    text = response.read().decode('gbk')
    print(text)
    if text.find("成功") != -1:
        return page + ":" + text
    else:
        return page + ":error"

username = "aaa"
password = "bbb"
page = 1
while page <= 99:
    try:
        static = up_post(username, password, page)
    except ( http.client.IncompleteRead, urllib.error.URLError, socket.timeout, ConnectionResetError) as e:
        time.sleep(5)
        static = up_post(username, password, page)
        while True:
            if static == page + ":" + static or static == page + ":error" or static == "":
                break
"""
import socket
import retrying
import urllib.request

@retrying.retry(stop_max_attempt_number=3)
def openURL():
    print(1)
    # timeout in seconds
    timeout = 10
    socket.setdefaulttimeout(timeout)
    # this call to urllib.request.urlopen now uses the default timeout
    # we have set in the socket module
    #req = urllib.request.Request('https://www.python.org/')
    #a = urllib.request.urlopen(req).read()
    page = urllib.request.urlopen('https://www.python.org/')
    print(2)
    a = page.read().decode("utf8")
    print(a)
openURL()