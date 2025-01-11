import java.util.LinkedList;

public class URLPool {
    LinkedList<URLDepthPair> viewedLinks;
    LinkedList<URLDepthPair> foundLink;
    int maxDepth;
    int waiters;

    public URLPool(int maxDepth){
        this.maxDepth = maxDepth;
        foundLink = new LinkedList<URLDepthPair>();
        viewedLinks = new LinkedList<URLDepthPair>();
        waiters = 0;
    }

    public synchronized URLDepthPair getPair(){
        while(foundLink.size() == 0){
            waiters++;
            try{
                wait();
            }
            catch (InterruptedException e){
                System.out.println("Interrupted Exception");
            }
            waiters--;
        }
        return foundLink.removeFirst();
    }

    public synchronized void addPair(URLDepthPair pair){
        if(URLDepthPair.check(viewedLinks, pair)){
            viewedLinks.add(pair);
            if (pair.getDepth()<maxDepth){
                foundLink.add(pair);
                notify();
            }
        }
    }

    public int getWait() {
        return waiters;
    }

    public LinkedList<URLDepthPair> getViewedLinks(){
        return viewedLinks;
    }
}