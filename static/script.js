const ModalContainer = document.querySelector('.modal-container');

function abrirModal() {
    ModalContainer.classList.add('active')
    
}

const editar = document.querySelector('.editar');
const remover = document.querySelector('.remover');


editar.addEventListener('click', function(event) {
    
    console.log(event.target.id)
})

