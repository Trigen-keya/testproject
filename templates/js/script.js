// var pieData = {
//     labels: ['Webデザイナー', 'Webデベロッパー', 'サーバーエンジニア', '営業職'],
//     series: [14, 9, 8, 6]
// };

// var pieOptions = {
//     width: '100%',
//     height: '440px'
// };

// new Chartist.Pie('.pie-chart', pieData, pieOptions);

var ctx = document.getElementById('myChart');
var myDoughnutChart = new Chart(ctx, {
    type: 'doughnut',
    data: {
        labels: ["CompanyA", "CompanyB", "CompanyC","CompanyD","CompanyE","CompanyF","CompanyG","CompanyH","CompanyI"],
        datasets: [
          {
            data: [300, 100, 80, 100, 30, 12, 34, 91, 200],
            backgroundColor: ["#f66", "#c7e", "#fc2", "#f66", "#c7e", "#fc2","#f66", "#c7e", "#fc2"]
          }
        ]
      }
});