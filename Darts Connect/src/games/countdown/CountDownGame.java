// Thursday October 15 2015

package games.countdown;

import games.*;

public class CountDownGame extends Game implements GameDelegate {

    @Override
    public void delegateDartDidHit(int hitValue, int multiplier) {
        int totalHitValue = hitValue * multiplier;
        this.players[this.currentTurn].score -= totalHitValue;

        // If the user Busts
        if (this.players[this.currentTurn].score < 0) {
            this.players[this.currentTurn].score += totalHitValue;
            this.players[this.currentTurn].forceEndTurn();
            this.nextPlayer();
        } else if (this.players[this.currentTurn].score == 0) {
            // This player wins
        }
    }

    public CountDownGame(int startScore, int numberOfPlayers) {
        super();
        this.currentGame = this;

        // Create an instance of a player and add it to the list
        for (int i = 0; i < numberOfPlayers; i++) {
            this.players[i] = new CountDownPlayer(startScore, "a");
        }
    }
}