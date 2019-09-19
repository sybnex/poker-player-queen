
class Player:
    VERSION = "Queen Python folding player"

    def betRequest(self, game_state):

        pId  = game_state["in_action"]
        bet  = game_state["players"][pId]["bet"]
        call = game_state["current_buy_in"]

        response = call - bet + game_state["minimum_raise"]

        players   = len(game_state["players"])
        highStack = 0
        pl = -1
        for player in range(players):
            if game_state["players"][player]["stack"] > highStack:
                highStack = game_state["players"][player]["stack"]
                pl = player

#        if pl == pId: 
#            time.sleep(5)
#            if   response < 0: return 1
#            else:              return response

        ranked = False
        suited = False
        try:
            card1r = game_state["players"][pId]["hole_cards"][0]["rank"]
            card2r = game_state["players"][pId]["hole_cards"][1]["rank"]
            card1s = game_state["players"][pId]["hole_cards"][0]["suit"]
            card2s = game_state["players"][pId]["hole_cards"][1]["suit"]
            if card1r == card2r: ranked = True
            if card1s == card2s: suited = True
        except:
            print("ERROR ON CARD CALC")

        if ranked or suited:
            bet += 100
            #return game_state["players"][pId]["stack"]

        if   response < 0: return 1
        else:              return response

    def showdown(self, game_state):
        print(str(game_state))
        pass

