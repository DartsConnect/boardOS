package system;

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

    private GlobalVariables() {
    }
}
