public ArrayList<String> DFSwithSeed(String origin) {
    ArrayList<String> holder = new ArrayList<String>();
    Stack<Vertex> s = new Stack<Vertex>();
    //Vertex[] vertArr = Vertices.values().toArray(new Vertex[Vertices.size()]);
    s.push(Vertices.get(origin));
    Vertices.get(origin).visited = true;
    holder.add(origin);
    int count = 1;
    while(!s.isEmpty()) {
        Vertex n = (Vertex)s.peek();
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
        for (String b : tempSub) {
            allReached.add(b);
        }
    }
    for (ArrayList<String> s : subGraphs) {
        check.add(this.cycleTestSub(s.get(0)));
    }
    for (int i = 0; i < checked.size(); i++) {
        if (!checked.get(i).isEmpty()) {
            last.add(checked.get(i));
        }
    }
    return last;
}

public ArrayList<String> DFSwithSeed(String origin) {
    ArrayList<String> holder = new ArrayList<String>(0);
    Stack<Vertex> s = new Stack<Vertex>();
    s.push(Vertices.get(origin));
    Vertices.get(origin).visited = true;
    int count = 1;
    while (!s.empty()) {
        Vertex n = s.peek();
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
        } else {
            s.pop();
        }
    }
    this.setVisitedToFalse();
    return holder;
}

public ArrayList<String> cycleTestSub(String passedHead) {
    ArrayList<String> cycle = new ArrayList<String>(0);
    int visitedCount = 0;
    Stack<Vertex> s = new Stack<Vertex>();
    s.push(Vertices.get(passedHead));
    Vertex head = s.peek();
    head.visited = true;
    visitedCount++;
    while (!s.empty()) {
        Vertex n = s.peek();
        LinkedList<Vertex> tempLinked = adj.get(n.toString());
        Vertex child = null;
        for (Vertex v : tempLinked) {
            if (!v.visited && child == null) {
                child = v;
            }
        }
        if (child != null) {
            visitedCount++;
            s.push(child);
            child.visited = true;
        } else {
            s.pop();
        }
        if (visitedCount > 2 && tempLinked.contains(head)) {
            this.setVisitedToFalse();
            while (!s.empty()) {
                cycle.add(s.pop().toString());
            }
            return cycle;
        }
    }
    return cycle;
}
