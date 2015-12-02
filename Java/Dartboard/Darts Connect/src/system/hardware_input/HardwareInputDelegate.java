package system.hardware_input;

/**
 * Created by JordanLewis on 21/10/2015.
 */
public interface HardwareInputDelegate {
    default void buttonPressed(ButtonName button) {
        System.out.println("Button Pressed: " + button.value);
    }

    default void buttonReleased(ButtonName button, long duration) {
        System.out.println("Button Released: " + button.value + "; Duration: " + duration);
    }

    default void dartDidHit(int hitValue, int multiplier) {}
}
