const ModalContainer = document.querySelector('.modal-container');
const ModalExcluir = document.querySelector('.excluir');

function abrirModal() {
    ModalContainer.classList.add('active')
    
}

const editar = document.querySelector('.editar');
const remover = document.querySelector('.remover');

let pontDelete = document.querySelector('.pont-delete');


editar.addEventListener('click', function(event) {
    
    if (event.target.id == '') {
        return
    }
    pontDelete.value = event.target.id
    ModalExcluir.classList.add('active')
     
})

