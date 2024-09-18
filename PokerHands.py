from random import randint
from collections import Counter
from settleTiefunctions import settleStraightFlush, settleFourOfAKind, settleFullHouse, settleFlush, settleStraight, settleThreeOfAKind,settleTwoPair, settleOnePair, settleHighCard

SUITS = {1: 'C', 2: 'H', 3: 'D', 4: 'S'}
VALUES = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
VALUESMAP = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
HANDRANKINGNG = {
    "Royal Flush": 10,
    "Straight Flush": 9,
    "Four of a kind": 8,
    "Full House": 7,
    "Flush": 6,
    "Straight": 5,
    "Three of a kind": 4,
    "Two Pair": 3,
    "One Pair": 2,
    "High Card": 1
}

def addSuiteToCard(randomlyPickedSuiteNumber: int, randomlyChosenCard: chr):
    return f"{randomlyChosenCard}{SUITS[randomlyPickedSuiteNumber]}"
    
def pickCards():
    suiteNumber = randint(1, 4)
    cardValue = VALUES[randint(0, len(VALUES) - 1)]
    return addSuiteToCard(suiteNumber, cardValue)

def getPlayerCards():
    return [pickCards() for _ in range(5)]

def extractSuitesAndValues(playerCards):
    suites = []
    cardValues = []
    for card in playerCards:
        if card[:-1] == '10': 
            cardValues.append('10')
        else:
            cardValues.append(card[0])
        suites.append(card[-1])  
    return suites, cardValues


def determineHandRank(playerCards):
    suites, cardValues = extractSuitesAndValues(playerCards)
    cardValues = [VALUESMAP[val] for val in cardValues]

    sortedCardValues = sorted(cardValues)
    # set removes duplicates
    isFlush  = len(set(suites)) == 1 
    # check if the soreted list is the same as a newly created list that starts from the least value in the sorted list to the max value in the sorted list + 1
    isStraigh = (sortedCardValues == list(range(min(sortedCardValues), max(sortedCardValues) + 1)))
    # creates as object with the value as the key and the number of times it appears as the value. example output => Counter({'Q': 2, '2': 1, '4': 1, 'A': 1})
    valueCounter = Counter(cardValues)
    # creates a list of the values of the values of the counter object. example output => [2, 1, 1, 1], used to check if the hand is pair, two pair, three of a kind, full house, four of a kind
    valueCounterList = sorted(valueCounter.values(), reverse = True)

    if (isStraigh and isFlush and max(cardValues) == 14):
        return "Royal Flush"
    elif (isStraigh and isFlush):
        return "Straight Flush"
    elif valueCounterList == [4, 1]:
        return "Four of a kind"
    elif valueCounterList == [3, 2]:
        return "Full House"
    elif isFlush:
        return "Flush"
    elif isStraigh:
        return "Straight"
    elif valueCounterList == [3, 1, 1]:
        return "Three of a kind"
    elif valueCounterList == [2, 2, 1]:
        return "Two Pair"
    elif valueCounterList == [2, 1, 1, 1]:
        return "One Pair"
    else:
        return "High Card"
    
def compareHands(player1Hand, player2Hand):
    player1HandRank = determineHandRank(player1Hand)
    player2HandRank = determineHandRank(player2Hand)

    if (HANDRANKINGNG[player1HandRank] > HANDRANKINGNG[player2HandRank]):
        print("Player 1 wins with " + player1HandRank)
    elif (HANDRANKINGNG[player1HandRank] < HANDRANKINGNG[player2HandRank]):
        print("Player 2 wins with " + player2HandRank)
    else:
        settleTie(player1Hand, player2Hand, player1HandRank, player2HandRank)

