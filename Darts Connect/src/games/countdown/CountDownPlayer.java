// Thursday October 15 2015
package games.countdown;

import games.Player;

public class CountDownPlayer extends Player {



    public CountDownPlayer(int startScore, String _cardID) {
        super(_cardID);
        this.score = startScore;
        System.out.println(this.score);
    }
}