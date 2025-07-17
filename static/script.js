const ModalContainer = document.querySelector('.modal-container');
const ModalAterar = document.querySelector('.alterar');
const ModalExcluir = document.querySelector('.excluir');
const tabela = document.querySelector('.tabela');
let pontUpdate = document.querySelector('.pont-opdate');
let pontDelete = document.querySelector('.pont-delete');

function abrirModal() {
    ModalContainer.classList.add('active')
    
}

tabela.addEventListener('click', function(event) {

    const ElementoClicado = event.target;

    if (ElementoClicado.id == '') {
        return
    }

    if (ElementoClicado.classList.contains('fa-pen-to-square')) {
        pontUpdate.value = ElementoClicado.id
        ModalAterar.classList.add('active')
    }

    if (ElementoClicado.classList.contains('fa-trash')) {
        pontDelete.value = ElementoClicado.id
        ModalExcluir.classList.add('active')
    }
    
})

