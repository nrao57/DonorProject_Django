
function Network() {
    //generate chart

    var width = 960;
    var height = 800;

    function network(selection, data){
     //main implementation
    }

    function update(){
	//private function
	//The update() function performs the bulk of the
        //work to setup our visualization based on the
        //current layout/sort/filter.

	//update() is called everytime a parameter changes
	//and the network needs to be reset.

	//filter data to show based on current filter settings
	curNodesData = filterNodes(allData.nodes);
	curLinksData = filterLinks(allData.links, curNodesData);

	//reset nodes in force layout
	force.nodes(curNodesData);
	//enter / exit for nodes
	updateNodes();

	//always show links in force layout
	force.links(curLinksData);
	updateLinks();


	//start me up!
	force.start();	
    }

    //enter/exit display for nodes
    function updateNodes(){
	node = nodesG.selectAll("circle.node");
	    .data(curNodesData, (d) -> d.id);
 
	node.enter().append("circle");
	    .attr("class", "node");
	    .attr("cx", (d) -> d.x);
	    .attr("cy", (d) -> d.y);
	    .attr("r", (d) -> d.radius);
	    .style("fill", (d) -> nodeColors(d.artist));
	    .style("stroke", (d) -> strokeFor(d));
	    .style("stroke-width", 1.0);
 
	node.on("mouseover", showDetails);
	    .on("mouseout", hideDetails);
 
	node.exit().remove();
    }

    //enter/exit display for links
    function updateLinks(){
	link = linksG.selectAll("line.link")
	    .data(curLinksData, (d) -> "#{d.source.id}_#{d.target.id}")
	link.enter().append("line")
	    .attr("class", "link")
	    .attr("stroke", "#ddd")
	    .attr("stroke-opacity", 0.8)
	    .attr("x1", (d) -> d.source.x)
	    .attr("y1", (d) -> d.source.y)
	    .attr("x2", (d) -> d.target.x)
	    .attr("y2", (d) -> d.target.y)
 
	link.exit().remove()
    }
    
    
    
}
