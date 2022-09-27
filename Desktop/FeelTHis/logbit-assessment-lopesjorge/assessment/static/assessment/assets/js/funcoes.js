//API FETCH GLOBAL - Requisições via javascript

const getFetchPOST = async (ajaxurl,  data) => {
      
    data = JSON.stringify(data)
    
     await fetch(ajaxurl, {
      method: 'POST',
      body: data,
      headers: {
        "Accept": "application/json, text/plain, */*",
        "Content-Type": "application/json",
        "X-CSRFToken": valid_csrf_token,
      },
    }).then(res => res.json()).then(
      res => resultado = res
    );
    return resultado
}
