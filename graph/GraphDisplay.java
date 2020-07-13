import javafx.application.Application;
import javafx.event.ActionEvent;
import javafx.event.EventHandler;
import javafx.scene.Scene;
import javafx.scene.layout.StackPane;
import javafx.stage.Stage;
import javafx.scene.control.Button;
import javafx.scene.control.Control;
import javafx.scene.control.ListView;
import javafx.scene.control.TextField;
import javafx.scene.control.ComboBox;
import javafx.scene.layout.HBox;
import javafx.scene.layout.VBox;
import javafx.collections.FXCollections;
import javafx.collections.ObservableList;
import javafx.beans.binding.Bindings;
import java.util.ArrayList;
import java.util.List;
import java.util.HashMap;
import java.util.Map;
import javafx.scene.layout.HBox;
import javafx.scene.layout.VBox;
import javafx.scene.control.Label;

//Make vertex and edge comparable

public class GraphDisplay extends Application {

    Map<String, Graph> Graphs = new HashMap<>();

    public void newVertDisplay(String temp1, String temp2) {
        Graphs.get(temp2).newVertex(temp1);
    }

    public void start (Stage stage) {

        ObservableList<String> ErrorMessages = FXCollections.observableArrayList();
        ListView<String> listView3 = new ListView<String>(ErrorMessages);

        ObservableList<String> RequestedInfo = FXCollections.observableArrayList();
        ListView<String> listView6 = new ListView<String>(RequestedInfo);

        ObservableList<String> vertexes = FXCollections.observableArrayList();

        ObservableList<String> NonErrorMessages = FXCollections.observableArrayList();
        ListView<String> listView4 = new ListView<String>(NonErrorMessages);

        //list of graphs
        ObservableList<String> graphs = FXCollections.observableArrayList();
        ListView<String> listView1 = new ListView<String>(graphs);


        Button addGraph = new Button("New Graph");
        addGraph.setPrefWidth(100);
        TextField inputField = new TextField("graph");
        inputField.setPrefWidth(75);

        HBox entryBox = new HBox();
        entryBox.setPrefWidth(75);
        entryBox.getChildren().addAll(inputField, addGraph);

        addGraph.setOnAction(e -> {
            if (Graphs.containsKey(inputField.getText())) {
                ErrorMessages.add("A graph with the name " + inputField.getText() + " already exists");}
            else {
                Graphs.put(inputField.getText(), new Graph(inputField.getText()));
                graphs.add(inputField.getText());
                NonErrorMessages.add("The new graph " + inputField.getText() + " was succesfully instantiated");
            };
            inputField.setText("graph");
            inputField.requestFocus();
        });
        addGraph.disableProperty().bind(Bindings.isEmpty(inputField.textProperty()));

        VBox vbox = new VBox();
        vbox.setPrefWidth(175);
        vbox.getChildren().addAll(new Label("Graphs"), listView1, entryBox);

        //list of edges
        ObservableList<String> edges = FXCollections.observableArrayList();
        ListView<String> listView2 = new ListView<String>(edges);

        Button addEdge = new Button("New Edge");
        addEdge.setPrefWidth(100);
        TextField inputField2 = new TextField("vertex1");
        inputField2.setPrefWidth(75);
        TextField inputField9 = new TextField("vertex2");
        inputField9.setPrefWidth(75);
        TextField inputField10 = new TextField("graph");
        inputField10.setPrefWidth(75);

        addEdge.setOnAction(e -> {
            //if the graph does not exist
            if (!Graphs.containsKey(inputField10.getText())) {
                ErrorMessages.add("There is no graph with the name " + inputField10.getText());

            } else if (inputField2.getText().equals(inputField9.getText())) {
                ErrorMessages.add("An edge cannot be made from one vertex to itself");

            } else if (Graphs.containsKey(inputField10.getText()) && Graphs.get(inputField10.getText()).edgeCheck(inputField2.getText(), inputField9.getText())) {
                ErrorMessages.add("An edge between vertices " + inputField2.getText() + " and " + inputField9.getText() + " already exists in the graph " + inputField10.getText());
            //if the graph does exist and the vertexs are not the same
            } else {
                //if the graph does exist and both vertices exist
                if
                (!Graphs.get(inputField10.getText()).edgeCheck(inputField2.getText(), inputField9.getText()) && Graphs.get(inputField10.getText()).vertCheck(inputField2.getText()) && Graphs.get(inputField10.getText()).vertCheck(inputField9.getText())) {
                    Graphs.get(inputField10.getText()).newEdge(inputField2.getText(), inputField9.getText());
                    edges.add("(" + inputField2.getText() + " , " + inputField9.getText()+ ") in graph " + inputField10.getText());
                    NonErrorMessages.add("The new edge from " + inputField2.getText() + " to " + inputField9.getText() + " was succesfully instantiated in the graph " + inputField10.getText());
                } else {
                    //if the graph does exist but the first vertex does not exist
                    if (!Graphs.get(inputField10.getText()).vertCheck(inputField2.getText()) && Graphs.get(inputField10.getText()).vertCheck(inputField9.getText())) {
                        Graphs.get(inputField10.getText()).newVertex(inputField2.getText());
                        Graphs.get(inputField10.getText()).newEdge(inputField2.getText(), inputField9.getText());
                        edges.add("(" + inputField2.getText() + ", " + inputField9.getText() + ") in graph " + inputField10.getText());
                        vertexes.add(inputField2.getText() + " in graph " +  inputField10.getText());
                        NonErrorMessages.add("A new vertex " + inputField2.getText() + " was created because it did not already exist in the graph " + inputField10.getText());
                        NonErrorMessages.add("The new edge from " + inputField2.getText() + " to " + inputField9.getText() + " was succesfully instantiated in the graph " + inputField10.getText());
                    //if the graph does exist but the second vertex does not exist
                    } else if
                    (!Graphs.get(inputField10.getText()).vertCheck(inputField9.getText()) && Graphs.get(inputField10.getText()).vertCheck(inputField2.getText())) {
                        Graphs.get(inputField10.getText()).newVertex(inputField9.getText());
                        Graphs.get(inputField10.getText()).newEdge(inputField2.getText(), inputField9.getText());
                        edges.add("(" + inputField2.getText() + ", "  + inputField9.getText() + ") in graph " + inputField10.getText());
                        vertexes.add(inputField9.getText() + " in graph " +  inputField10.getText());
                        NonErrorMessages.add("A new vertex " + inputField9.getText() + " was created because it did not already exist in the graph " + inputField10.getText());
                        NonErrorMessages.add("The new edge from " + inputField2.getText() + " to " + inputField9.getText() + " was succesfully instantiated in the graph " + inputField10.getText());
                    //if the graph does exist but neither vertex exists
                    } else {
                        Graphs.get(inputField10.getText()).newVertex(inputField2.getText());
                        Graphs.get(inputField10.getText()).newVertex(inputField9.getText());
                        Graphs.get(inputField10.getText()).newEdge(inputField2.getText(), inputField9.getText());
                        edges.add("(" + inputField2.getText() + ", " + inputField9.getText()+ ") in graph " + inputField10.getText());
                        vertexes.add(inputField2.getText() + " in graph " +  inputField10.getText());
                        NonErrorMessages.add("A new vertex " + inputField2.getText() + " was created because it did not already exist in the graph " + inputField10.getText());
                        vertexes.add(inputField9.getText() + " in graph " +  inputField10.getText());
                        NonErrorMessages.add("A new vertex " + inputField9.getText() + " was created because it did not already exist in the graph " + inputField10.getText());
                        NonErrorMessages.add("The new edge from " + inputField2.getText() + " to " + inputField9.getText() + " was succesfully instantiated in the graph " + inputField10.getText());
                    }
                }
            };
            inputField2.setText("vertex1");
            inputField2.requestFocus();
            inputField9.setText("vertex2");
            inputField9.requestFocus();
            inputField10.setText("graph");
            inputField10.requestFocus();});

/////////////////////
        addEdge.disableProperty().bind(Bindings.isEmpty(inputField2.textProperty()));
/////////////////////

        HBox entryBox2 = new HBox();
        entryBox2.getChildren().addAll(inputField2, inputField9, inputField10,  addEdge);

        VBox vbox2 = new VBox();
        vbox2.getChildren().addAll(new Label("Edges"), listView2, entryBox2);

        //list of vertices
        ListView<String> listView5 = new ListView<String>(vertexes);
///
        Button addVertexNew = new Button("New Vertex");
        addVertexNew.setPrefWidth(100);
        TextField inputField3 = new TextField("vertex");
        inputField3.setPrefWidth(80);
        TextField inputField8 = new TextField("graph");
        inputField8.setPrefWidth(80);

        addVertexNew.setOnAction(e -> {
            if (Graphs.containsKey(inputField8.getText())) {
                if (!Graphs.get(inputField8.getText()).vertCheck(inputField3.getText())){
                    Graphs.get(inputField8.getText()).newVertex(inputField3.getText());
                    vertexes.add(inputField3.getText() + " in graph " +  inputField8.getText());
                    NonErrorMessages.add("The vertex " + inputField3.getText() + " was succesfully instantiated in the graph " + inputField8.getText());
                } else {
                    ErrorMessages.add("A vertex with the name " + inputField3.getText() + " already exists in the graph " + inputField8.getText());
                };}
            else {

                ErrorMessages.add("There is no graph with the name " + inputField8.getText() + " so the vertex " + inputField3.getText() + " could not be created");
            };
            inputField3.setText("vertex");
            inputField3.requestFocus();
            inputField8.setText("graph");
            inputField8.requestFocus();});

//        addVertexNew.disableProperty().bind(Bindings.isEmpty(inputField3.textProperty()));
//        addVertexNew.disableProperty().bind(Bindings.isEmpty(inputField8.textProperty()));

        HBox entryBox3 = new HBox();
        entryBox3.getChildren().addAll(inputField3, inputField8, addVertexNew);

        VBox vbox5 = new VBox();
        vbox5.getChildren().addAll(new Label("Vertices"), listView5, entryBox3);

        Button fetchDegree = new Button("get Degree");
        fetchDegree.setPrefWidth(100);
        TextField inputField7 = new TextField("vertex");
        inputField7.setPrefWidth(75);
        TextField inputField6 = new TextField("graph");
        inputField6.setPrefWidth(75);

        fetchDegree.setOnAction(e -> {
            if (!Graphs.containsKey(inputField6.getText())) {
                ErrorMessages.add("The graph " + inputField6.getText() + " does not exist so a degree for a vertex in the graph cannot be found");
            } else if (Graphs.containsKey(inputField6.getText()) && !Graphs.get(inputField6.getText()).vertCheck(inputField7.getText())) {
                ErrorMessages.add("There is no vertex with the name " + inputField7.getText() + " in the graph " + inputField6.getText());
            } else if (Graphs.containsKey(inputField6.getText()) && Graphs.get(inputField6.getText()).vertCheck(inputField7.getText())) {
                RequestedInfo.add("The vertex " + inputField7.getText() + " in graph " + inputField6.getText() + " has degree " +Graphs.get(inputField6.getText()).getDegreeGraphVersion(inputField7.getText()));
                NonErrorMessages.add("The degree for vertex " + inputField7.getText() + " in graph " + inputField6.getText() + " was succesfully found");};
            inputField7.setText("vertex");
            inputField7.requestFocus();
            inputField6.setText("graph");
            inputField6.requestFocus();});

        HBox degreeGetter = new HBox();
        degreeGetter.getChildren().addAll(inputField7, inputField6, fetchDegree);

        //degreeSequence
        Button fetchDegreeSequence = new Button("get Degree Sequence");
        fetchDegreeSequence.setPrefWidth(160);
        TextField inputField11 = new TextField("graph");
        inputField11.setPrefWidth(75);

        fetchDegreeSequence.setOnAction(e -> {
            if (!Graphs.containsKey(inputField11.getText())) {
                ErrorMessages.add("The graph " + inputField11.getText() + " does not exist so a degree sequence cannot be found");
            } else if (Graphs.get(inputField11.getText()).Vertices.size() == 0) {
                RequestedInfo.add("The graph " + inputField11.getText() + " has no vertices so its degree sequence is empty or {∅}");
            } else {
                List<Integer> degSeq = Graphs.get(inputField11.getText()).getDegreeSequence();
                String tempString = "The graph " + inputField11.getText() + " has degree sequence: ";
                for (int i = 0; i < degSeq.size(); i++) {
                    tempString += (degSeq.get(i) + " ");
                }
                RequestedInfo.add(tempString);
                NonErrorMessages.add("The degree sequence for the graph " + inputField11.getText() + " was succesfully found");
            };
            inputField11.setText("graph");
            inputField11.requestFocus();});

        HBox degreeSequenceGetter = new HBox();
        degreeSequenceGetter.getChildren().addAll(inputField11, fetchDegreeSequence);

        //list of vertices for graph
        Button fetchVertexSetOfGraph = new Button("get Vertex Set");
        fetchVertexSetOfGraph.setPrefWidth(140);
        TextField inputField12 = new TextField("graph");
        inputField12.setPrefWidth(75);

        fetchVertexSetOfGraph.setOnAction(e -> {
            if (!Graphs.containsKey(inputField12.getText())) {
                ErrorMessages.add("The graph " + inputField12.getText() + " does not exist so a vertex set cannot be found");
            } else if (Graphs.get(inputField12.getText()).Vertices.size() == 0) {
                RequestedInfo.add("The graph " + inputField12.getText() + " has no vertices so its vertex set is empty or {∅}");
            } else {
                ArrayList<String> VertSet = Graphs.get(inputField12.getText()).getVertices();
                String tempString = "The graph " + inputField12.getText() + " has vertex set: ";
                for (int i = 0; i < VertSet.size(); i++) {
                    tempString += (VertSet.get(i) + " ");
                }
                RequestedInfo.add(tempString);
                NonErrorMessages.add("The vertex set for the graph " + inputField12.getText() + " was succesfully found");
            };
            inputField12.setText("graph");
            inputField12.requestFocus();});

        HBox VertexSetGetter = new HBox();
        VertexSetGetter.getChildren().addAll(inputField12, fetchVertexSetOfGraph);

        //edge set getter
        Button fetchEdgeSetOfGraph = new Button("get Edge Set");
        fetchEdgeSetOfGraph.setPrefWidth(140);
        TextField inputField13 = new TextField("graph");
        inputField13.setPrefWidth(75);

        fetchEdgeSetOfGraph.setOnAction(e -> {
            if (!Graphs.containsKey(inputField13.getText())) {
                ErrorMessages.add("The graph " + inputField13.getText() + " does not exist so an edge set cannot be found");
            } else if (Graphs.get(inputField13.getText()).Edges.size() == 0) {
                RequestedInfo.add("The graph " + inputField13.getText() + " has no edges so its edge set is empty or {∅}");
            } else {
                ArrayList<String> EdgSet = Graphs.get(inputField13.getText()).getEdges();
                String tempString = "The graph " + inputField13.getText() + " has edge set: ";
                for (int i = 0; i < EdgSet.size(); i++) {
                    tempString += (EdgSet.get(i) + " ");
                }
                RequestedInfo.add(tempString);
                NonErrorMessages.add("The edge set for the graph " + inputField13.getText() + " was succesfully found");
            };
            inputField13.setText("graph");
            inputField13.requestFocus();});

        //Is Connected
        Button fetchIsConnected = new Button("Is Connected");
        fetchIsConnected.setPrefWidth(160);
        TextField inputField16 = new TextField("graph");
        inputField16.setPrefWidth(75);

        fetchIsConnected.setOnAction(e -> {
            if (!Graphs.containsKey(inputField16.getText())) {
                ErrorMessages.add("The graph " + inputField16.getText() + " does not exist so its connectivity cannot be found");
            } else if (Graphs.get(inputField16.getText()).Vertices.size() == 0) {
                RequestedInfo.add("The graph " + inputField16.getText() + " has no vertices so its connectivity does not exist");
            } else {
                boolean isCon = Graphs.get(inputField16.getText()).isConnected();
                String booCon;
                if (isCon) {
                    booCon = " is connected";
                } else {
                    booCon = " is not connected";
                }
                String tempString = ("The graph " + inputField16.getText() + booCon);
                RequestedInfo.add(tempString);
                NonErrorMessages.add("The connectivity of the graph " + inputField16.getText() + " was succesfully found");
            };
            inputField16.setText("graph");
            inputField16.requestFocus();});

        HBox connectivityGetter = new HBox();
        connectivityGetter.getChildren().addAll(inputField16, fetchIsConnected);

        //degreeSequence
        Button fetchNeighborhood = new Button("get Neighborhood");
        fetchDegreeSequence.setPrefWidth(160);
        TextField inputField14 = new TextField("vertex");
        inputField14.setPrefWidth(75);
        TextField inputField15 = new TextField("graph");
        inputField15.setPrefWidth(75);

        fetchNeighborhood.setOnAction(e -> {
            //if the graph does not exist
            if (!Graphs.containsKey(inputField15.getText())) {
                ErrorMessages.add("The graph " + inputField15.getText() + " does not exist so a neighborhood cannot be found");
            //if the graph exists but the vertex does not
            } else if (!Graphs.get(inputField15.getText()).vertCheck(inputField14.getText())) {
                ErrorMessages.add("There is no vertex with name " + inputField14.getText() + " in the graph " + inputField15.getText());
            //if the graph does exist and the vertex does exist and the vertex has no neighbors/edges
        } else if (Graphs.get(inputField15.getText()).Vertices.get(inputField14.getText()).neighborhood.size() == 0) {
                RequestedInfo.add("The vertex " + inputField14.getText() + " has no neighbors so its neighborhood is empty or {∅}");
            //if the graph and vertex exist and the vertex does have edges
            } else {
                List<String> hood = Graphs.get(inputField15.getText()).Vertices.get(inputField14.getText()).getNeighborhood();
                String tempString = "The vertex " + inputField14.getText() + " in the graph " + inputField15.getText() + " has neighborhood: ";
                for (int i = 0; i < hood.size(); i++) {
                    tempString += (hood.get(i) + " ");
                }
                RequestedInfo.add(tempString);
                NonErrorMessages.add("The neighborhood for the vertex " + inputField14.getText() + " in the graph " + inputField15.getText() + " was succesfully found");
            };
            inputField14.setText("vertex");
            inputField14.requestFocus();
            inputField15.setText("graph");
            inputField15.requestFocus();});

        HBox NeighborhoodGetter = new HBox();
        NeighborhoodGetter.getChildren().addAll(inputField14, inputField15, fetchNeighborhood);

        HBox EdgeSetGetter = new HBox();
        EdgeSetGetter.getChildren().addAll(inputField13, fetchEdgeSetOfGraph);

        VBox degreeInfoGetters = new VBox();
        degreeInfoGetters.getChildren().addAll(degreeGetter, degreeSequenceGetter, connectivityGetter);

        VBox componentInfoGetters = new VBox();
        componentInfoGetters.getChildren().addAll(VertexSetGetter, EdgeSetGetter, NeighborhoodGetter);

        VBox displayWindowInfo = new VBox();
        displayWindowInfo.setPrefWidth(500);
        displayWindowInfo.setPrefHeight(220);
        displayWindowInfo.getChildren().addAll(new Label("Requested Info"), listView6);

        HBox info = new HBox();
        info.setPrefWidth(250);
        info.getChildren().addAll(degreeInfoGetters, new Label("  "), componentInfoGetters, new Label("  "), displayWindowInfo);


        //Error Messages Box
        VBox vbox3 = new VBox();
        vbox3.setPrefWidth(525);
        vbox3.setPrefHeight(222);
        vbox3.getChildren().addAll(new Label("Error Messages"), listView3);

        //Non Error Messages Box
        VBox vbox4 = new VBox();
        vbox4.setPrefWidth(525);
        vbox4.setPrefHeight(222);
        vbox4.getChildren().addAll(new Label("Non Error Messages"), listView4);

        VBox messages = new VBox();
        messages.setPrefWidth(525);
        messages.getChildren().addAll(vbox3, vbox4);

        //sets up the full scene
        HBox creators = new HBox();
        creators.getChildren().addAll(vbox, new Label("  "), vbox2, new Label("  "), vbox5, new Label("  "), messages);

        VBox fullScene = new VBox();
        fullScene.getChildren().addAll(new Label("Constructors"), creators, new Label("  "), new Label("Info"), info);

        //makes stage
        Scene scene = new Scene(fullScene);
        stage.setScene(scene);
        stage.setTitle("Graphs");
        stage.show();
    }
}
