export default function handleCreateSubComments(urls, avatar) {
    // Adicionar Resposta ao Comentário
    const createElement = ({
        id_comentario,
        first_name,
        last_name,
        username,
        data_criacao,
        comentario

    }) => (`
        <div class="comments--header">
            ${avatar}

            <p>${username}</p>
            <span>${data_criacao}</span>
        </div>

        <div class="comments--text">
            <p class="pt-4 pb-8">${comentario}</p>
        </div>
    `)

    const createSubComment = async (el) => {
        let video_id = el.dataset.idvideo
        let comentario_id = el.dataset.idcomentario
        let comentario = el.closest('.responder_comentario').querySelector('textarea').value

        const comentsContainer =  el.closest('.comments--wrapper')
        const myTab = comentsContainer.querySelector('[data-toggle="collapse"]')

        if (comentario.length > 0){
            el.closest('.responder_comentario').querySelector('textarea').value = ""

            const response = await getFetchPOST(urls.url_criar_comentario, {
                comentario: comentario,
                comentario_id: comentario_id,
                video_id: video_id
            })


            let elemento_sub_comentario = createElement(await response)

            const container =  document.querySelector(`#respostas-${comentario_id}`)
            const ultimo = container.closest(".comments--content").querySelector(".responder_comentario")

            container.innerHTML += (elemento_sub_comentario)

            //se a tab estiver fechada abra se n nada
            if(myTab && !myTab.getAttribute("aria-expanded")){
                myTab.click()

                setTimeout(() => {
                    ultimo.scrollIntoView({block: "end", behavior: "instant"})
                }, 450)

            }

            setTimeout(() => { ultimo.querySelector("textarea").focus() }, 450)
        }
    }

    return { createSubComment }
}