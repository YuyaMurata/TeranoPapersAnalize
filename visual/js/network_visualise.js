function onButtonClick() {
	jsonData = document.forms.id_form1.graph_select.value;
	label_size = document.forms.id_form1.label_size.value;
	
	d3.selectAll("svg > g").remove()
	var sizeScale = d3.scaleLinear().domain([1, 320]).range([5, 40]);
	
	var svg = d3.select("svg"),
    	width = +svg.attr("width"),
    	height = +svg.attr("height"),
    	radius = 5,
    	transform = d3.zoomIdentity;
	
	var color = d3.scaleOrdinal(d3.schemeCategory20);
	
	var g = svg.append("g");
	
	if(jsonData.indexOf('undirect') == -1)
		_setArrow(g);

	var simulation = d3.forceSimulation()
		.force("link", d3.forceLink().id(function(d) { return d.id; }))
		.force("charge", d3.forceManyBody())
		.force("center", d3.forceCenter(width / 2, height / 2));
		
	
	//d3.json("data_graph.json", function(error, graph) {
	//	if (error) throw error;
	
	console.log(jsonData)
	console.log(label_size)

	oboe(jsonData).node('*', function(graph) {
		
		//console.log(graph)
		
		var link = g.append("g")
			.attr("class", "links")
			.selectAll(".link")
			.data(graph.links)
			.enter().append("line")
				.attr("class", "link")
				.attr("stroke-width", function(d) { return Math.sqrt(d.value); })
				.attr("marker-end", "url(#arrow)");

		var node = g.append("g")
			.attr("class", "nodes")
			.selectAll(".node")
			.data(graph.nodes)
			.enter().append("circle")
				.attr("r", function(d){return sizeScale(d.size);})
				.attr("fill", function(d) { return color(d.group); })
				.call(d3.drag()
					.subject(dragsubject)
					.on("start", dragstarted)
					.on("drag", dragged)
					.on("end", dragended));
				
		var label = g.append("g")
			.attr("class", "labels")
			.selectAll(".label")
				.data(graph.nodes)
				.enter()
				.append("text")
				.text(function (d) { return d.label; })
					.style("text-anchor", "middle")
					.style("fill", "#555")
					.style("font-family", "Arial")
					.style("font-size", label_size);

		simulation
			.nodes(graph.nodes)
			.on("tick", ticked);

		simulation.force("link")
			.links(graph.links);

		function ticked() {
			link
				.attr("x1", function(d) { return d.source.x; })
				.attr("y1", function(d) { return d.source.y; })
				.attr("x2", function(d) { return d.target.x; })
				.attr("y2", function(d) { return d.target.y; });

			node
				.attr("cx", function(d) { return d.x; })
				.attr("cy", function(d) { return d.y; });
		
			label
				.attr("x", function(d){ return d.x; })
    			.attr("y", function (d) {return d.y - 8; });
		}
		
		function dragsubject() {
			return simulation.find(d3.event.x, d3.event.y, radius);
		}
	});
	
	svg.call(d3.zoom()
		.scaleExtent([1/8, 10])
		.on("zoom", zoomed));
	
	//Zoom Event
	function zoomed() {
		g.attr("transform", d3.event.transform);
	}
	
	//Drag Event
	function dragstarted() {
		if (!d3.event.active) simulation.alphaTarget(0.3).restart();
		d3.event.subject.fx = d3.event.subject.x;
		d3.event.subject.fy = d3.event.subject.y;
	}

	function dragged() {
		d3.event.subject.fx = d3.event.x;
		d3.event.subject.fy = d3.event.y;
	}

	function dragended() {
		if (!d3.event.active) simulation.alphaTarget(0);
		d3.event.subject.fx = null;
		d3.event.subject.fy = null;
	}
	
	function _setArrow(svg)
	{
    svg.append('defs').selectAll('marker')
       .data(['arrow']).enter()
       .append('marker')
       .attr('id', function(d) { return d; })
       .attr('viewBox', '0 -5 10 10')
       .attr('refX', 15)
       .attr('refY', -1.5)
       .attr('markerWidth', 6)
       .attr('markerHeight', 6)
       .attr('orient', 'auto')
       .append('path')
       .attr("d", "M0,-5L10,0L0,5")
       .style('stroke', '#666')
       .style('opacity', '0.6');
	};
	
}
