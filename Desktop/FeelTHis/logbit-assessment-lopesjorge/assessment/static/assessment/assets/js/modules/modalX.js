function ModalX(el, opts) {
	//classes
	const classOpen = `modal--open`
	const classMain = 'modal--content'
	const classActive = "active"
	const ElNotPoint = el.replace(".", "")
	const deep = document.createElement('div')

	const options = {
		...opts
		//deep: true,
		// zIndex: 300000,
		// zIndexDeep:900
		// closeOnSwipe: true,
		// observer: true,
		// bgMOdal : white
	}

	//els
	const body = document.body
	const elModal = document.querySelector(el);
	const items = elModal.querySelectorAll(`.${classMain}`)

	const state = { //STATE
		open: false,
		id_active: "",
		dragable: false,
	}

	const changeIDActive = (id) => state.id_active = id

	const keyClose = (e) => e.key === 'Escape' ? closeModal() : null

	function createElementAndAppend(el, src, type = "text/javascript",) {  // UTILITY
		const script = document.createElement(el)
		script.type = type
		script.src = src
		document.body.appendChild(script)
	}


	function createDeep() { // FUNDO
		if (options.deep) {
			document.body.appendChild(deep)
			deep.classList.add(`${ElNotPoint}--deep`)
			deep.addEventListener('click', closeModal)
			return this
		}

	}


	function openModal(item, classX) { //OPEN
		const elemento = typeof item === "object"
		const id = elemento ? item.dataset.id : item

		changeIDActive(id)
		state.dragable = true
		const actualSectionActive = elModal.querySelector(`section[data-id="${state.id_active}"]`)

		classX ? addClassOnModal(true, classX) : ""

		elModal.classList.add(classActive)
		deep.classList.add(classActive)
		body.classList.add(`${classOpen}-${ElNotPoint}`)

		items && items.forEach(i => i.classList.remove(classActive))
		actualSectionActive && actualSectionActive.classList.add(classActive)
		state.id_active = id
		elModal.dataset.active = state.id_active
		state.open = true
		body.addEventListener("keydown", keyClose)
		return this
	}



	function closeModal() { // CLOSE
		const modalWidth = `${elModal.getBoundingClientRect().width.toFixed(0)}px `
		const modalHeight = `${elModal.getBoundingClientRect().height.toFixed(0)}px `

		elModal.style.minWidth = `${modalWidth} `
		elModal.style.minHeight = `${modalHeight} `
		elModal.style.width = `${modalWidth} `
		elModal.style.height = `${modalHeight} `


		changeIDActive("")
		state.dragable = false

		body.classList.remove(`${classOpen}-${ElNotPoint}`)

		items && items.forEach(i => i.classList.remove(classActive))
		elModal.classList.remove(classActive)
		deep.classList.remove(classActive)

		state.id_active = ''
		elModal.dataset.active = state.id_active
		state.open = false

		addClassOnModal(false)
		body.removeEventListener("keydown", keyClose)
		setTimeout(() => {
			elModal.style.removeProperty("min-width")
			elModal.style.removeProperty("width")
			elModal.style.removeProperty("min-height")
			elModal.style.removeProperty("height")
		}, 300)
		return this
	}

	function toggleModal(target, classX) { // TOGGLE
		state.open ? closeModal() : openModal(target)
		return this
	}

	function addClassOnModal(verification, classX) {
		verification ? elModal.setAttribute('data-classX', classX) :
			elModal.removeAttribute('data-classX')
	}


	function dataOpenEClose() { //DATA-ATRIBUTE
		const dataOpen = document.querySelectorAll(`[data-xopen="${ElNotPoint}"]`)
		const dataClose = document.querySelectorAll(`[data-xclose="${ElNotPoint}"]`)
		const dataToggle = document.querySelectorAll(`[data-xtoggle="${ElNotPoint}"]`)

		dataOpen.forEach(i => i.addEventListener('click', (ev) => {
			openModal(i)
			const target = ev.currentTarget
			const haveClassAttribute = target.dataset.classx

			if (haveClassAttribute) {
				addClassOnModal(true, haveClassAttribute)
			}
		}))

		dataClose.forEach(i => i.addEventListener('click', () => closeModal()))
		dataToggle.forEach(i => i.addEventListener('click', () => toggleModal(i)))
	}



	async function addHammerTag() {
		if (options.closeOnSwipe) {
			const hammerLink = "https://hammerjs.github.io/dist/hammer.min.js"
			const temHammer =
				Array.from(document.scripts)
					.filter(e => e.src === hammerLink).length === 1

			if (temHammer) { return }

			createElementAndAppend("script", hammerLink)
		}
	}

	async function hammerFeature() { // HAMMER

		addHammerTag()

		if (options.closeOnSwipe) {
			const toogles = elModal.querySelectorAll("header.modal--header .hammer--toggle")


			var makeTouchable = {};

			makeTouchable.preparingHammer = function () {

				function dragModal(toogle) {
					return function (ev) {
						if (state.dragable) {
							if (ev.deltaY >= 200) {
								delModal(toogle)
								return
							}

							if (ev.deltaY <= 0) return

							toogle.style.transition = 'none';
							toogle.style.transform = 'translateY(' + (ev.deltaY / 4) + 'px)';
							toogle.style.background = "#CFF6E4";
							toogle.style.opacity = "1";


						}

					}
				}

				function resetModal(toogle) {
					return function (ev) {
						if (state.dragable) {
							if (ev.deltaY >= 140) {
								delModal(toogle)
								return
							}

							toogle.style.transition = 'transform .3s ease, opacity .3s ease';
							toogle.style.transform = 'translateY(0)';
							toogle.style.removeProperty("background");
							toogle.style.removeProperty("opacity")
						}

					}
				}

				function delModal(toogle) {
					toogle.style.transition = 'transform .4s';
					toogle.style.removeProperty("transform");
					toogle.style.removeProperty("background");
					toogle.style.removeProperty("opacity");
					closeModal()
				}



				var hammerOptions = {
					recognizers: [
						// RecognizerClass, [options], [recognizeWith, ...], [requireFailure, ...]        
						[Hammer.Pan, { direction: Hammer.DIRECTION_VERTICAL }],
						[Hammer.Swipe, { direction: Hammer.DIRECTION_VERTICAL, threshold: 10 }, ['pan']],
					]
				}

				function initTouchEvents(el) {
					var swipeableEl = new Hammer.Manager(el, hammerOptions);
					//var swipeableEl = new Hammer(el);
					const toogle = el.querySelector(".hammer--toggle")
					swipeableEl
						.on('pan', dragModal(toogle))
						.on('panend', resetModal(toogle))
					// .on('swipe', delModal);

				}



				toogles.forEach(i => {
					initTouchEvents(i.closest("header"));
				})

			}

			await new Promise(resolve => {
				const interval = setInterval(() => {
					if (!window.Hammer) { return }
					else {
						clearInterval(interval)
						makeTouchable.preparingHammer()
						resolve()
					}

				}, 50);

			})




		}


	}

	function addStyles() { //STYLES
		options.zIndex ? elModal.style.setProperty('--zindex-modal', options.zIndex) : ""
		options.bgModal ? elModal.style.setProperty('--bg-modal', options.bgModal) : ""
		options.zIndexDeep ? deep.style.setProperty('--zindex-deep', options.zIndexDeep) : ""
	}

	function ObserverModal() { // OBSERVER
		if (options.observer) {
			const observer = new MutationObserver(mutations => {
				mutations.forEach(mutation => {
					if (mutation.type == "attributes") {
						// if (mutation.target.dataset.active) { }
					}

				})
			})

			observer.observe(elModal, {
				attributes: true,
				// attributeFilter: ['data-active']
			})
		}
	}


	function init() {
		dataOpenEClose()
		createDeep()
		hammerFeature()
		addStyles()
		ObserverModal()
		return this
	}

	return {
		elModal,
		state,
		openModal,
		closeModal,
		toggleModal,
		init
	}


}