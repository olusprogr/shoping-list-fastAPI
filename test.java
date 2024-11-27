import java.awt.Color;
import sas.*;
import java.util.Random;

public class Main {
    View win;
    private Random random = new Random();
    
    
    public Main() {
        int winWidth = 1400;
        int winHeight = 900;
        
        win = new View(winWidth, winHeight);
        
        this.StartAnimations();
    }
    
    private void StartAnimations() {
        while (true) {
            System.out.println(generateRandomNumber(new int[]{0, 1400}));
            
        }
    }
    
    private int generateRandomNumber(int[] interval) {
        int lowerBound = interval[0];
        int upperBound = interval[1];
        
        return random.nextInt(upperBound - lowerBound + 1) + lowerBound;
    }
}
