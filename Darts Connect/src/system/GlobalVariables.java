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

    private GlobalVariables() {
    }
}
