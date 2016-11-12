# -*- coding: utf-8 -*-

import websocket

class WebSocket:
    
    def __init__(self, ai):
        url = "ws://www.logos.t.u-tokyo.ac.jp/mjai/";
        self.ai = ai
        ai.ws = self
    
        # websocket.enableTrace(True)
        self.ws = websocket.WebSocketApp(url,
                                  on_message = self.on_message,
                                  on_error = self.on_error,
                                  on_close = self.on_close,
                                  on_open = self.on_open)
           
    def start(self):
        self.ws.run_forever()  

    def send(self, message):
        print "send: {}".format(message)
        self.ws.send(message)
    
    def close(self):
        self.ws.close()

    def on_message(self, ws, message):
        # print "debug: called on_message"
        # print message
        self.ai.get_message(message)
        
    def on_error(self, ws, error):
        print "debug: called on_error"
        print error
    
    def on_close(self, ws):
        print "### closed ###"
    
    def on_open(self, ws):
        print "### open ###"
        
                   
