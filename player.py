
class Player:
    VERSION = "Queen Python folding player"

    def bet_request(self, game_state):
        return self.betRequest(game_state)

    def betRequest(self, game_state):

        players = game_state["players"]
        bet = 0
        print(players)
        for player in players: 
            bet += players[player]["bet"]

        
        call = game_state["current_buy_in"]

        return call - bet + 1

    def showdown(self, game_state):
        pass

