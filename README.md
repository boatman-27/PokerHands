# Poker Hand Comparison Game

This project implements a poker hand comparison game where two players each receive a random poker hand, and their hands are evaluated to determine the winner. In the case of a tie, additional logic is used to break the tie based on the hand rankings.

This project was inspired by [Coding Dojo](/https://codingdojo.org/kata/PokerHands/)

## Features
- Random card generation with suits and values.
- Hand ranking based on standard poker rules:
  - Royal Flush
  - Straight Flush
  - Four of a Kind
  - Full House
  - Flush
  - Straight
  - Three of a Kind
  - Two Pair
  - One Pair
  - High Card
- Tie-breaking logic that follows the rules of poker.

## Functions

### `pickCards()`
Generates a random card by choosing a random suit and value.

### `getPlayerCards()`
Generates a hand of 5 cards for a player by calling `pickCards()`.

### `determineHandRank(playerCards)`
Evaluates a hand and returns the rank of the hand as a string. The hand is analyzed to determine if it qualifies for a specific poker hand (e.g., Flush, Full House).

### `compareHands(player1Hand, player2Hand)`
Compares two poker hands and determines the winner based on the rank of the hands. If the ranks are the same, the `settleTie()` function is called to break the tie.

### `settleTie(player1Hand, player2Hand, player1HandRank, player2HandRank)`
Breaks ties between hands of the same rank by comparing individual card values or kickers.

### `playGame()`
Main game function that deals hands to two players, displays the hands, and compares them to determine the winner.

### Hand Ranking Tiebreaker Functions:
These functions handle tie-breaking logic for specific hand types:
- `settleStraightFlush(highestCard1, highestCard2)`
- `settleFourOfAKind(player1FourOfAKindValue, player2FourOfAKindValue, player1Kicker, player2Kicker)`
- `settleFullHouse(player1ThreeOfAKindValue, player2ThreeOfAKindValue, Player1Pair, Player2Pair)`
- `settleFlush(player1CardValues, player2CardValues)`
- `settleStraight(highestCard1, highestCard2)`
- `settleThreeOfAKind(player1ThreeOfAKindValue, player2ThreeOfAKindValue)`
- `settleTwoPair(player1Pair1Value, player1Pair2Value, player2Pair1Value, player2Pair2Value, player1Kicker, player2Kicker)`
- `settleOnePair(player1PairValue, player2PairValue, player1Kickers, player2Kickers)`
- `settleHighCard(player1CardValues, player2CardValues)`

## How to Play
1. Run the `playGame()` function to start the game.
2. Two hands will be generated randomly for Player 1 and Player 2.
3. The hands will be compared based on their ranks, and the winner will be announced.

## Example

Player 1's hand: `2H 9C 10S KS AD` Player 2's hand: `3D 4H 9D QS QC` Player 2 wins with One Pair
In this example, Player 2 has a pair of Queens, while Player 1 has a High Card (Ace), so Player 2 wins.

## Dependencies
- Python's built-in `random` and `collections` libraries.
- Custom module `settleTiefunctions` (Ensure to implement and import functions such as `settleStraightFlush`, `settleFourOfAKind`, etc.).
