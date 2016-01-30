package system;

import javafx.scene.Scene;
import system.hardware_input.KeyboardListener;

/**
 * Created by JordanLewis on 22/10/2015.
 */

public class GlobalVariables {
    private static GlobalVariables ourInstance = new GlobalVariables();

    public static GlobalVariables getInstance() {
        return ourInstance;
    }

    public static KeyboardListener keyboardListener;

    public static Scene currentScene;

    public int indexOf(int item, int[] arr) {
        int index = -1;
        for (int i = 0; i < arr.length; i++) {
            if (arr[i] == item) {
                index = i;
                break;
            }
        }
        return index;
    }

    private GlobalVariables() {
    }
}
