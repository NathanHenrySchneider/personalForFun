public ArrayList<String> cycleTestForGraph() {
    if (this.isConnected()) {
        return this.cycleTestForSubGraph();
    } else {

    }



    ArrayList<String> allVertReached = this.DFS();
    ArrayList<String> firstRun = this.cycleTestForGraph();
    if (!firstRun.isEmpty()) {
        return firstRun;
    } else {
        while (allVertReached.length() < Vertices.length()) {
            String nextVert;
            for (String temp : Vertices.keySet()) {
                if (!allVertReached.contains(temp)) {
                    nextVert = temp;
                }
            }
            ArrayList<String> tempArr =
        }
    }

}

public ArrayList<String> cycleTestForSubGraph() {
    //boolean cyclical = false;
    ArrayList<String> cycle = new ArrayList<String>();
    int visitedCount = 0;
    //ArrayList<String> holder = new ArrayList<String>();
    Stack<Vertex> s = new Stack<Vertex>();
    Vertex[] vertArr = Vertices.values().toArray(new Vertex[Vertices.size()]);
    s.push(Vertices.get(vertArr[0].toString()));
    Vertex head = vertArr[0];
    vertArr[0].visited = true;
    //holder.add(vertArr[0].toString());
    visitedCount++;
    //int count = 1;
    while(!s.isEmpty()) {
        Vertex n = (Vertex)s.peek();
        //System.out.println(n);
        LinkedList<Vertex> tempLinked = adjList.get(n.toString());
        Vertex child = null;
        for (Vertex v : tempLinked) {
            if (!v.visited && child == null) {
                child = v;
            }
            System.out.println("YOTE");
            if (visitedCount > 2 && tempLinked.contains(head)) {
                System.out.println("YEEE");
                //cyclical = true;
                while (!s.empty()) {
                    System.out.println("ETOY");
                    cycle.add(s.pop().toString());
                }
                System.out.println(cycle);
                return cycle;
            }
        }
        if (child != null) {
            visitedCount++;
            s.push(child);
            child.visited = true;
            //holder.add(child.toString());
            System.out.println(child.toString());
        } else {
            s.pop();
        }
    }
    //System.out.println("Start of for loop");
    for (int i = 0; i < count; i++) {
        System.out.println(holder.get(i));
        if (holder.get(i) != null) {
            Vertices.get(holder.get(i)).visited = false;
        }
    }
    System.out.println(cycle);
    return cycle;
}
public ArrayList<String> cycleTestForSubGraph(String passedHead) {
    boolean cyclical = false;
    ArrayList<String> cycle = new ArrayList<String>(0);
    int visitedCount = 0;
    //ArrayList<String> holder = new ArrayList<String>();
    Stack<Vertex> s = new Stack<Vertex>();
    //Vertex[] vertArr = Vertices.values().toArray(new Vertex[Vertices.size()]);
    s.push(Vertices.get(passedHead);
    Vertex head = s.pop();
    head.visited = true;
    //holder.add(vertArr[0].toString());
    visitedCount++;
    //int count = 1;
    while(!s.isEmpty()) {
        Vertex n = (Vertex)s.peek();
        //System.out.println(n);
        LinkedList<Vertex> tempLinked = adjList.get(n.toString());
        Vertex child = null;
        for (Vertex v : tempLinked) {
            if (!v.visited && child == null) {
                child = v;
            }
            System.out.println("YOTE");
            if (visitedCount > 2 && tempLinked.contains(head)) {
                System.out.println("YEEE");
                cyclical = true;
                while (!s.empty()) {
                    System.out.println("ETOY");
                    s.pop().visited = false;
                    cycle.add(s.pop().toString());
                }
                System.out.println(cycle);
                return cycle;
            }
        }
        if (child != null) {
            visitedCount++;
            s.push(child);
            child.visited = true;
            //holder.add(child.toString());
            System.out.println(child.toString());
        } else {
            s.pop();
        }
    }
    System.out.println(cycle);
    return cycle;
}
