#!/usr/bin/python
# -*- coding: utf-8 -*-

from websocketmj import WebSocket
import json

def game_main():

  ai = AI()
  ws = WebSocket(ai)
  ws.start()

class AI:
    # ws: WebSocket
    def __init__(self):
        self.player_number = -1

    def get_message(self, message):
        j = json.loads(message)
        print j
        # print j["type"]
        
        if j["type"] == "error":
            # print "error occured"            
            # print j
            self.ws.close()

        elif j["type"] == "end_game":
            print "game ended"            
            self.ws.close()
            
        else:
            res = self.response(j)
            m = json.dumps(res)
            # print m
            self.ws.send(m)
            
    def response(self, j):
        
        res = {}
        
        if j["type"] == "hello":
            res["type"] = "join"
            res["name"] = "tsumogiri_python"
            res["room"] = "default"                           
        if j["type"] == "start_game":
            self.player_number = (int)(j["id"])
            res["type"] = "none"                
        if j["type"] == "start_kyoku":
            res["type"] = "none"

        if j["type"] == "tsumo":            
            if self.player_number==(int)(j["actor"]):
                res["type"] = "dahai"
                res["actor"] = self.player_number
                res["pai"] = j["pai"]
                res["tsumogiri"] = True
            else:
                res["type"] = "none"

        if j["type"] == "dahai":
            res["type"] = "none"
        if j["type"] == "pon":
            res["type"] = "none"
        if j["type"] == "chi":
            res["type"] = "none"
        if j["type"] == "kakan":
            res["type"] = "none"
        if j["type"] == "daiminkan":
            res["type"] = "none"
        if j["type"] == "ankan":
            res["type"] = "none"
            
        if j["type"] == "dora":
            res["type"] = "none"
        if j["type"] == "reach":
            res["type"] = "none"
        if j["type"] == "reach_accepted":
            res["type"] = "none"
        if j["type"] == "hora":
            res["type"] = "none"
        if j["type"] == "ryukyoku":
            res["type"] = "none"
        if j["type"] == "end_kyoku":
            res["type"] = "none"
        if j["type"] == "end_game":
            res["type"] = "none"
        if j["type"] == "hora":
            res["type"] = "none"
        
        return res
              
if __name__ == "__main__":
    game_main()