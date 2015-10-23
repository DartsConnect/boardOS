package games;

import system.hardware_input.ButtonName;
import system.hardware_input.HardwareInputDelegate;

/**
 * Created by 38559 on 15/10/15.
 */
public class Game implements HardwareInputDelegate {

    protected GameDelegate currentGame;
    protected int currentTurn = 0;
    protected int currentRound = 1;
    protected int roundLimit = -1; // Amount of rounds allowed in a game before it is forced to finish.
    protected Player[] players;

    /*
        Wednesday October 21 2015
     */
    @Override
    public void buttonPressed(ButtonName button) {
        switch (button) {
            case BUTTON_BACK:
                break;
            case BUTTON_1:
                break;
            case BUTTON_2:
                break;
            case BUTTON_3:
                break;
            case BUTTON_4:
                break;
            case BUTTON_ENTER:
                break;
        }
    }

    /*
        Thursday October 15 2015
        Called when a dart hits the Dartboard.
        Tell's the current player's class that the player threw a dart, which will then return if it can throw again.
        If the player cannot, the currentTurn is incremented so that the next player can throw.
    */
    @Override
    public void dartDidHit(int hitValue, int multiplier) {
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

            currentRound++;

            if (roundLimit != -1 && currentRound > roundLimit) {
                this.endGame();
            }
        }
    }

    /*
        Wednesday October 21 2015
     */
    protected void endGame() {
        System.out.println("game has been finished");
    }

    /*
        Wednesday October 21 2015
     */
    void beginGame() {

    }

    /*
        Wednesday October 21 2015
     */
    void quitGame() {

    }

    public Game() {

    }

}
