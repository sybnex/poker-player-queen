
class Player:
    VERSION = "Queen Python folding player"

    def bet_request(self, game_state):
        return self.betRequest(game_state)

    def betRequest(self, game_state):

        players = game_state["players"]
        bet = 0
        #for i in range(len(players)):
        #    if players[i]["status"] == "active":
        #        bet += players[i]["bet"]

        bet  = game_state["players"][game_state["in_action"]]["bet"]
        call = game_state["current_buy_in"]

        response = call - bet + game_state["minimum_raise"]
        if response < 0: return 0 
        else:            return response

    def showdown(self, game_state):
        pass

