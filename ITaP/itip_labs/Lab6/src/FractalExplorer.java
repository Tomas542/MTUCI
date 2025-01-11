import java.awt.BorderLayout;
import java.awt.Color;
import java.awt.geom.Rectangle2D;
import java.awt.event.*;
import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.JButton;
import javax.swing.JComboBox;
import javax.swing.JFileChooser;
import javax.swing.JLabel;
import javax.swing.JOptionPane;
import javax.swing.filechooser.FileFilter;
import javax.swing.filechooser.FileNameExtensionFilter;
import javax.swing.SwingWorker;

public class FractalExplorer {
    private int displaySize;
    private JImageDisplay display;
    private FractalGenerator fractal;
    private Rectangle2D.Double range;
    JComboBox<FractalGenerator> fractalCBox;
    JButton saveButton;
    JButton resetButton;
    int rowsRemaining;
    public FractalExplorer(int size) {
        this.displaySize = size;
        this.fractal = new Mandelbrot();
        this.range = new Rectangle2D.Double();
        fractal.getInitialRange(this.range);
        display = new JImageDisplay(displaySize, displaySize);
    }


    public void createAndShowGUI() {
        JFrame frame = new JFrame("Fractal Explorer");

        resetButton = new JButton("Reset");
        resetButton.setActionCommand("reset");

        saveButton = new JButton("Save");
        saveButton.setActionCommand("save");

        JLabel label = new JLabel("Fractal: ");
        fractalCBox	= new JComboBox<FractalGenerator>();

        JPanel cbPanel = new JPanel();
        cbPanel.add(label);
        cbPanel.add(fractalCBox);

        JPanel buttonPanel = new JPanel();
        buttonPanel.add(saveButton);
        buttonPanel.add(resetButton);

        fractalCBox.addItem(new Mandelbrot());
        fractalCBox.addItem(new BurningShip());
        fractalCBox.addItem(new Tricorn());

        MouseHandler click = new MouseHandler();
        display.addMouseListener(click);

        ActionHandler actHandler = new ActionHandler();
        resetButton.addActionListener(actHandler);
        saveButton.addActionListener(actHandler);
        fractalCBox.addActionListener(actHandler);

        frame.setLayout(new BorderLayout());
        frame.add(display, BorderLayout.CENTER);
        frame.add(buttonPanel, BorderLayout.SOUTH);
        frame.add(cbPanel, BorderLayout.NORTH);

        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        frame.pack();
        frame.setVisible(true);
        frame.setResizable(false);
    }

    public void enableUI(boolean val) {
        saveButton.setEnabled(val);
        resetButton.setEnabled(val);
        fractalCBox.setEnabled(val);
    }

    private void drawFractal() {
        enableUI(false);
        rowsRemaining = displaySize;
        for (int i = 0; i < displaySize; i++) {
            FractalWorker rowDrawer = new FractalWorker(i);
            rowDrawer.execute();
        }
    }


    public class ActionHandler implements ActionListener {
        public void actionPerformed(ActionEvent e) {
            if (e.getActionCommand().equals("reset")) {
                fractal.getInitialRange(range);
                drawFractal();
            }
            else if (e.getActionCommand().equals("save")) {
                JFileChooser chooser = new JFileChooser();
                FileFilter filter = new FileNameExtensionFilter("PNG Images", "png");
                chooser.setFileFilter(filter);
                chooser.setAcceptAllFileFilterUsed(false);
                int res = chooser.showSaveDialog(display);

                if (res == JFileChooser.APPROVE_OPTION) {
                    try {
                        javax.imageio.ImageIO.write(display.getBufferedImage(), "png",
                                chooser.getSelectedFile());
                    } catch (Exception e1) {
                        javax.swing.JOptionPane.showMessageDialog(display, e1.getMessage(), "Cannot Save Image",
                                JOptionPane.ERROR_MESSAGE);
                    }
                }
                else {
                    return;
                }
            }
            else if (e.getSource() == (Object) fractalCBox) {
                fractal = (FractalGenerator) fractalCBox.getSelectedItem();
                fractal.getInitialRange(range);
                drawFractal();
            }
        }
    }

    public class MouseHandler extends MouseAdapter {
        @Override
        public void mouseClicked(MouseEvent e) {
            if (rowsRemaining != 0) {return;}
            double xCoord = FractalGenerator.getCoord(range.x, range.x + range.width, displaySize, e.getX());
            double yCoord = FractalGenerator.getCoord(range.y, range.y + range.width, displaySize, e.getY());

            fractal.recenterAndZoomRange(range, xCoord, yCoord, 0.5);
            drawFractal();
        }
    }

    public static void main(String[] args) {
        FractalExplorer displayExplorer = new FractalExplorer(600);
        displayExplorer.createAndShowGUI();
        displayExplorer.drawFractal();
    }

    private class FractalWorker extends SwingWorker<Object, Object> {
        int rowY;
        int[] rgbVals;

        public FractalWorker(int yCoord) {
            rowY = yCoord;
        }

        public Object doInBackground() {
            rgbVals = new int[displaySize];
            double yCoord = FractalGenerator.getCoord(range.y,
                    range.y + range.width, displaySize, rowY);

            for (int i = 0; i < displaySize; i++) {
                double xCoord = FractalGenerator.getCoord(range.x,
                    range.x + range.width, displaySize, i);
                double numIters = fractal.numIterations(xCoord, yCoord);

                if (numIters == -1) {rgbVals[i] = 0;}
                else {
                    float hue = 0.7f + (float) numIters / 200f;
                    int rgbColor = Color.HSBtoRGB(hue, 1f, 1f);
                    rgbVals[i] = rgbColor;
                }
            }
            return null;
        }

        public void done() {
            for (int i = 0; i < displaySize; i++) {
                display.drawPixel(i, rowY, rgbVals[i]);
            }
            display.repaint(0, 0, rowY, displaySize, 1);
            rowsRemaining--;
            if (rowsRemaining == 0) {
                enableUI(true);
            }
        }
    }
}
