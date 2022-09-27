import accordion from './modules/accordion'
import sidebarMenu from './modules/sidebarMenu'

accordion()

const menu = sidebarMenu().init()
window.menu = menu

document.addEventListener("DOMContentLoaded", () => document.body.classList.add("DOMContentLoaded"))