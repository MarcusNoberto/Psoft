export default function initLineChart(element, config) {
    const chartConfig = {
        chart: {
            width: '100%',
            height: '100%',
            type: 'line',
            toolbar: {
                show: false,
            },
            zoom: {
                enabled: false
            }
        },
        dataLabels: {
            enabled: false,
        },
        colors: ['#F40000', '#E5813E', '#D7B85B', '#FF560E', '#F79900', '#B59E74'],
        stroke: {
            width: 2,
            curve: 'smooth',
            color: '#F0F0F0'
        },
        grid: {
            row: {
                opacity: 0.5
            },
            xaxis: {
                lines: {
                    show: true
                }
            },
            yaxis: {
                lines: {
                    show: true
                }
            }
        },
        markers: {
            size: 5,
        },
        yaxis: {
            labels: {
                formatter: function (val) {
                    return val + "%"
                },
            }
        },
        ...config
    }

    const chartEl = new ApexCharts(document.querySelector(element), chartConfig)

    setTimeout(() => chartEl.render(), 200)
}