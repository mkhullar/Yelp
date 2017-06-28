/**
 * Created by mayankkhullar on 6/28/17.
 */
$(function() {

    $('#funnel-container').highcharts({
    chart: {
        type: 'funnel'
    },
    title: {
        text: 'Yelp Usage'
    },
    plotOptions: {
        series: {
            dataLabels: {
                enabled: true,
                format: '<b>{point.name}</b> ({point.y:,.0f})',
                color: (Highcharts.theme && Highcharts.theme.contrastTextColor) || 'black',
                softConnector: true
            },
            center: ['40%', '50%'],
            neckWidth: '30%',
            neckHeight: '25%',
            width: '80%'
        }
    },
    legend: {
        enabled: true
    },
    series: [{
        name: 'Unique users',
        data: yelpTip()
    }]
});
});