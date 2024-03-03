// IDs para enviar na requisição

var ids = ['05a1e092-9e5a-47sjyj8f-a359-886af8831ec9', 'a2b17286-50f1-48c8-a9f8-2136ea906104'];

// URL da API
var url = 'http://127.0.0.1:8000/api/room/'

// Construindo a URL com os parâmetros da consulta
url += ids.join(',');

// Fazendo a requisição GET
fetch(url)
    .then(response => {
        // Verificando se a resposta foi bem sucedida
        if (!response.ok) {
            console.log(response.error);
        }
        return response.json();
    })
    .then(data => {
        // Manipular os dados recebidos
        console.log(data);
    })
    .catch(error => {
        // Manipular erros
        console.error('Erro:', error);
    });