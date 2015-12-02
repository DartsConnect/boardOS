package register;

/**
 * Created by JordanLewis on 2/12/2015.
 */

import javafx.fxml.Initializable;
import org.parse4j.Parse;
import java.net.URL;
import java.util.ResourceBundle;

public class RegisterUserController implements Initializable {

    private void cancel() {
        // Return to the main scene
    }

    private boolean registerUser(String username, String email, String password) {

        return true;
    }

    @Override
    public void initialize(URL location, ResourceBundle resources) {
        System.out.println("View is now loaded!");
    }

    public RegisterUserController() {

    }
}
