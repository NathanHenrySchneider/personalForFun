import java.util.ArrayList;
import java.util.List;
import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;
import java.util.Collections;
import java.util.Stack;
import java.util.LinkedList;

public class Graph {

    public Map<String, LinkedList<Vertex>> adjList = new HashMap<>(0);

    public String GraphName;
    public Map<String, Edge> Edges = new HashMap<>(0);
    public Map<String, Vertex> Vertices = new HashMap<>(0);

    public Graph(String args) {
        GraphName = args;
        System.out.println("The new graph " + args + " was succesfully instantiated");
    }

    @Override
    public String toString() {
        return this.GraphName;
    }

    public void printEdges() {
        System.out.print("The graph " + this + " has the edges: ");
        ArrayList<Edge> valuesList = new ArrayList<Edge>(Edges.values());
        for (int i = 0; i < Edges.size(); i++) {
            System.out.print(valuesList.get(i) + "\t");
        }
        System.out.println("");
    }
///////////////
    public void printEdgesOfVert(String temp) {
        if (!this.vertCheck(temp)) {
            System.out.println("The vertex " + temp + " does not exist in the graph " + this);
        } else {
            this.Vertices.get(temp).printEdges();
        }
    }

    public ArrayList<String> getVertices() {
        ArrayList<String> vertsFromGraph = new ArrayList<String>();
        if (this.Vertices.size() == 0) {
            return vertsFromGraph;
        } else {
            String[] temp = Vertices.keySet().toArray(new String[Vertices.size()]);
            for (int i = 0; i < Vertices.size(); i++) {
                vertsFromGraph.add(temp[i]);
            }
            Collections.sort(vertsFromGraph);
            return vertsFromGraph;
        }

    }

    public ArrayList<String> getEdges() {
        ArrayList<String> edgesFromGraph = new ArrayList<String>();
        if (this.Edges.size() == 0) {
            return edgesFromGraph;
        } else {
            Edge[] temp = Edges.values().toArray(new Edge[Edges.size()]);
            for (int i = 0; i < Edges.size(); i++) {
                System.out.println(temp[i]);
                if(temp[i] != null){
                    edgesFromGraph.add(temp[i].toString());
                }
            }
            Collections.sort(edgesFromGraph);
            return edgesFromGraph;
        }

    }

    public void printNeighborhoodOfVertex(String temp) {
        this.Vertices.get(temp).printNeighborhood();
    }

    public void printVertices() {
        if (this.Vertices.size() != 0) {
            System.out.print("The graph " + this + " has the vertices: ");
            ArrayList<Vertex> valuesList = new ArrayList<Vertex>(Vertices.values());
            for (int i = 0; i < Vertices.size(); i++) {
                System.out.print(valuesList.get(i) + "   ");
            }
            System.out.println("");
        } else {
            System.out.println("The graph " + this + " has no vertices");
        }
    }

    public String getName(Graph temp) {
        return temp.GraphName;
    }

    // checks to see if a vertex exists in the graph
    public boolean vertCheck(String vert) {
        return this.Vertices.containsKey(vert);
    }
    // checks to see if an edge exists in the graph
    public boolean edgeCheck(String vertA, String vertB) {
        String temp1 = (vertA + vertB);
        String temp2 = (vertB + vertA);
        return (this.Edges.containsKey(temp1) || this.Edges.containsKey(temp2));
    }
    // creates a new vertex
    public void newVertex(String newVert) {
        if (this.vertCheck(newVert)) {
            System.out.println("A vertex with the name " + newVert + " already exists in the graph " + this);
        } else {
            this.Vertices.put(newVert, new Vertex(newVert, this.GraphName));
            this.adjList.put(newVert, new LinkedList<Vertex>());
            System.out.println("The new vertex " + newVert + " was succesfully instantiated in the graph " + this);
        }
    }
    // creates a new edge
    public void newEdge(String vertA, String vertB) {
        String temp = (vertA + vertB);
        if (this.edgeCheck(vertA, vertB)) {
            System.out.println("An edge between " + vertA + " and " + vertB + " already exists in the graph " + this);
        } else {
            if (!this.vertCheck(vertA)) {
                this.newVertex(vertA);
                System.out.println("A new vertex " + vertA + " was created because it did not already exist in the graph " + this);
            }
            if (!this.vertCheck(vertB)) {
                this.newVertex(vertB);
                System.out.println("A new vertex " + vertB + " was created because it did not already exist in the graph "+ this);
            }
            this.Edges.put(temp, new Edge(this.Vertices.get(vertA), this.Vertices.get(vertB)));
            this.adjList.get(vertA).add(this.Vertices.get(vertB));
            this.adjList.get(vertB).add(this.Vertices.get(vertA));
            System.out.println("The new edge from " + vertA + " to " + vertB + " was succesfully instantiated in the graph " + this);
        }
    }

    public void printDegree(String temp) {
        if (this.vertCheck(temp)){
            System.out.println("The vertex " + temp + " from the graph " + this + " has degree: " + this.Vertices.get(temp).getDegree());
        } else {
            System.out.println("The graph " + this + " does not contain the vertex " + temp);
        }
    }

    public int getDegreeGraphVersion(String temp1) {
        return this.Vertices.get(temp1).getDegree();
    }

    public List<Integer> getDegreeSequence() {
        List<Integer> degreeSequence = new ArrayList<Integer>();
        if (Vertices.size() == 0) {
            degreeSequence.add(0);
            return degreeSequence;
        } else {
            Vertex[] temp = Vertices.values().toArray(new Vertex[Vertices.size()]);
            for (int i = 0; i < Vertices.size(); i++) {
                degreeSequence.add(temp[i].getDegree());
            }
            Collections.sort(degreeSequence);
            Collections.reverse(degreeSequence);
            return degreeSequence;
        }
    }

