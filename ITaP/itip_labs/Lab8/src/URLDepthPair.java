import java.net.*;
import java.util.LinkedList;


public class URLDepthPair {
    public final static String URL_PREFIX = "http://";
    public String URL;
    public int depth;

    public URLDepthPair (String URL, int depth) {
        this.URL = URL;
        this.depth = depth;
    }

    public int getDepth() {
        return depth;
    }

    public String getUrl() {
        return URL;
    }

    public void setDepth(int depth) {
        this.depth = depth;
    }

    public void setUrl(String URL) {
        this.URL = URL;
    }

    public String getHost() throws MalformedURLException {
        URL host = new URL(URL);
        return host.getHost();
    }
    public String getPath() throws MalformedURLException {
        URL path = new URL(URL);
        return path.getPath();
    }

    @Override
    public String toString() {
        return "URLDepthPair{" +
                "url='" + URL + '\'' +
                ", depth=" + depth +
                '}';
    }

    public static boolean check(LinkedList<URLDepthPair> viewedLinks, URLDepthPair pair) {
        boolean isAlready = true;
        for (URLDepthPair i : viewedLinks)
            if (i.getUrl().equals(pair.getUrl()))
                isAlready=false;
        return isAlready;
    }
}
