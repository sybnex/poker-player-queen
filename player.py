
class Player:
    VERSION = "Queen Python folding player"
    goodCards = 0

    def betRequest(self, game_state):

        pId  = game_state["in_action"]
        bet  = game_state["players"][pId]["bet"]
        call = game_state["current_buy_in"]

        response = call - bet + game_state["minimum_raise"]

        ranked = False
        suited = False
        try:
            card1r = game_state["players"][pId]["hole_cards"][0]["rank"]
            card2r = game_state["players"][pId]["hole_cards"][1]["rank"]
            card1s = game_state["players"][pId]["hole_cards"][0]["suit"]
            card2s = game_state["players"][pId]["hole_cards"][1]["suit"]

            if card1r == card2r: ranked = True
            if card1s == card2s: suited = True

            rankRange = ("8","9","J","K","Q","A")
            if card1r in rankRange and card2r in rankRange: self.goodCards = True

        except:
            print("ERROR ON CARD CALC")

        if suited and self.goodCards: bet += 200
        elif self.goodCards:          bet += 100
        elif ranked or suited:        bet += 50
        elif game_state["current_buy_in"] > 250: return 0
        else:                                    return 0

        if   response < 0: return 0
        else:              return response

        #return game_state["players"][pId]["stack"] # allIn

def showdown(self, game_state):
        print(str(game_state))
        pass

