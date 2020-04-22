import javafx.scene.layout.Pane;
import javafx.scene.text.Text;

public class Breadboard {

    private Hole[][] holeArr;
    private final int cols = 50, rows = 14;

    public Breadboard(Pane pane) {
        holeArr = new Hole[rows][cols];
        String[] lbs = {"+","-","","a","b","c","d","e","","f","g","h","i","j","","-","+"};
        int x = 50, y = 150;
        for (int r = 0; r < rows+3; r++) {
            for (int c = 0; c < cols; c++) {
                if (r != 2 && r != 8 && r != 14) {
                    int locR = r;
                    if (r > 2) locR--;
                    if (r > 8) locR--;
                    if (r > 14) locR--;
                    Hole hole = new Hole(x+c*Hole.size,y+r*Hole.size, locR,c+1);
                    holeArr[locR][c] = hole;
                    hole.setOnMouseClicked(e -> {
                        System.out.println(hole.r + " " + hole.c);
                    });
                    pane.getChildren().add(hole);

                    if (c == 0) {
                        Text text = new Text(x-12,(y+r*Hole.size)+(Hole.size-7),lbs[r]);
                        pane.getChildren().add(text);
                    } else if (c == cols - 1) {
                        Text text = new Text((x+(c+1)*Hole.size)+5,(y+r*Hole.size)+(Hole.size-7),lbs[r]);
                        pane.getChildren().add(text);
                    }
                } else if (r == 2 || r == 14) {
                    Text text = new Text((x+c*Hole.size)+4,(y+r*Hole.size)+(Hole.size-5),(c+1) +"");
                    pane.getChildren().add(text);
                }
            }
        }
    }
}
