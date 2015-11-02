package ui;

import javafx.scene.control.Label;
import javafx.scene.layout.BorderPane;
import javafx.scene.layout.VBox;
import system.hardware_input.ButtonName;
import system.hardware_input.HardwareInputDelegate;

import java.util.List;

/**
 * Created by JordanLewis on 29/10/2015.
 */
public class SideMenu extends BorderPane implements HardwareInputDelegate {
    Label titleLabel = new Label("Title");
    private VBox optionsBox = new VBox();
    private SideMenuOption[] allOptions = new SideMenuOption[8];
    Label footerLabel = new Label("More");
    Boolean isFooterSelectable = false;

    @Override
    public void buttonPressed(ButtonName button) {
        /*
        0 = back
        1 = down
        2 = up
        5 = select
         */

    }

    public void setOptions(String[] options) {
        // Clear and reset
        allOptions = new SideMenuOption[8];
        optionsBox.getChildren().removeAll();

        // Add the new ones
        for (int i = 0; i <= options.length; i++) {
            String option = options[i];
            SideMenuOption menuOption = new SideMenuOption(option);
            allOptions[i] = menuOption;
            optionsBox.getChildren().add(menuOption);
        }
    }

    public SideMenu() {
        this.setTop(titleLabel);
        this.setCenter(optionsBox);
        this.setBottom(footerLabel);
    }
}
