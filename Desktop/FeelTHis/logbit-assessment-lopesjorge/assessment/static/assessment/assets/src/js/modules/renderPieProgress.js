export default function renderPieProgress(percent, bronze, prata, ouro) {
    const svgPaths = document.querySelectorAll('[js-progress-bar]')
    const progressValue = document.querySelector('[js-progress-value]')

    const bronzePercent = Number(bronze.replace(',', '.'))
    const silverPercent = Number(prata.replace(',', '.'))
    const goldPercent = Number(ouro.replace(',', '.'))

    // Remove as cores de todos svgs
    svgPaths.forEach(svg => svg.style.clipPath = 'inset(0 100% 0 0)')
    
    if (percent > 0 && percent <= bronzePercent) {
        svgPaths[0].style.clipPath = 'inset(0 0 0 0)'

    } else if (percent > bronzePercent && percent < silverPercent) {
        svgPaths[0].style.clipPath = 'inset(0 0 0 0)'
        svgPaths[1].style.clipPath = 'inset(0 0 0 0)'
        
    } else if (percent >= goldPercent) {
        svgPaths[0].style.clipPath = 'inset(0 0 0 0)'
        svgPaths[1].style.clipPath = 'inset(0 0 0 0)'
        svgPaths[2].style.clipPath = 'inset(0 0 0 0)'
    }

    progressValue.innerHTML = `${percent}%`
}