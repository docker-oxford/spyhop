$(function () {

    var RELOAD = 25000, TIMEOUT = 5000, SHIFT = 20, PERCISION = 2;

    var SERIES = {};

    var table = $('#containers').DataTable({
	"ajax": "/api/ps",
	"columns": [
	    { "title": "Container ID", "data": "Id" },
	    { "title": "Image", "data": "Image" },
	    { "title": "Command", "data": "Command" },
	    { "title": "Created", "data": "Created" },
	    { "title": "Status", "data": "Status" },
	    { "title": "Ports", "data": "Ports[0].PublicPort" },
	    { "title": "Names", "data": "Names" }
	],
	"fnInitComplete": function (settings) {

	    if (settings.json) {
		for (var i = 0; i < settings.json.data.length; i++) {

		    var hash = settings.json.data[i].Id;

		    SERIES[hash] = chart.addSeries({
			name: settings.json.data[i].Names,
		    });

		}
		cpuPercent();
	    }
	},

	"fnDrawCallback": function(settings) {

	    if (settings.json) {

		for (var i = 0; i < settings.json.data.length; i++) {
		    console.log(settings.json.data[i].Id);
		}
	    }
	}
    });


    setInterval(function () {
	table.ajax.reload(null, false);
    }, RELOAD);


    function cpuPercent() {

	for (var containerId in SERIES) {

	    $.getJSON('/api/curated/' + containerId, function (data) {

		console.log('calling /api/curated/' + containerId);

		var series = SERIES[containerId], shift = series.data.length > SHIFT;
		series.addPoint(parseFloat(data.cpu_percent.toFixed(PERCISION)), true, shift);
		setTimeout(cpuPercent, TIMEOUT);

	    });
	}
    }

    var chart = new Highcharts.Chart({

	chart: {
	    renderTo: 'charts',
	},

	credits: {
	    enabled: false,
	},

	title: {
	    text : 'CPU %'
	},

	exporting: {
	    enabled: false
	},

    });


});
