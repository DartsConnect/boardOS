// Thursday October 15 2015

package games.countdown;

import games.countdown.*;

public class CountDownGame {

    int currentTurn = 0;
    CountDownPlayer[] players;

    void dartDidHit(int valueOfHit) {
        // The Player threw the dart
        if (players[currentTurn].threwDart()) {
            currentTurn++;
            if (currentTurn == players.length) {
                currentTurn = 0;
            }
        }
    }

    public CountDownGame(int startScore, int numberOfPlayers) {
        for (int i = 0; i < numberOfPlayers; i++) {
            players[i] = new CountDownPlayer(startScore, "a");
        }

    }
}