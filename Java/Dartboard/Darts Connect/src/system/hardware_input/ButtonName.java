package system.hardware_input;

import java.util.HashMap;

/**
 * Created by JordanLewis on 21/10/2015.
 */
public enum ButtonName {
    BUTTON_BACK(0),
    BUTTON_1(1),
    BUTTON_2(2),
    BUTTON_3(3),
    BUTTON_4(4),
    BUTTON_ENTER(5);

    public int value;

    /*
        Begin Code from StackOverflow by MeBigFatGuy
        https://stackoverflow.com/questions/5292790/convert-integer-value-to-matching-java-enum
        Written on: March 13th 2011
        Taken: Thursday October 22 2015
     */
    private static final HashMap<Integer, ButtonName> intToTypeMap = new HashMap<Integer, ButtonName>();
    static {
        for (ButtonName type : ButtonName.values()) {
            intToTypeMap.put(type.value, type);
        }
    }

    public static ButtonName fromInt(int i) {
        ButtonName type = intToTypeMap.get(Integer.valueOf(i));
        // If it is not found, it will return null
        return type;
    }
    /*
        End Code from StackOverflow by MeBigFatGuy
     */

    ButtonName(int i) {
        this.value = i;
    }
}
