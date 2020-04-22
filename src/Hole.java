import javafx.scene.paint.Color;
import javafx.scene.shape.Rectangle;

public class Hole extends Rectangle {

    public static final int size = 20;
    public int r,c;

    public Hole(int x, int y, int r, int c) {
        setX(x); setY(y); setWidth(size); setHeight(size);
        setFill(Color.WHITE);
        setStroke(Color.GRAY);
        this.r = r; this.c = c;
    }
}
