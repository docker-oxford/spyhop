$(function () {

    var TIMEOUT = 1000, SHIFT = 20;

    $('#containers').dataTable({
	"ajax": "/data/containers.json",
	"columns": [
	    { "title": "Container ID", "data": "container-id" },
	    { "title": "Image", "data": "image" },
	    { "title": "Command", "data": "command" },
	    { "title": "Created", "data": "created" },
	    { "title": "Status", "data": "status" },
	    { "title": "Ports", "data": "ports" },
	    { "title": "Names", "data": "names" }
	]
    });

    function rx_bytes() {

	$.getJSON('/data/stats.json', function (data) {

	    var series = chart.series[0], shift = series.data.length > SHIFT;
	    chart.series[0].addPoint(data.network.rx_bytes, true, shift);
	    setTimeout(rx_bytes, TIMEOUT);

	});

    }

    var chart = new Highcharts.Chart({

	chart: {
	    renderTo: 'charts',
	    events: {
		load: rx_bytes
	    }
	},

	credits: {
	    enabled: false,
	},

	title: {
	    text : 'Network Traffic'
	},

	exporting: {
	    enabled: false
	},

	series: [{
	    name: 'Random data',
	    data: []
	}]

    });

});
