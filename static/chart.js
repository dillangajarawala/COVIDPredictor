var barOptions_stacked = {
    tooltips: {
        enabled: false
    },
    hover :{
        animationDuration:0
    },
    scales: {
        xAxes: [{
            ticks: {
                beginAtZero:true,
                fontFamily: "'Open Sans Bold', sans-serif",
                fontSize:11,
                fontColor: "#fff"
            },
            scaleLabel:{
                display:true
            },
            gridLines: {
            }, 
            stacked: true
        }],
        yAxes: [{
            gridLines: {
                display:false,
                color: "#fff",
                zeroLineColor: "#fff",
                zeroLineWidth: 0
            },
            ticks: {
                fontFamily: "'Open Sans Bold', sans-serif",
                fontSize:11,
                fontColor: "#fff"
            },
            stacked: true
        }]
    },
    legend:{
        display:true,
        labels: {
            fontColor: "#fff"
        }
    },
    maintainAspectRatio: false,
    responsive: true,
    
    animation: {
        onComplete: function () {
            var chartInstance = this.chart;
            var ctx = chartInstance.ctx;
            ctx.textAlign = "center";
            ctx.font = "15px 'Open Sans Bold', sans-serif";
            ctx.fillStyle = "#fff";
        }
    },
    pointLabelFontFamily : "Quadon Extra Bold",
    scaleFontFamily : "Quadon Extra Bold",
};


function createCasesChart(weights, labels) {
var ctx = document.getElementById("Chart");
var myChart = new Chart(ctx, {
    type: 'horizontalBar',
    data: {
        labels: ["Cases"],
        
        datasets: [{
            data: [weights[0]],
            label: labels[0] + ": " + String(weights[0]),
            backgroundColor: "#66CDAA"
        },{
            data: [weights[1]],
            label: labels[1] + ": " + String(weights[1]),
            backgroundColor: "#00FF7F"
        },{
            data: [weights[2]],
            label: labels[2] + ": " + String(weights[2]),
            backgroundColor: "#7CFC00"
        },{
            data: [weights[3]],
            label: labels[3] + ": " + String(weights[3]),
            backgroundColor: "#FFFF00"
        },{
            data: [weights[4]],
            label: labels[4] + ": " + String(weights[4]),
            backgroundColor: "#DAA520"
        },{
            data: [weights[5]],
            label: labels[5] + ": " + String(weights[5]),
            backgroundColor: "#FF8C00"
        },{
            data: [weights[6]],
            label: labels[6] + ": " + String(weights[6]),
            backgroundColor: "#FF0000"
        },{
            data: [weights[7]],
            label: labels[7] + ": " + String(weights[7]),
            backgroundColor: "#800000"
        }]
    },

    options: barOptions_stacked
});
}

function createDeathsChart(weights, labels) {
    var ctx = document.getElementById("Chart");
    var myChart = new Chart(ctx, {
        type: 'horizontalBar',
        data: {
            labels: ["Deaths"],
            
            datasets: [{
                data: [weights[0]],
                label: labels[0] + ": " + String(weights[0]),
                backgroundColor: "#2D69DA"
            },{
                data: [weights[1]],
                label: labels[1] + ": " + String(weights[1]),
                backgroundColor: "#66CDAA"
            },{
                data: [weights[2]],
                label: labels[2] + ": " + String(weights[2]),
                backgroundColor: "#00FF7F"
            },{
                data: [weights[3]],
                label: labels[3] + ": " + String(weights[3]),
                backgroundColor: "#7CFC00"
            },{
                data: [weights[4]],
                label: labels[4] + ": " + String(weights[4]),
                backgroundColor: "#FFFF00"
            },{
                data: [weights[5]],
                label: labels[5] + ": " + String(weights[5]),
                backgroundColor: "#DAA520"
            },{
                data: [weights[6]],
                label: labels[6] + ": " + String(weights[6]),
                backgroundColor: "#FF8C00"
            },{
                data: [weights[7]],
                label: labels[7] + ": " + String(weights[7]),
                backgroundColor: "#FF0000"
            },{
                data: [weights[8]],
                label: labels[8] + ": " + String(weights[8]),
                backgroundColor: "#800000"
            }]
        },
    
        options: barOptions_stacked
    });
    }