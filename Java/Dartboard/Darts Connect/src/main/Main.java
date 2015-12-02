// Thursday October 15 2015
package main;

import javafx.application.Application;
import javafx.fxml.FXMLLoader;
import javafx.scene.Parent;
import javafx.scene.Scene;
import javafx.stage.Stage;
import system.GlobalVariables;
import system.hardware_input.HardwareInputDelegate;
import system.hardware_input.KeyboardListener;

public class Main extends Application implements HardwareInputDelegate {

    Stage window;

    @Override
    public void start(Stage primaryStage) throws Exception{
        window = primaryStage;

        FXMLLoader fxmlLoader = new FXMLLoader(getClass().getResource("main.fxml"));
        Parent root = fxmlLoader.load();
        primaryStage.setTitle("Darts Connect");
        Scene currentScene = new Scene(root, 1280, 720);
        primaryStage.setScene(currentScene);
        primaryStage.setResizable(false);
        primaryStage.show();

        GlobalVariables.getInstance().currentScene = currentScene;
        GlobalVariables.getInstance().keyboardListener = new KeyboardListener(currentScene);
        GlobalVariables.getInstance().keyboardListener.frontClass = this;

        GameSelectionController controller = fxmlLoader.getController();
        controller.sceneLoaded(currentScene);
    }


    public static void main(String[] args) {
        launch(args);
    }
}
