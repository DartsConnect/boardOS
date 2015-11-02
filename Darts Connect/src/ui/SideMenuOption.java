package ui;

import javafx.scene.control.Label;
import javafx.scene.layout.Pane;
import javafx.scene.layout.StackPane;

/**
 * Created by JordanLewis on 2/11/2015.
 */
public class SideMenuOption extends StackPane {
    Pane highlight = new Pane();
    Label optionLabel = new Label("Label");


    String optionSelected() {
        return optionLabel.getText();
    }

    void selectOption(Boolean isSelected) {
        if (isSelected) {
            // set background colour to red
            highlight.getStyleClass().add("highlight-on");
        } else {
            // set background colour to grey
            //highlight.getStyleClass().remove("highlight-on");
            highlight.getStyleClass().add("highlight-off");
        }
    }

    public SideMenuOption(String title) {
        optionLabel.setText(title);

        this.getChildren().add(highlight);
        this.getChildren().add(optionLabel);
    }
}
