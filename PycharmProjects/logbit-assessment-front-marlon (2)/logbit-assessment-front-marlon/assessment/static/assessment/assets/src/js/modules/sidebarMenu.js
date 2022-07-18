export default function multiLevelMenu() {
	let state = { open: false, delay: 150 }
	const { isMobile, debounceFunction } = GLOBAL

	const sidebar = document.querySelector(".sidebar")
	const body = document.body

	const fundo = document.querySelector(".nav-fundo ")
	const toogle = document.querySelector("[js-menu-toggle]")
	const currentPage = document.querySelector("[js-page]")


	const handleClickFundo = () => {
		body.classList.remove("menu-ativo")
		toogleMenu()
	}

	const toogleMenu = () => { //calback hover menu
		//funcao do jquery que me da mais certeza c o menu esta aberto ou n
		if (!isMobile) {
			if (body.classList.contains("menu-ativo")) return
			state.open = !$(sidebar).is(":hover")
		}
		
		// console.log(state.open);
		if (state.open) {
			body.classList.add("menu-closed")
			
			const accordions = sidebar.querySelectorAll('.active')
			const accordionContents = sidebar.querySelectorAll('.accordion-content.active')

			if (accordions) {
				accordions.forEach(i => i.classList.remove("active"))
				accordionContents.forEach(i => i.style.height = 0)
			}

			if (isMobile) {
				state.open = false
				body.classList.remove("menu-ativo")
			}
		}

		else {
			body.classList.remove("menu-closed")
			body.classList.remove("menu-ativo")

			if (isMobile) {
				state.open = true
			}
		}
	}

	const handleAddCurrentPageClass = () => {
		const menuItems = sidebar.querySelectorAll('[js-menu-page]')
		const pageName = currentPage ? currentPage.getAttribute('js-page') : ''

		menuItems.forEach(item => {
			if (item.getAttribute('js-menu-page') == pageName)
				item.classList.add('current-page')
		})
	}

	const events = () => {
		if (isMobile) {
			toogle?.addEventListener('click', toogleMenu)

		} else {
			sidebar.addEventListener("mouseenter", debounceFunction(toogleMenu, state.delay))
			sidebar.addEventListener("mouseout", toogleMenu)
			fundo.addEventListener("click", handleClickFundo)
		}

		// sidebar.addEventListener("mousemove", showLevelActive)
	}

	function init() {
		events()
		handleAddCurrentPageClass()

		return this
	}


	return {
		init,
		toogleMenu
	}
}