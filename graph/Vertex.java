import java.util.ArrayList;
import java.util.List;
import java.util.HashMap;
import java.util.Map;
import java.util.Collections;

public class Vertex {

    public String name;
    public Map<String, Edge> EdgesOfVert = new HashMap<String, Edge>(0);
    public int deg = EdgesOfVert.size();
    public ArrayList<String> neighborhood = new ArrayList<String>(0);
    public boolean visited = false;
    public String graphName = "";

    public Vertex(String name, String g) {
        this.name = name;
        this.graphName = g;
    }

    public String toString() {
        return this.name;
    }

    public void printNeighborhood() {
        if (this.neighborhood.size() == 0) {
            System.out.println("The vertex " + this + " has no neighbors");
        } else {
            System.out.print("The vertex has neighborhood: ");
            for (int i = 0; i < this.neighborhood.size(); i++) {
                System.out.print(neighborhood.get(i) + "  ");
            }
        }
    }

    public List<String> getNeighborhood() {
        List<String> neighborhoodSet = new ArrayList<String>(this.neighborhood.size());
        if (this.neighborhood.size() == 0) {
            return neighborhoodSet;
        } else {

            for (int i = 0; i < this.neighborhood.size(); i++) {
                neighborhoodSet.add(neighborhood.get(i));
            }
            Collections.sort(neighborhoodSet);
            return neighborhoodSet;
        }
    }

    public void newEdgeVert(Edge temp, String temp1) {
        this.EdgesOfVert.put(temp.toTitle(), temp);
        deg = EdgesOfVert.size();
        neighborhood.add(temp1);
    }

    public void printEdges() {
        System.out.print("The vertex " + this + " has the edges: ");
        ArrayList<Edge> valuesList = new ArrayList<Edge>(EdgesOfVert.values());
        for (int i = 0; i < EdgesOfVert.size(); i++) {
            System.out.print(valuesList.get(i) + "   ");
        }
        System.out.println("");
    }

    public void printDegree() {
        System.out.println(this.deg);
    }

    public int getDegree() {
        return this.deg;
    }

    public boolean equals(Object other) {
        if (other == this) {return true;}
        if (!(other instanceof Vertex)) {return false;}
        Vertex temp = (Vertex)other;
        return (temp.name.equals(name) && temp.graphName.equals(graphName));
    }

}
