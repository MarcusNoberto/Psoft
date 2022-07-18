export default function initChoices(el, options) {
    new Choices(el, {
        silent: true,
        placeholder: true,
        searchResultLimit: 10,
        placeholderValue: 0,
        renderChoiceLimit: -1,
        itemSelectText: 'Selecionar',
        noResultsText: 'Nada Encontrado...',
        shouldSort: false,
        searchEnabled: false,
        searchChoices: false,
        ...options
    })
}