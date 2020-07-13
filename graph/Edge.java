import java.util.ArrayList;
import java.util.List;

public class Edge {

    public Vertex vert1;
    public Vertex vert2;
    public ArrayList<Vertex> VertRep = new ArrayList<Vertex>(2);

    public Edge(Vertex vert1, Vertex vert2) {
        this.vert1 = vert1;
        this.vert2 = vert2;
        VertRep.add(0, vert1);
        VertRep.add(1, vert2);
        this.addEdgeToVertices();
    }
    @Override
    public String toString() {
        return ("(" + vert1 + ", " + vert2 +")");
    }

    public String toTitle() {
        return (vert1.toString() + vert2.toString());
    }

    public void addEdgeToVertices() {
        vert1.newEdgeVert(this, vert2.toString());
        vert2.newEdgeVert(this, vert1.toString());
    }

}