def settleTie(player1Hand, player2Hand, player1HandRank, player2HandRank):
    player1CardValues = [VALUESMAP[card[:-1]] for card in player1Hand]
    player2CardValues = [VALUESMAP[card[:-1]] for card in player2Hand]

    player1CardValues.sort(reverse = True)
    player2CardValues.sort(reverse = True)

    player1Counts = Counter(player1CardValues)
    player2Counts = Counter(player2CardValues)

    if (player1HandRank == player2HandRank == "Straight Flush"):
        highestCard1 = max(player1CardValues)
        highestCard2 = max(player2CardValues)
        settleStraightFlush(highestCard1, highestCard2)
    elif (player1HandRank == player2HandRank == "Four of a kind"):
        player1FourOfAKindValue = [val for val, count in player1Counts.items() if count == 4]
        player2FourOfAKindValue = [val for val, count in player2Counts.items() if count == 4]
        Player1Kickers = [val for val in player1CardValues if val != player1FourOfAKindValue]
        Player2Kickers = [val for val in player2CardValues if val != player2FourOfAKindValue]
        settleFourOfAKind(player1FourOfAKindValue, player2FourOfAKindValue, Player1Kickers, Player2Kickers)
    elif (player1HandRank == player2HandRank == "Full House"):
        player1ThreeOfAKindValue = [val for val, count in player1Counts.items() if count == 3]
        player2ThreeOfAKindValue = [val for val, count in player2Counts.items() if count == 3]
        Player1Pair = [val for val, count in player1Counts.items() if count == 2]
        Player2Pair = [val for val, count in player2Counts.items() if count == 2]
        settleFullHouse(player1ThreeOfAKindValue, player2ThreeOfAKindValue, Player1Pair, Player2Pair)
    elif (player1HandRank == player2HandRank == "Flush"):
        settleFlush(player1CardValues.sort(reverse = True), player2CardValues.sort(reverse = True))
    elif (player1HandRank == player2HandRank == "Straight"):
        highestCard1 = max(player1CardValues)
        highestCard2 = max(player2CardValues)
        settleStraight(highestCard1, highestCard2)
    elif (player1HandRank == player2HandRank == "Three of a kind"):
        player1ThreeOfAKindValue = [val for val, count in player1Counts.items() if count == 3]
        player2ThreeOfAKindValue = [val for val, count in player2Counts.items() if count == 3]
        settleThreeOfAKind(player1ThreeOfAKindValue, player2ThreeOfAKindValue)
    elif (player1HandRank == player2HandRank == "Two Pair"):
        player1Pair1Value = [val for val, count in player1Counts.items() if count == 2][0]
        player1Pair2Value = [val for val, count in player1Counts.items() if count == 2][1]
        player2Pair1Value = [val for val, count in player2Counts.items() if count == 2][0]
        player2Pair2Value = [val for val, count in player2Counts.items() if count == 2][1]
        player1Kicker = [val for val in player1CardValues if val not in [player1Pair1Value, player1Pair2Value]]
        player2Kicker = [val for val in player2CardValues if val not in [player2Pair1Value, player2Pair2Value]]
        settleTwoPair(player1Pair1Value, player1Pair2Value, player2Pair1Value, player2Pair2Value, player1Kicker, player2Kicker)
    elif (player1HandRank == player2HandRank == "One Pair"):
        player1PairValue = [val for val, count in player1Counts.items() if count == 2][0]
        player2PairValue = [val for val, count in player2Counts.items() if count == 2][0]
        player1Kickers = [val for val in player1CardValues if val != player1PairValue]
        player2Kickers = [val for val in player2CardValues if val != player2PairValue]
        settleOnePair(player1PairValue, player2PairValue, player1Kickers, player2Kickers)
    else:
        settleHighCard(player1CardValues, player2CardValues)
        
def playGame():
    player1 = getPlayerCards()
    player2 = getPlayerCards()

    print("Player 1's hand: ", end = " ")
    for card in player1:
        print(card, end = " ")
    print("Player 2's hand: ", end = " ")
    for card in player2:
        print(card, end = " ")
    print()
    compareHands(player1, player2)

playGame()

