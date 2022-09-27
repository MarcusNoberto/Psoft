export default function accordion() {
	const accordions = document.querySelectorAll('.accordion-item[js-accordion][js-accordion-gsap]');

	if (!accordions) return

	accordions.forEach(a => {
		const title = a.querySelector(".accordion-title")

		title.addEventListener("click", () => {
			const attrParent = title.getAttribute(`js-comentario-parent`)

			if (attrParent) { //parent accordion
				document.querySelectorAll(`.accordion-title[js-comentario-parent="${attrParent}"]`)
					.forEach(i => {
						console.log(i, title)
						if (i !== title) {
							if (i.closest(".accordion-item").classList.contains("active")) {
								i.click()
							}
						}
					})
			}

			const idAccordion = title.getAttribute("data-accordion");
			const content = a.querySelector(`.accordion-content[data-accordion="${idAccordion}"]`)
			const height = content.scrollHeight

			a.classList.toggle("active");
			content.classList.toggle("active");


			if (content.classList.contains("active")) {
				gsap.fromTo(content, { height: 0 }, { height: "auto", duration: 0.3 })
			} else {
				gsap.fromTo(content, { height: height }, { height: 0, duration: 0.3 })
			}


		})
	})


}