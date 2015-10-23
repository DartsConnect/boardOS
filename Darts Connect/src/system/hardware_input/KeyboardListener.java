package system.hardware_input;

import javafx.scene.Scene;
import javafx.scene.input.KeyEvent;

import java.util.Date;
import java.util.HashMap;
import java.util.List;

/**
 * Created by JordanLewis on 22/10/2015.
 */
public class KeyboardListener {

    public HardwareInputDelegate frontClass;
    private HashMap<String, Long> keyTimes = new HashMap<String, Long>();
    public KeyboardListener(Scene scene) {

        // Key Pressed
        scene.addEventHandler(KeyEvent.KEY_PRESSED, (key) -> {
            int keyValue = Integer.parseInt(key.getText());
            ButtonName buttonType = ButtonName.fromInt(keyValue - 1);
            if (buttonType != null) {
                if (keyTimes.get(key.getText()) == null) {
                    keyTimes.put(key.getText(), new Date().getTime());
                    frontClass.buttonPressed(buttonType);
                }
            }
        });

        // Key Released
        scene.addEventHandler(KeyEvent.KEY_RELEASED, (key) -> {
            int keyValue = Integer.parseInt(key.getText());
            ButtonName buttonType = ButtonName.fromInt(keyValue - 1);
            if (buttonType != null) {

                // Calculate the time between the key being pressed and released
                long keyDownTime = keyTimes.get(key.getText());
                long now = new Date().getTime();
                long timeBetween = now - keyDownTime; // 1000 = 1 second

                frontClass.buttonReleased(buttonType, timeBetween);

                keyTimes.remove(key.getText());
            }
        });
    }
}
