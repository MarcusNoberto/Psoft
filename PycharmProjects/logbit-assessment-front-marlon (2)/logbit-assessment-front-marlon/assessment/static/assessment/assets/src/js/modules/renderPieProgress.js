export default function renderPieProgress(percent) {
    const svgPaths = document.querySelectorAll('[js-progress-bar]')
    const progressValue = document.querySelector('[js-progress-value]')

    // Remove as cores de todos svgs
    svgPaths.forEach(svg => svg.style.clipPath = 'inset(0 100% 0 0)')

    if (percent < 33.33) {
        const percentageValue = 100 - ((percent / 33) * 100)
        svgPaths[0].style.clipPath = `inset(0 ${percentageValue}% 0 0)`
    }
    
    if (percent >= 33.33) {
        svgPaths[0].style.clipPath = 'inset(0 0 0 0)'

        const percentageValue = 100 - (((percent - 33) / 33) * 100)
        svgPaths[1].style.clipPath = `inset(0 ${percentageValue}% 0 0)`
    }

    if (percent >= 66.66) {
        svgPaths[0].style.clipPath = 'inset(0 0 0 0)'
        svgPaths[1].style.clipPath = 'inset(0 0 0 0)'

        const percentageValue = 100 - (((percent - 66) / 33) * 100)
        svgPaths[2].style.clipPath = `inset(0 ${percentageValue}% 0 0)`
    }

    progressValue.innerHTML = `${percent}%`
}