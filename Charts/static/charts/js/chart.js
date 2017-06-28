/**
 * Created by mayankkhullar on 6/28/17.
 */
$(function() {

    $('#container').highcharts({
        
        chart: {
            type: 'heatmap',
            marginTop: 40,
            marginBottom: 40
        },


        title: {
            text: 'Stars vs Cities'
        },

        xAxis: {
            categories: ['Edinburgh','Montreal','Pittsburgh','Charlotte','Urbana-Champaign','Phoenix','Las_Vegas','Madison','Cleveland']
        },

        yAxis: {
            categories: ['1', '2', '3', '4', '5'],
            title: "Stars"
        },

        colorAxis: {
            min: 0,
            minColor: '#FFFFFF',
            maxColor: Highcharts.getOptions().colors[0]
        },

        legend: {
            align: 'left',
            layout: 'vertical',
            margin: 0,
            verticalAlign: 'top',
            y: 25,
            symbolHeight: 320
        },

        tooltip: {
            formatter: function () {
                return '<b>' + this.series.xAxis.categories[this.point.x] + '</b> had <br><b>' +
                    this.point.value + ' reviews of '+ this.series.yAxis.categories[this.point.y] + '</b> stars <br><b>' +'</b>';
            }
        },

        series: [{
            name: '',
            borderWidth: 1,
            data: getStars(),
            dataLabels: {
                enabled: true,
                color: 'black',
                style: {
                    textShadow: 'none'
                }
            }
        }]

    });
});