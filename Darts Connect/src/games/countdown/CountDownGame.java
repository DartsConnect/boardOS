// Thursday October 15 2015

package games.countdown;

import games.*;

public class CountDownGame extends Game implements GameDelegate {

    private int gameStartScore;
    private boolean openOnDouble = false;
    private boolean closeOnDouble = false;
    private boolean openOnTriple = false;
    private boolean closeOnTriple = false;

    @Override
    public void delegateDartDidHit(int hitValue, int multiplier) {
        int totalHitValue = hitValue * multiplier;
        int currentPlayerScore = this.players[this.currentTurn].score;

        // If it is a shot to open the count down and there is a condition to open the game.
        if (currentPlayerScore == gameStartScore) {
            boolean canContinue = false;
            if (openOnDouble && openOnTriple) {
                if (multiplier != 1) canContinue = true;
            } else if (openOnDouble) {
                if (multiplier == 2) canContinue = true;
            } else if (openOnTriple) {
                if (multiplier == 3) canContinue = true;
            } else { // No condition
                canContinue = true;
            }

            if (canContinue) {
                currentPlayerScore -= totalHitValue;
                this.players[this.currentTurn].score = currentPlayerScore;
            }
        } else {
            // This is general play

            this.players[this.currentTurn].score -= totalHitValue;

            // If the user Busts
            if (currentPlayerScore < 0) {
                currentPlayerScore += totalHitValue;
                this.players[this.currentTurn].score = currentPlayerScore;
                this.players[this.currentTurn].forceEndTurn();
                this.nextPlayer();
            } else if (currentPlayerScore == 0) {
                // The player may have finished

                boolean canContinue = false;

                // If there are condition to win, ie close on a double, triple or both.
                if (closeOnDouble && closeOnTriple) {
                    if (multiplier != 1) canContinue = true;
                } else if (closeOnDouble) {
                    if (multiplier == 2) canContinue = true;
                } else if (closeOnTriple) {
                    if(multiplier == 3) canContinue = true;
                } else { // No condition
                    canContinue = true;
                }

                if (canContinue) {
                    // NOW the user finally wins.

                } else {
                    // The player didn't hit the right spot to win according to the game conditions.
                    currentPlayerScore += totalHitValue;
                    this.players[this.currentTurn].score = currentPlayerScore;
                    this.players[this.currentTurn].forceEndTurn();
                    this.nextPlayer();
                }
            }
        }
    }

    public CountDownGame(int startScore, int numberOfPlayers) {
        super();

        gameStartScore = startScore;

        this.currentGame = this;

        // Create an instance of a player and add it to the list
        for (int i = 0; i < numberOfPlayers; i++) {
            this.players[i] = new CountDownPlayer(startScore, "a");
        }
    }
}