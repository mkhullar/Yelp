/**
 * Created by mayankkhullar on 6/28/17.
 */
$(function()  {
    var chart = new CanvasJS.Chart("chartContainer",
        {
            title: {
                text: "CheckIn vs Day"
            },
            animationEnabled: true,
            axisY: {
                title: "Check In"
            },
            axisX: {
                title: "Days"
            },
            legend: {
                verticalAlign: "bottom",
                horizontalAlign: "center"
            },
            theme: "theme2",
            data: [

                {
                    type: "column",
                    showInLegend: false,
                    legendMarkerColor: "grey",
                    legendText: "MMbbl = one million barrels",
                    dataPoints: getCheckTime()
                }
            ]
        });
    chart.render();
});