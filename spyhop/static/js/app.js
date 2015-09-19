$(function () {

    var TIMEOUT = 1000, SHIFT = 20;

    $('#containers').dataTable({
	"ajax": "/api/ps",
	"columns": [
	    { "title": "Container ID", "data": "Id" },
	    { "title": "Image", "data": "Image" },
	    { "title": "Command", "data": "Command" },
	    { "title": "Created", "data": "Created" },
	    { "title": "Status", "data": "Status" },
	    { "title": "Ports", "data": "Ports[0].PublicPort" },
	    { "title": "Names", "data": "Names" }
	]
    });

    function rx_bytes() {

	$.getJSON('/api/db72a8931dcd', function (data) {

	    var series = chart.series[0], shift = series.data.length > SHIFT;
	    chart.series[0].addPoint(data.cpu_stats.cpu_usage.total_usage, true, shift);
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
