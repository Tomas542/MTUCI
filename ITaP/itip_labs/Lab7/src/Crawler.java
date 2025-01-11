import java.io.*;
import java.net.*;
import java.util.*;

public class Crawler {
    static LinkedList<URLDepthPair> foundLink = new LinkedList<URLDepthPair>();
    static LinkedList<URLDepthPair> viewedLink = new LinkedList<URLDepthPair>();
    static String line;

    public static void main(String[] args) {
        String[] arg = new String[]{"http://mathprofi.ru/","1"};

        try {
            search(arg[0], Integer.parseInt(arg[1]));
        } catch (NumberFormatException | IOException e) {
            System.out.println(1);
        }
    }

    public static void request(PrintWriter out,URLDepthPair pair) throws MalformedURLException {
        out.println("GET " + pair.getPath() + " HTTP/1.1");
        out.println("Host: " + pair.getHost());
        out.println("Connection: close");
        out.println();
        out.flush();
    }

    public static void getSites(LinkedList<URLDepthPair> list){
        for (URLDepthPair c:viewedLink){
            System.out.println("Depth : "+c.getDepth() + "\tLink : "+c.getUrl());
        }
    }


    public static void search(String pair, int maxDepth) throws IOException{
        foundLink.add(new URLDepthPair(pair,0));
        while (!foundLink.isEmpty()) {
            URLDepthPair current = foundLink.removeFirst();
            if (current.getDepth() < maxDepth) {
                Socket my_socket = new Socket(current.getHost(), 80);
                my_socket.setSoTimeout(2000);
                try{
                    BufferedReader in = new BufferedReader(new InputStreamReader(my_socket.getInputStream()));
                    PrintWriter out = new PrintWriter(my_socket.getOutputStream(), true);
                    request(out, current);
                    while ((line = in.readLine()) != null){
                        if (line.contains(URLDepthPair.URL_PREFIX) && line.indexOf('"') != -1) {
                            StringBuilder currentLink = new StringBuilder();
                            int i = line.indexOf(URLDepthPair.URL_PREFIX);
                            while (line.charAt(i) != '"' && line.charAt(i) != ' ') {
                                currentLink.append(line.charAt(i));
                                i++;
                            }
                            URLDepthPair newPair = new URLDepthPair(currentLink.toString(), current.depth + 1);
                            if (current.check(foundLink, newPair) && current.check(viewedLink, newPair) && !current.URL.equals(newPair.URL))
                                foundLink.add(newPair);
                        }
                    }
                    my_socket.close();
                } catch(SocketTimeoutException e){
                    my_socket.close();
                }
            }
            viewedLink.add(current);
        }
        getSites(viewedLink);
    }
}