    public void printDegreeSequence() {
        List<Integer> temp = this.getDegreeSequence();
        if (this.Vertices.size() == 0) {
            System.out.println("There are no vertices in the graph " + this + " so it has no degree sequence");
        } else {
            System.out.print("The graph " + this + " has the degree sequence: ");
            for (int i = 0; i < temp.size(); i++) {
                System.out.print(temp.get(i) + " ");
            }
            System.out.println("");
        }
    }

    public boolean isConnected() {
        if (this.DFSforConnection().size() < Vertices.size()) {
            return false;
        } else {
            return true;
        }
    }

    public ArrayList<String> DFSforConnection() {
        ArrayList<String> holder = new ArrayList<String>(0);
        Stack<Vertex> s = new Stack<Vertex>();
        Vertex[] vertArr = Vertices.values().toArray(new Vertex[Vertices.size()]);
        s.push(Vertices.get(vertArr[0].toString()));
        vertArr[0].visited = true;
        holder.add(vertArr[0].toString());
        int count = 1;
        while(!s.empty()) {
            Vertex n = /*(Vertex)*/s.peek();
            //System.out.println(n);
            LinkedList<Vertex> tempLinked = adjList.get(n.toString());
            Vertex child = null;
            for (Vertex v : tempLinked) {
                if (!v.visited && child == null) {
                    child = v;
                }
            }
            if (child != null) {
                count++;
                s.push(child);
                child.visited = true;
                holder.add(child.toString());
                System.out.println(child.toString());
            } else {
                s.pop();
            }
        }
        System.out.println("Start of for loop");
        for (int i = 0; i < count; i++) {
            System.out.println(holder.get(i));
            if (holder.get(i) != null) {
                Vertices.get(holder.get(i)).visited = false;
            }
        }
        System.out.println(holder);
        System.out.println(holder.size());
        return holder;
    }

    public void setVisitedToFalse() {
        for (String v : Vertices.keySet()) {
            Vertices.get(v).visited = false;
        }
    }

    ///////////////////////////////////////////////////
    ///////////////////////////////////////////////////
    ///////////////////////////////////////////////////
    ///////////////////////////////////////////////////
    ///////////////////////////////////////////////////

    public ArrayList<ArrayList<String>> isCycleGraph() {
        ArrayList<ArrayList<String>> subGraphs = new ArrayList<ArrayList<String>>(0);
        ArrayList<ArrayList<String>> checked = new ArrayList<ArrayList<String>>(0);
        ArrayList<ArrayList<String>> last = new ArrayList<ArrayList<String>>(0);
        ArrayList<String> allReached = new ArrayList<String>(0);
        while (allReached.size() < Vertices.size()) {
            String temp = null;
            for (String a : this.Vertices.keySet()) {
                if (!allReached.contains(a) && temp == null) {
                    temp = a;
                }
            }
            ArrayList<String> tempSub = DFSwithSeed(temp);
            subGraphs.add(tempSub);
            System.out.println(tempSub);
            for (String b : tempSub) {
                allReached.add(b);
            }
        }
        for (ArrayList<String> s : subGraphs) {
            checked.add(this.cycleTestSub(s.get(0)));
        }
        for (int i = 0; i < checked.size(); i++) {
            if (!checked.get(i).isEmpty()) {
                last.add(checked.get(i));
            }
        }
        return last;
    }

    public ArrayList<String> DFSwithSeed(String origin) {
        ArrayList<String> cycle = new ArrayList<String>(0);
        ArrayList<String> holder = new ArrayList<String>(0);
        holder.add(origin);
        Stack<Vertex> s = new Stack<Vertex>();
        s.push(Vertices.get(origin));
        Vertices.get(origin).visited = true;
        int count = 1;
        while (!s.empty()) {
            Vertex n = s.peek();
            LinkedList<Vertex> tempLinked = adjList.get(n.toString());
            Vertex child = null;
            int cycCount = 0;
            for (Vertex v : tempLinked) {
                if (!v.visited && child == null) {
                    child = v;
                } else if (v.visited && count > 2) {
                    boolean l = true;
                    while (!s.empty() && l) {
                        if (s.peek().equals(v)) {
                            l = false;
                        } else {
                            cycle.add(s.pop().toString());
                        }
                    }
                    System.out.println(cycle);
                    this.setVisitedToFalse();
                    return cycle;
                }
            }

            if (child != null) {
                count++;
                s.push(child);
                child.visited = true;
                holder.add(child.toString());
            } else {
                s.pop();
            }
        }
        this.setVisitedToFalse();
        return cycle;
    }

    public ArrayList<String> cycleTestSub(String passedHead) {
        System.out.println(passedHead);
        ArrayList<String> cycle = new ArrayList<String>(0);
        int visitedCount = 0;
        Stack<Vertex> s = new Stack<Vertex>();
        s.push(Vertices.get(passedHead));
        Vertex head = s.peek();
        head.visited = true;
        visitedCount++;
        while (!s.empty()) {
            Vertex n = s.peek();
            System.out.println(n);
            LinkedList<Vertex> tempLinked = adjList.get(n.toString());
            Vertex child = null;
            for (Vertex v : tempLinked) {
                if (!v.visited && child == null) {
                    child = v;
                }
            }
            if (visitedCount > 2 && tempLinked.contains(head)) {
                this.setVisitedToFalse();
                while (!s.empty()) {
                    cycle.add(s.pop().toString());
                }
                return cycle;
            }
            if (child != null) {
                visitedCount++;
                s.push(child);
                child.visited = true;
            } else {
                visitedCount--;
                s.pop();
            }
        }
        return cycle;
    }

}
