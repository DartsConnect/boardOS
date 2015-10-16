package games;

/**
 * Created by 38559 on 15/10/15.
 */
public class Game {

    protected GameDelegate currentGame;
    protected int currentTurn = 0;
    protected Player[] players;

    /*
        Thursday October 15 2015
        Called when a dart hits the Dartboard.
        Tell's the current player's class that the player threw a dart, which will then return if it can throw again.
        If the player cannot, the currentTurn is incremented so that the next player can throw.
     */
    void dartDidHit(int hitValue, int multiplier) {
        // The Player threw the dart
        if (players[currentTurn].threwDart()) {
            this.nextPlayer();
        }
        currentGame.delegateDartDidHit(hitValue, multiplier);
    }

    protected void nextPlayer() {
        currentTurn++;
        if (currentTurn == players.length) {
            // Tell the user's to switch players.
            currentTurn = 0;
        }
    }

    public Game() {

    }

}
