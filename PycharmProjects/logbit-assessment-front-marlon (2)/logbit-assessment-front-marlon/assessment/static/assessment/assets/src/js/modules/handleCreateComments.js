export default function handleCreateComments(urls, avatar) {
    // Adicionar Comentário ao Vídeo
    const createElement = ({
        id,
        first_name,
        last_name,
        username,
        data_criacao,
        comentario,
        video_id
    
    }) => (`
        <div class="comments--wrapper flex">
            <div class="line--content">
                ${avatar}
            </div>

            <div class="comments--content w-full ml-8">
                <div class="comments--header mt-[.375rem]">
                    <p>${username}</p>
                    <span>${data_criacao}</span>
                </div>

                <div class="comments--text" id="comentario-${id}}">
                    <p class="pt-16 pb-24">${comentario}</p>
                </div>

                <div class="respostas collapse fade show" id="respostas-${id}">
                </div>

                <div class="responder_comentario">
                    ${avatar}

                    <textarea placeholder="Adicione um resposta..." name="comentario" id="id_comentario_${id}" class="form-control"></textarea>
                    <button data-idvideo="${video_id}" data-idcomentario="${id}" type="button" onclick="subComments.createSubComment(this)">Enviar</button>
                </div>
            </div>
        </div>
    `)

    const createComment = async (el) => {
        let video_id = el.dataset.idvideo
        let comentario = el.closest('.criar_comentario').querySelector('textarea').value

        if (comentario.length > 0) {
            el.closest('.criar_comentario').querySelector('textarea').value = ""
           
            const response = await getFetchPOST(urls.url_criar_comentario, {
                comentario: comentario,
                video_id: video_id
            })

            response.video_id = video_id

            let elemento_comentario = createElement(await response)

            document.querySelector(`#comentarios`).innerHTML += (elemento_comentario)

            if (document.querySelector(`#div-not-comments`))
                document.querySelector(`#div-not-comments`).style.display = "none"
        }
    }

    return { createComment }
}