VALUESMAP = {2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 
             10: '10', 11: 'Jack', 12: 'Queen', 13: 'King', 14: 'Ace'}

def settleStraightFlush(highestCard1, highestCard2):
    if highestCard1 > highestCard2:
        result = "Player 1 wins with a " + str(VALUESMAP[highestCard1]) + " Straight Flush"
    elif highestCard1 < highestCard2:
        result = "Player 2 wins with a " + str(VALUESMAP[highestCard2]) + " Straight Flush"
    else:
        result = "It's a tie with a " + str(VALUESMAP[highestCard1]) + " Straight Flush"
    
    print(result)
    return result

def settleFourOfAKind(player1FourOfAKindValue, player2FourOfAKindValue, player1Kicker, player2Kicker):
    if player1FourOfAKindValue > player2FourOfAKindValue:
        result = "Player 1 wins with a " + str(VALUESMAP[player1FourOfAKindValue]) + " Four of a Kind"
    elif player1FourOfAKindValue < player2FourOfAKindValue:
        result = "Player 2 wins with a " + str(VALUESMAP[player2FourOfAKindValue]) + " Four of a Kind"
    else:
        # Four of a kind values are tied, so compare kickers
        if player1Kicker > player2Kicker:
            result = "Player 1 wins with a " + str(VALUESMAP[player1FourOfAKindValue]) + " Four of a Kind and " + str(VALUESMAP[player1Kicker]) + " kicker"
        elif player1Kicker < player2Kicker:
            result = "Player 2 wins with a " + str(VALUESMAP[player2FourOfAKindValue]) + " Four of a Kind and " + str(VALUESMAP[player2Kicker]) + " kicker"
        else:
            result = "It's a tie with a " + str(VALUESMAP[player1FourOfAKindValue]) + " Four of a Kind"
    
    print(result)
    return result

def settleFullHouse(player1ThreeOfAKindValue, player2ThreeOfAKindValue, Player1Pair, Player2Pair):
    if (player1ThreeOfAKindValue > player2ThreeOfAKindValue):
        result = "Player 1 wins with a " + str(VALUESMAP[player1ThreeOfAKindValue]) + " Full House"
    elif (player1ThreeOfAKindValue < player2ThreeOfAKindValue):
        result = "Player 2 wins with a " + str(VALUESMAP[player2ThreeOfAKindValue]) + " Full House"
    else:
        # Three of a kind values are tied, so compare pairs
        if (Player1Pair > Player2Pair):
            result = "Player 1 wins with a " + str(VALUESMAP[player1ThreeOfAKindValue]) + " Full House and " + str(VALUESMAP[Player1Pair]) + " pair"
        elif (Player1Pair < Player2Pair):
            result = "Player 2 wins with a " + str(VALUESMAP[player2ThreeOfAKindValue]) + " Full House and " + str(VALUESMAP[Player2Pair]) + " pair"
        else:
            result = "It's a tie with a " + str(VALUESMAP[player1ThreeOfAKindValue]) + " Full House"
    print(result)
    return result

def settleFlush(player1CardValues, player2CardValues):
    for i in range(len(player1CardValues)):
        if player1CardValues[i] > player2CardValues[i]:
            result = "Player 1 wins with a " + str(VALUESMAP[player1CardValues[i]]) + " Flush"
            break
        elif player1CardValues[i] < player2CardValues[i]:
            result = "Player 2 wins with a " + str(VALUESMAP[player2CardValues[i]]) + " Flush"
            break
    else:
        result = "It's a tie with a Flush"
    
    print(result)
    return result

def settleStraight(highestCard1, highestCard2):
    if highestCard1 > highestCard2:
        result = "Player 1 wins with a " + str(VALUESMAP[highestCard1]) + " Straight"
    elif highestCard1 < highestCard2:
        result = "Player 2 wins with a " + str(VALUESMAP[highestCard2]) + " Straight"
    else:
        result = "It's a tie with a Straight"

    print(result)
    return result

