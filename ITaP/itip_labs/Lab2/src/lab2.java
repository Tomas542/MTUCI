public class lab2 {
    public static void main(String[] args){
        double[] xyz = new double[9];

        for (int i = 0; i < args.length; i++){
            String str = args[i];
            double num = Double.parseDouble(str);

            if(i > 8){
                System.out.println("Много чисел");
                break;
            }

            xyz[i] = num;
        }

        Point3d point1 = new Point3d(xyz[0], xyz[1], xyz[2]);
        Point3d point2 = new Point3d(xyz[3], xyz[4], xyz[5]);
        Point3d point3 = new Point3d(xyz[6], xyz[7], xyz[8]);

        if (computeArea(point1, point2, point3) != -1){
            System.out.println(computeArea(point1, point2, point3));
        }
        else System.out.println("Некоторые точки равны");
    }

    public static double computeArea(Point3d a, Point3d b, Point3d c){
        if (samePoints(a, b, c)) {return -1;}

        double sideA = a.distanceTo(b.getX(), b.getY(),b.getZ());
        double sideB = b.distanceTo(c.getX(), c.getY(), c.getZ());
        double sideC = a.distanceTo(c.getX(), c.getY(), c.getZ());

        double p = (sideA + sideB + sideC)/2;
        p = (Math.ceil(p*100))/100;
        double area = Math.sqrt(p*(p-sideA)*(p-sideB)*(p-sideC));
        area = (Math.ceil(area * 100)) / 100;

        return area;
    }

    public static boolean samePoints(Point3d a, Point3d b, Point3d c){
        if (a.getX() == b.getX() & a.getY() == b.getY() & a.getZ() == b.getZ()) {return true;}
        if (a.getX() == c.getX() & a.getY() == c.getY() & a.getZ() == c.getZ()) {return true;}

        return b.getX() == c.getX() & b.getY() == c.getY() & b.getZ() == c.getZ();
    }
}
