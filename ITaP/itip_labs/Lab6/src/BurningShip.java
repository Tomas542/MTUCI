import java.awt.geom.Rectangle2D;

public class BurningShip extends FractalGenerator {

    public static final int MAX_ITERATIONS = 2000;


    public void getInitialRange(Rectangle2D.Double range) {
        range.x = -2;
        range.y = -2.5;
        range.width = 4;
        range.height = 4;
    }


    public int numIterations(double x, double y) {
        double magSq;
        double zReal = x;
        double zImaginary = y;
        int iteration = 0;

        while (iteration < MAX_ITERATIONS && zReal * zReal + zImaginary * zImaginary < 4) {
            double zRealUpdated = x + Math.abs(zReal) * Math.abs(zReal)
                    - Math.abs(zImaginary) * Math.abs(zImaginary);
            double zImaginaryUpdated = y + 2 * Math.abs(zReal) * Math.abs(zImaginary);
            zReal = zRealUpdated;
            zImaginary = zImaginaryUpdated;
            iteration += 1;
        }

        if(iteration == MAX_ITERATIONS) {return -1;}
        return iteration;
    }

    public String toString() {
        return "Burning Ship";
    }
}