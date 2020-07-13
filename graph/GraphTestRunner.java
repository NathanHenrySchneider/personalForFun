public class GraphTestRunner {

    public static void main(String[] args) {
/*
        System.out.println("");
        Graph graph1 = new Graph("alpha");
        graph1.newVertex("A");
        graph1.newVertex("B");
        graph1.newEdge("A", "B");
        graph1.newVertex("C");
        graph1.newVertex("A");
        graph1.newEdge("A", "B");
        graph1.newEdge("B", "A");
        graph1.printDegree("A");
        graph1.printDegree("Z");

        System.out.println("");

        Graph graph2 = new Graph("beta");
        graph2.newVertex("A");
        graph2.newEdge("A", "B");
        graph2.newEdge("C","D");
        graph2.printVertices();
        graph2.printDegree("B");

        System.out.println("");

        Graph graph3 = new Graph("gamma");
        graph3.newEdge("A", "Z");
        graph3.printEdgesOfVert("B");
        graph3.printEdgesOfVert("A");
        graph3.printEdges();
        graph3.newEdge("B", "A");
        graph3.newEdge("X", "A");
        graph3.printEdgesOfVert("A");
        graph3.printDegree("A");
        graph3.printDegreeSequence();
        graph3.printNeighborhoodOfVertex("A");
        System.out.println("\n");
        System.out.println("\n");
        System.out.println("gamma DFS test");
        System.out.println(graph3.isConnected());

        System.out.println("");


        Graph graph4 = new Graph("zeta");
        graph4.newEdge("a", "b");
        graph4.newEdge("a", "c");
        graph4.newEdge("c", "d");
        graph4.newEdge("d", "e");
        //graph4.newEdge("x", "z");
        //graph4.newEdge("d", "f");
        graph4.newVertex("a");
        graph4.printVertices();
        //System.out.println(graph4.DFS());
        System.out.println(graph4.isConnected());

*/

        Graph graph5 = new Graph("yote");
        graph5.newEdge("a", "e");
        graph5.newEdge("e", "c");
        graph5.newEdge("a", "b");
        graph5.newEdge("b", "c");
        graph5.newEdge("d", "c");
        System.out.println(graph5.isConnected());
        System.out.println("\n");
        System.out.println(graph5.isCycleGraph());

        System.out.println("");
    }


}
