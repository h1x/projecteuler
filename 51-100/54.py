# In the card game poker, a hand consists of five cards and are ranked,
# from lowest to highest, in the following way:
#
# High Card: Highest value card.
# One Pair: Two cards of the same value.
# Two Pairs: Two different pairs.
# Three of a Kind: Three cards of the same value.
# Straight: All cards are consecutive values.
# Flush: All cards of the same suit.
# Full House: Three of a kind and a pair.
# Four of a Kind: Four cards of the same value.
# Straight Flush: All cards are consecutive values of same suit.
# Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.
# The cards are valued in the order:
# 2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.
#
# If two players have the same ranked hands then the rank made up of the highest
# value wins; for example, a pair of eights beats a pair of fives (see example 1 below).
# But if two ranks tie, for example, both players have a pair of queens, then highest
# cards in each hand are compared (see example 4 below); if the highest cards tie
# then the next highest cards are compared, and so on.
#
# Consider the following five hands dealt to two players:
#
# Hand	 	Player 1	 	Player 2	 	Winner
# 1	 	5H 5C 6S 7S KD   2C 3S 8S 8D TD    Player 2
#          Pair of Fives   Pair of Eights
# 2	 	5D 8C 9S JS AC   2C 5C 7D 8S QH    Player 1
#        Highest card Ace Highest card Queen
# 3	 	2D 9C AS AH AC   2C 5C 7D 8S QH    PLayer 2
#           Three Aces   Flush with Diamonds
# 4	 	4D 6S 9H QH QC   3D 6D 7H QD QS    Player 1
#         Pair of Queens   Pair of Queens
#       Highest card Nine Highest card Seven
# 5	 	2H 2D 4C 4D 4S   3C 3D 3S 9S 9D    Player 1
#           Full House       Full House
#        With Three Fours With Three Threes
#
# The file, poker.txt, contains one-thousand random hands dealt to two players.
# Each line of the file contains ten cards (separated by a single space): the first
# five are Player 1's cards and the last five are Player 2's cards. You can assume
# that all hands are valid (no invalid characters or repeated cards), each player's
# hand is in no specific order, and in each hand there is a clear winner.
#
# How many hands does Player 1 win?

def getHighCard(c1, c2, c3, c4, c5):
    hand = ''.join(sorted(c1 + c2 + c3 + c4 + c5));

    if "A" in hand:
        return "A";
    elif "K" in hand:
        return "K";
    elif "Q" in hand:
        return "Q";
    elif "J" in hand:
        return "J";
    elif "T" in hand:
        return "T";

    return hand[len(hand) - 1];

def determineHand(card1, card2, card3, card4, card5):
    hand = ''.join(sorted(card1[0] + card2[0] + card3[0] + card4[0] + card5[0]));

    if card1[1] == card2[1] and card1[1] == card3[1] and card1[1] == card4[1] and card1[1] == card5[1]:
        forRoyal = 'AJKQT';
        # ROYAL FLUSH
        if hand == forRoyal:
            return 10;
        # STRAIGHT FLUSH
        if ord(hand[0]) + 1 == ord(hand[1]) and ord(hand[0]) + 2 == ord(hand[2]) and ord(hand[0]) + 3 == ord(hand[3]) and ord(hand[0]) + 4 == ord(hand[4]):
            return 9, getHighCard(hand[0], hand[1], hand[2], hand[3], hand[4]);
        elif hand == "9JKQT" or hand == "89JQT" or hand == "789JT" or hand == "6789T":
            return 9, getHighCard(hand[0], hand[1], hand[2], hand[3], hand[4]);
        # FLUSH
        return 6, getHighCard(hand[0], hand[1], hand[2], hand[3], hand[4]);
    else:
        # FOUR OF A KIND
        if hand[0] == hand[1] and hand[0] == hand[2] and hand[0] == hand[3]:
            return 8, hand[2];
        elif hand[1] == hand[2] and hand[1] == hand[3] and hand[1] == hand[4]:
            return 8, hand[2];
        # FULL HOUSE
        if hand[0] == hand[1] and hand[0] == hand[2] and hand[3] == hand[4]:
            return 7, hand[2];
        elif hand[0] == hand[1] and hand[2] == hand[3] and hand[2] == hand[4]:
            return 7, hand[2];
        # STRAIGHT
        if ord(hand[0]) + 1 == ord(hand[1]) and ord(hand[0]) + 2 == ord(hand[2]) and ord(hand[0]) + 3 == ord(hand[3]) and ord(hand[0]) + 4 == ord(hand[4]):
            return 5, getHighCard(hand[0], hand[1], hand[2], hand[3], hand[4]);
        elif hand == "9JKQT" or hand == "89JQT" or hand == "789JT" or hand == "6789T" or hand == "AJKQT":
            return 5, getHighCard(hand[0], hand[1], hand[2], hand[3], hand[4]);
        # THREE OF A KIND
        if hand[0] == hand[1] and hand[0] == hand[2]:
            return 4, hand[2];
        elif hand[1] == hand[2] and hand[1] == hand[3]:
            return 4, hand[2];
        elif hand[2] == hand[3] and hand[2] == hand[4]:
            return 4, hand[2];
        # TWO PAIRS
        if hand[0] == hand[1] and hand[2] == hand[3]:
            return 3, getHighCard(hand[0], hand[2], "", "", "");
        elif hand[0] == hand[1] and hand[3] == hand[4]:
            return 3, getHighCard(hand[0], hand[3], "", "", "");
        elif hand[1] == hand[2] and hand[3] == hand[4]:
            return 3, getHighCard(hand[1], hand[3], "", "", "");
        #ONE PAIR
        if hand[0] == hand[1] or hand[1] == hand[2]:
            return 2, hand[1];
        elif hand[2] == hand[3] or hand[3] == hand[4]:
            return 2, hand[3];
    # HIGH CARD
    return 1, getHighCard(hand[0], hand[1], hand[2], hand[3], hand[4]);


def determineWinnerForHand(player1Hand, player2Hand, player1HighCard, player2HighCard):
    if player1Hand > player2Hand:
        return 1;
    elif player1Hand < player2Hand:
        return 2;
    elif player1Hand == player2Hand:
        if player1HighCard not in "AKQJT" and player2HighCard not in "AKQJT":
            if int(player1HighCard) > int(player2HighCard):
                return 1;
            else:
                return 2;
        else:
            if player1HighCard == "A":
                return 1;
            elif player2HighCard == "A":
                return 2;
            elif player1HighCard == "K":
                return 1;
            elif player2HighCard == "K":
                return 2;
            elif player1HighCard == "Q":
                return 1;
            elif player2HighCard == "Q":
                return 2;
            elif player1HighCard == "J":
                return 1;
            elif player2HighCard == "J":
                return 2;
            elif player1HighCard == "T":
                return 1;
            elif player2HighCard == "T":
                return 2;

f = open("poker.txt", "r");
count = 0;

for line in f:
    currentHand = line.split(" ");
    currentHand[9] = currentHand[9].replace("\n", "");
    p1hand, p1hc = determineHand(currentHand[0], currentHand[1], currentHand[2], currentHand[3], currentHand[4]);
    p2hand, p2hc = determineHand(currentHand[5], currentHand[6], currentHand[7], currentHand[8], currentHand[9]);
    if determineWinnerForHand(p1hand, p2hand, p1hc, p2hc) == 1:
        count += 1;

f.close();

print(count);
