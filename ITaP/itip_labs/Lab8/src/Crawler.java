import java.util.LinkedList;

public class Crawler {


    public static void showResult(LinkedList<URLDepthPair> list){
        for (URLDepthPair c:list){
            System.out.println("Depth : "+c.getDepth() + "\tLink : "+c.getUrl());
        }
    }

    public static void main(String[] args) {
        String[] arg = new String[]{"http://www.consultant.ru/","3", "4"};
        String url = arg[0];
        int maxDepth = Integer.parseInt(arg[1]);
        int numThreads = Integer.parseInt(arg[2]);

        URLPool pool = new URLPool(maxDepth);
        pool.addPair(new URLDepthPair(url,0));
        for(int i = 0; i < numThreads; i ++){
            CrawlerTask c = new CrawlerTask(pool);
            Thread t = new Thread(c);
            t.start();
        }
        while(numThreads != pool.getWait()){
            try{
                Thread.sleep(500);
            }
            catch (InterruptedException e){}
        }
        try{
            showResult(pool.getViewedLinks());
        }
        catch(NullPointerException e){
            System.out.println("usage: java Crawler " + arg[0] + " " + arg[1] + " " + arg[2]);
        }
        System.exit(0);
    }
}
