const GLOBAL = {
	isMobile: window.matchMedia("(max-width: 768px)").matches,
	isTablet: window.matchMedia("(max-width: 1180px)").matches,

	/////////////////////////////////////////
	debounceFunction(fn, wait = 1000, timing) {
		return (...args) => {
			console.log("ENTROU DEBOUNCE");
			clearTimeout(timing)
			timing = setTimeout(() => fn(...args), wait)

		}
	},

	////////////////////////////////////////////////////
	defaultAJAX(ajaxurl, data, method = "POST", headers) {
		fetch(ajaxurl, {
			method: method,
			body: JSON.stringify(data),
			headers: {
				'Accept': 'application/json, text/plain, */*',
				'Content-Type': 'application/json',
				...headers
			},
		})
	},
}