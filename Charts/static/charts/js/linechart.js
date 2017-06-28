/**
 * Created by mayankkhullar on 6/28/17.
 */
$(function() {

    $('#line-container').highcharts({

        title: {
            text: 'Growth of Yelp '
        },

        yAxis: {
            title: {
                text: 'Number of Tips'
            }
        },
        legend: {
            layout: 'vertical',
            align: 'right',
            verticalAlign: 'middle'
        },

        plotOptions: {
            series: {
                pointStart: 2009
            }
        },

        series: [{
            name: 'Tips',
            data: yelpTip()
        }]

    });
});