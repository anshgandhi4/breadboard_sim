import javafx.application.Application;
import javafx.scene.Scene;
import javafx.scene.image.Image;
import javafx.scene.layout.BorderPane;
import javafx.scene.layout.Pane;
import javafx.stage.Stage;

public class main extends Application {

    @Override
    public void start(Stage primaryStage) {
        BorderPane mainPane = new BorderPane();
        Pane simPane = new Pane();
        Breadboard breadboard = new Breadboard(simPane);
        mainPane.setCenter(simPane);

        Scene scene = new Scene(mainPane, 1200, 650);
        primaryStage.setTitle("Breadboard Sim");
        primaryStage.setScene(scene);
        primaryStage.getIcons().add(new Image("icon.png"));
        primaryStage.show();
    }
}