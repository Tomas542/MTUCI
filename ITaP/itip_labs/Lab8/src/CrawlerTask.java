import java.io.*;
import java.net.*;

public class CrawlerTask implements Runnable {
    URLPool URLPool;

    public CrawlerTask(URLPool pool){
        URLPool = pool;
    }

    public static void request(PrintWriter out, URLDepthPair pair) throws MalformedURLException {
        out.println("GET " + pair.getPath() + " HTTP/1.1");
        out.println("Host: " + pair.getHost());
        out.println("Connection: close");
        out.println();
        out.flush();
    }

    @Override
    public void run() {
        while (true) {
            URLDepthPair currentPair = URLPool.getPair();
            try {
                Socket my_socket = new Socket(currentPair.getHost(), 80);
                my_socket.setSoTimeout(10000);
                try {
                    PrintWriter out = new PrintWriter(my_socket.getOutputStream(), true);
                    BufferedReader in =  new BufferedReader(new InputStreamReader(my_socket.getInputStream()));
                    request(out,currentPair);
                    String line = in.readLine();
                    while (line != null){
                        if (line.contains(URLDepthPair.URL_PREFIX) && line.indexOf('"') != -1) {
                            StringBuilder currentLink = new StringBuilder();
                            int i = line.indexOf(URLDepthPair.URL_PREFIX);
                            while (line.charAt(i) != '"' && line.charAt(i) != ' ') {
                                currentLink.append(line.charAt(i));
                                i++;
                            }
                            URLDepthPair newPair = new URLDepthPair(currentLink.toString(), currentPair.depth + 1);
                            URLPool.addPair(newPair);
                        }
                        line = in.readLine();
                    }
                    my_socket.close();
                } catch (SocketTimeoutException e) {
                    my_socket.close();
                }
            }
            catch (IOException e) {
                System.out.println("IOEception caught");
            }
        }
    }
}