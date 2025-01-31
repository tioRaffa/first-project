

function gritar() {
    alert('AAAAAAAAAAAAAAAAAIN');
}


function perguntar() {
    var nome
    nome = prompt('Qual seu nome? ')
    alert('Olá!, ' + nome);
}


function mudar_h1() {
    var novo_nome
    novo_nome = prompt('Novo nome do h1')
    
    var h1 = document.getElementsByTagName('h1')
    let nomeh1 = h1[0].innerHTML
    h1[0].innerText = novo_nome

    alert(`Nome ${nomeh1} alterado com sucesso para -> ${novo_nome}`)
}


function incrementar() {
    var p1 = document.getElementById('p1');

    p1.innerText = parseInt(p1.innerText) + 1;

}