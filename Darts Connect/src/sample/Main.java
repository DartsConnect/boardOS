// Thursday October 15 2015
package sample;

import javafx.application.Application;
import javafx.fxml.FXMLLoader;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.stage.Stage;
import system.GlobalVariables;
import system.hardware_input.HardwareInputDelegate;
import system.hardware_input.KeyboardListener;

public class Main extends Application implements HardwareInputDelegate {

    @Override
    public void start(Stage primaryStage) throws Exception{
        Parent root = FXMLLoader.load(getClass().getResource("sample.fxml"));
        primaryStage.setTitle("Hello World");
        Scene currentScene = new Scene(root, 300, 275);
        primaryStage.setScene(currentScene);
        primaryStage.show();

        GlobalVariables.getInstance().keyboardListener = new KeyboardListener(currentScene);
        GlobalVariables.getInstance().keyboardListener.frontClass = this;
    }


    public static void main(String[] args) {
        launch(args);
    }

    @Override
    public void dartDidHit(int hitValue, int multiplier) {

    }
}
