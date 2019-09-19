
class Player:
    VERSION = "Queen Python folding player"

    def bet_request(self, game_state):
        return self.betRequest(game_state)

    def betRequest(self, game_state):

        players = game_state["players"]
        bet = 0
        print(len(players))
        bet += players[0]["bet"]
        bet += players[1]["bet"]
        bet += players[2]["bet"]
        bet += players[3]["bet"]

        
        call = game_state["current_buy_in"]

        return call - bet + 1

    def showdown(self, game_state):
        pass

