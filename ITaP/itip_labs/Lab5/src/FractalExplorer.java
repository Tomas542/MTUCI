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

public class FractalExplorer {
    private int displaySize;
    private JImageDisplay display;
    private FractalGenerator fractal;
    private Rectangle2D.Double range;
    JComboBox<FractalGenerator> fractalCBox;

    public FractalExplorer(int size) {
        this.displaySize = size;
        this.fractal = new Mandelbrot();
        this.range = new Rectangle2D.Double();
        fractal.getInitialRange(this.range);
        display = new JImageDisplay(displaySize, displaySize);
    }


    public void createAndShowGUI() {
        JFrame frame = new JFrame("Fractal Explorer");

        JButton resetButton = new JButton("Reset");
        resetButton.setActionCommand("reset");

        JButton saveButton = new JButton("Save");
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


    private void drawFractal() {

        for (int x = 0; x < displaySize; x++) {
            for (int y = 0; y < displaySize; y++) {
                double xCoord = FractalGenerator.getCoord(range.x,
                        range.x + range.width, displaySize, x);
                double yCoord = FractalGenerator.getCoord(range.y,
                        range.y + range.width, displaySize, y);
                double numIters = fractal.numIterations(xCoord, yCoord);

                if (numIters == -1) {
                    display.drawPixel(x, y, 0);
                }
                else {
                    float hue = 0.7f + (float) numIters / 200f;
                    int rgbColor = Color.HSBtoRGB(hue, 1f, 1f);
                    display.drawPixel(x, y, rgbColor);
                }
            }
        }
        display.repaint();
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
}
