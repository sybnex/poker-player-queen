
class Player:
    VERSION = "Queen Python folding player"

    def betRequest(self, game_state):

        player = game_state[players]
        bet = 0
        for i in players: 
            bet += players[i][bet]

        call = game_state[current_buy_in]

        return call - bet + 1

    def showdown(self, game_state):
        pass

