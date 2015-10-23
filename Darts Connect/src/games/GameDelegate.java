package games;

/**
 * Created by 38559 on 15/10/15.
 */
public interface GameDelegate {
    default void delegateBeginGame() {

    }

    default void delegateEndGame() {

    }

    void delegateDartDidHit(int hitValue, int multiplier);
    //void delegateSkipPlayer();
}
