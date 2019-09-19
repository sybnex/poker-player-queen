
class Player:
    VERSION = "Queen Python folding player"

    def bet_request(self, game_state):
        return self.betRequest(game_state)

    def betRequest(self, game_state):

        pId  = game_state["in_action"]
        bet  = game_state["players"][pId]["bet"]
        call = game_state["current_buy_in"]

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
            print("ERROR ON CALC")

        if game_state["round"] == 2 or suited:
            return game_state["players"][pId]["stack"]

        response = call - bet + game_state["minimum_raise"]
        if response < 0: return 1
        else:            return response

    def showdown(self, game_state):
        pass

