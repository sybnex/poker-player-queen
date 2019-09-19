
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
        except:
            print("ERROR ON CARD CALC")

        rankRange = ("9","J","K","Q","A")
        if suited and card1r in rankRange and card2r in rankRange: 
            goodCards = 1
            bet += 100
        elif card1r in rankRange and card2r in rankRange: 
            goodCards = 1
            bet += 100

        if ranked or suited:
            bet += 50
            #return game_state["players"][pId]["stack"]

        if   response < 0: return 1
        else:              return response

    def showdown(self, game_state):
        print(str(game_state))
        pass

