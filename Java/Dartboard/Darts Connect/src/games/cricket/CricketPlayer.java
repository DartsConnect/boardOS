package games.cricket;

import games.Player;
import system.GlobalVariables;

import java.util.ArrayList;
import java.util.HashMap;

/**
 * Created by JordanLewis on 29/01/2016.
 */
public class CricketPlayer extends Player {
    ArrayList<Integer> closedNumbers = new ArrayList<Integer>();
    HashMap<Integer, Integer> closureBuffer = new HashMap<Integer, Integer>(7);
    private boolean isCutThroat = false;

    private void registerScore(int hitValue, int multiplier) {
        if (isCutThroat) {
            // Push the score against other players
            // TODO Write code to hurt other people in cut throat cricket
        } else {
            this.score += hitValue * multiplier;
        }
    }

    private void closeNumber(int numberToClose) {
        this.closedNumbers.add(numberToClose);

        if (closedNumbers.size() == 7) {
            // TODO Complete game code
            // This player has finished the game
        }
    }

    void didHitNumber(int hitValue, int multiplier) {
        if (closedNumbers.indexOf(hitValue) == -1) {
            // If the hit number is not yet closed

        } else if ((closureBuffer.get(hitValue) + multiplier) - 3 > 0) {
            // if the number is not yet closed, but will be with this shot with some extra
            // ie 15 was hit twice, and just got hit with a triple, meaning 2 shots will earn points
            int overflow = (closureBuffer.get(hitValue) + multiplier) -3;

            this.closeNumber(hitValue);

            this.registerScore(hitValue, overflow);
        } else {
            // If the hit number is closed
            this.registerScore(hitValue, multiplier);
        }
    }

    public CricketPlayer(boolean _isCutThroat, String _cardID) {
        super(_cardID);

        isCutThroat = _isCutThroat;

        // Initiate the items in the closer buffer
        for (int i = 15; i <= 20; i++) {
            closureBuffer.put(i, 0);
        }
        closureBuffer.put(25, 0);
    }
}
