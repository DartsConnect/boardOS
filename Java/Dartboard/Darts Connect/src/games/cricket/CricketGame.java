package games.cricket;

import games.*;
import system.GlobalVariables;

import java.util.ArrayList;

/**
 * Created by JordanLewis on 29/01/2016.
 */
public class CricketGame extends Game implements GameDelegate {

    final int[] validHits = {15,16,17,18,19,20,25};
    private  int[] closedNumbers = new int[7];
    private boolean isCutThroat = false;
    private ArrayList<CricketPlayer> cricketPlayers = new ArrayList<CricketPlayer>(4);

    private void cutThroatDartHit(int hitValue, int multiplier) {
        // TODO Write code for cut throat dart hit
    }

    private void normalDartHit(int hitValue, int multiplier) {
        // TODO Write code for normal dart hit
        this.cricketPlayers[this.currentTurn].didHit

    }

    @Override
    public void delegateDartDidHit(int hitValue, int multiplier) {
        if (GlobalVariables.getInstance().indexOf(hitValue, validHits) != -1) {
            if (isCutThroat) {
                this.cutThroatDartHit(hitValue, multiplier);
            } else {
                this.normalDartHit(hitValue, multiplier);
            }
        }
    }
}