def settleThreeOfAKind(player1ThreeOfAKindValue, player2ThreeOfAKindValue):
    if player1ThreeOfAKindValue > player2ThreeOfAKindValue:
        result = "Player 1 wins with a " + str(VALUESMAP[player1ThreeOfAKindValue]) + " Three of a Kind"
    elif player1ThreeOfAKindValue < player2ThreeOfAKindValue:
        result = "Player 2 wins with a " + str(VALUESMAP[player2ThreeOfAKindValue]) + " Three of a Kind"
    else:
        result = "It's a tie with a " + str(VALUESMAP[player1ThreeOfAKindValue]) + " Three of a Kind"
    print(result)
    return result

def settleTwoPair(player1Pair1Value, player1Pair2Value, player2Pair1Value, player2Pair2Value, player1Kicker, player2Kicker):
    if player1Pair1Value > player2Pair1Value:
        result = "Player 1 wins with " + str(VALUESMAP[player1Pair1Value]) + " and " + str(VALUESMAP[player1Pair2Value]) + " Two Pair"
    elif player1Pair1Value < player2Pair1Value:
        result = "Player 2 wins with " + str(VALUESMAP[player2Pair1Value]) + " and " + str(VALUESMAP[player2Pair2Value]) + " Two Pair"
    else:
        # Pair values are tied, so compare the second pair
        if player1Pair2Value > player2Pair2Value:
            result = "Player 1 wins with " + str(VALUESMAP[player1Pair1Value]) + " and " + str(VALUESMAP[player1Pair2Value]) + " Two Pair"
        elif player1Pair2Value < player2Pair2Value:
            result = "Player 2 wins with " + VALUESMAP[player2Pair1Value] + " and " + VALUESMAP[player2Pair2Value] + " Two Pair"
        else:
            # Second pair values are tied, so compare kickers
            if player1Kicker > player2Kicker:
                result = "Player 1 wins with " + str(VALUESMAP[player1Pair1Value]) + " Two Pair and a " + str(VALUESMAP[player1Kicker]) + " kicker"
            elif player1Kicker < player2Kicker:
                result = "Player 2 wins with " + str(VALUESMAP[player2Pair1Value]) + " Two Pair and a " + str(VALUESMAP[player2Kicker]) + " kicker"
            else:
                result = "It's a tie with " + str(VALUESMAP[player1Pair1Value]) + " Two Pair"
    
    print(result)
    return result

def settleOnePair(player1PairValue, player2PairValue, player1Kickers, player2Kickers):
    if player1PairValue > player2PairValue:
        result = "Player 1 wins with a " + str(VALUESMAP[player1PairValue]) + " Pair"
    elif player1PairValue < player2PairValue:
        result = "Player 2 wins with a " + str(VALUESMAP[player2PairValue]) + " Pair"
    else:
        # Compare kickers one by one
        for i in range(len(player1Kickers)):
            if player1Kickers[i] > player2Kickers[i]:
                result = "Player 1 wins with a " + str(VALUESMAP[player1PairValue]) + " Pair and a " + str(VALUESMAP[player1Kickers[i]]) + " kicker"
                break
            elif player1Kickers[i] < player2Kickers[i]:
                result = "Player 2 wins with a " + str(VALUESMAP[player2PairValue]) + " Pair and a " + str(VALUESMAP[player2Kickers[i]]) + " kicker"
                break
        else:
            # If loop completes without finding a winner, it's a tie
            result = "It's a tie with a " + str(VALUESMAP[player1PairValue]) + " Pair"

    print(result)
    return result

def settleHighCard(player1CardValues, player2CardValues):
    # Ensure the card values are sorted in descending order
    player1CardValues.sort(reverse=True)
    player2CardValues.sort(reverse=True)
    
    # Compare card values one by one
    for i in range(len(player1CardValues)):
        if player1CardValues[i] > player2CardValues[i]:
            result = "Player 1 wins with a " + str(VALUESMAP[player1CardValues[i]]) + " High"
            break
        elif player1CardValues[i] < player2CardValues[i]:
            result = "Player 2 wins with a " + str(VALUESMAP[player2CardValues[i]]) + " High"
            break
    else:
        result = "It's a tie with a " + str(VALUESMAP[player1CardValues[0]]) + " High"

    print(result)
    return result
