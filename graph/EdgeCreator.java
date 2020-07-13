public class EdgeCreator {
    public EdgeCreator(String temp1, String temp2, String temp3) {
        if (Graphs.containsKey(temp1)) {
            Graphs.get(temp1).newEdge(temp2, temp3);
        }
    }
}
