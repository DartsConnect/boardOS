// Thursday October 15 2015
package games;

import java.lang.String;

public class Player {
    protected String cardID = ""; // The user's RFID card's UID.
    protected String username = ""; // The user's username (unique).
    protected int totalNumberOfThrows = 0; // Total number of throws in the game.
    protected int score = 0; // The user's current score in the game.
    protected int numberOfThrowsInTurn = 0; // Total number of throws in the turn.


    /*
        Thursday October 15 2015
        A stub.
        Will later be replaced with actual code to fetch the username of the user from the database based on the user's RFID card's UID.
     */
    String getUsernameForCardID(String _cardID) {
        return "Jordan";
    }

    /*
        Thursday October 15 2015
        Called when a player throws a dart and the hit was registered on the board.
        Each player only ever get 3 throws (valid hits) per turn.
        So it checks if the number of registered hits is 3 and returns false if true and true if false, so the game can decide whether or not it is time to switch players.
        It will then reset the current play throw count back to 0.
     */
    public Boolean threwDart() {
        numberOfThrowsInTurn++;
        totalNumberOfThrows++;
        if (numberOfThrowsInTurn == 3) {
            numberOfThrowsInTurn = 0;
            return false;
        }
        return true;
    }

    public Player(String _cardID) {
        cardID = _cardID;
        username = getUsernameForCardID(cardID);
    }
}