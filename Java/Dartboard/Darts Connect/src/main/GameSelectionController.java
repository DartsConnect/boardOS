// Thursday October 15 2015

package main;

import javafx.fxml.Initializable;
import javafx.scene.Scene;
import system.GlobalVariables;
import system.hardware_input.ButtonName;
import system.hardware_input.HardwareInputDelegate;
import ui.SideMenu;

import java.net.URL;
import java.util.ResourceBundle;

public class GameSelectionController implements Initializable, HardwareInputDelegate {

    SideMenu menu = new SideMenu();

    @Override
    public void buttonPressed(ButtonName button) {
        System.out.println(button.value);
    }

    // Monday November 02 2015
    void sceneLoaded(Scene scene) {
        GlobalVariables.getInstance().keyboardListener.frontClass = this;
    }

    @Override
    public void initialize(URL location, ResourceBundle resources) {
        System.out.println("View is now loaded!");
    }

    public GameSelectionController() {

    }
}
