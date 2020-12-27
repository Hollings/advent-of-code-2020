import sys, os

class Game:
    def __init__(self, players, depth = 0):
        self.rounds = []
        self.depth = depth
        self.players = players
        self.totalCards = (self.players[0].deck + self.players[1].deck)
        pass

    def part1(self):
        for player in players:
            print(player.score())

    def checkEnd(self):
        for player in self.players:
            if len(player.deck) == len(self.totalCards):
                return player
        return None

    def play(self):
        winner = None
        while not winner:
            if len(self.rounds) % 1000 == 0 and self.rounds != []:
                print(f"---- ROUND {len(self.rounds) + 1} GAME {self.depth}----")
                print(self)
            # If this outcome already exists, p1 wins
            if str(self) not in self.rounds:
                self.rounds.append(str(self))
            else:
                # print("Player 1 wins by round copy")
                return self.players[0]

            # Take a turn
            self.turnPart2()
            winner = self.checkEnd()
        # self.part1()
        return winner

    def turnPart2(self):
        # If both players have at least as many cards remaining in their deck as
        # the value of the card they just drew, the winner of the round is determined
        # by playing a new game of Recursive Combat

        # Otherwise, at least one player must not have enough cards left in their
        # deck to recurse; the winner of the round is the player with the higher-value card.
        highCard = {
            'val': 0,
            'player': None
        }

        playedCards = []
        recurse = True
        for player in self.players:
            playedCards.append(player.play())

            if playedCards[-1].value > len(player.deck):
                recurse = False

        if recurse:
            newPlayers = []
            for i in [0,1]:
                newCards = self.players[i].deck[:playedCards[i].value][:]
                newPlayers.append(Player(newCards, i+1))
            newGame = Game(newPlayers, self.depth+1)
            recWinner = newGame.play()
            winnerIndex = int(recWinner.name)-1
            playedCards = [playedCards[winnerIndex], playedCards[winnerIndex-1]]
            winner = self.players[winnerIndex]
        else:
            if playedCards[0].value > playedCards[1].value:
                winner = self.players[0]
            else:
                winner = self.players[1]

            if playedCards[0].value < playedCards[1].value:
                playedCards.insert(0, playedCards[1])
                playedCards.pop(2)

        winner.deck.extend(playedCards)

        return winner


    def turnPart1(self):
        highCard = {
            'val': 0,
            'player': None
        }

        playedCards = []
        for player in self.players:
            card = player.play()
            if card.value > highCard['val']:
                playedCards.insert(0, card)
                highCard = {
                    'val': card.value,
                    'player': player
                }
            else:
                playedCards.append(card)
        highCard['player'].deck.extend(playedCards)

    def __str__(self):
        string = ""
        for player in self.players:
            string += str(player) + " SCORE: " + str(player.score())
            string += "\n"
        return  string





class Player:
    def __init__(self, cardValues, name):
        self.name = str(name)
        self.deck = []
        self.setupCards(cardValues)
        pass

    def score(self):
        score = 0
        for i in range(len(self.deck)):
            score += self.deck[::-1][i].value * (i+1)
        return score

    def setupCards(self, cardValues):
        if type(cardValues[0]) == str:
            for cardValue in cardValues:
                self.deck.append(Card(int(cardValue)))
        else:
            for card in cardValues:
                self.deck.append(card)


    def play(self):
        card = self.draw()
        return card

    def draw(self):
        return self.deck.pop(0)

    def __str__(self):
        string = f"Player {self.name}: "
        for card in self.deck:
            string += f"{card.value}, "
        return string

class Card:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

    def __repr__(self):
        return str(self)


data = open('22.txt').read()
playersData = data.split("\n\n")
players = []
i = 0
for player in playersData:
    i+=1
    cards = player.split("\n")[1:]
    players.append(Player(cards, i))

game = Game(players)
winner = game.play()

print(winner)
print(winner.score())