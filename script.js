const button = document.querySelector('.button-add-task')
const input = document.querySelector('.input-task')
const listaCompleta = document.querySelector('.list-tasks')

let minhaListaDeItens = []




function adicionarNovaTarefa(){

    if (input.value == ''){
        alert('Adicione uma tarefa no campo!')
        return
    }

    minhaListaDeItens.push({
        tarefa: input.value,
        concluida: false
    })

    input.value = ''
    mostrarTarefas()
    
}

function mostrarTarefas(){
    let novaLi = ''
    minhaListaDeItens.forEach((item,posicao) => {
        novaLi = novaLi + `
        
        <li class="task ${item.concluida && "done"}">
            <img src="img/checked.png" alt="" onclick="concluirtarefa(${posicao})">
            <p>${item.tarefa}</p>
            <img src="img/trash.png" alt="" onclick="deletarItem(${posicao})">
        </li>

        `
    })

    listaCompleta.innerHTML = novaLi
    localStorage.setItem('lista', JSON.stringify(minhaListaDeItens))
}

function concluirtarefa(posicao){
    minhaListaDeItens[posicao].concluida = ! minhaListaDeItens[posicao].concluida
    mostrarTarefas()
    
}

function deletarItem(posicao){
    minhaListaDeItens.splice(posicao, 1)
    mostrarTarefas()

}


function recarregartarefa(){
    const tarefasDolocalStorage = localStorage.getItem('lista')
    if (tarefasDolocalStorage) {
        minhaListaDeItens = JSON.parse(tarefasDolocalStorage)
    }
    mostrarTarefas()
}

recarregartarefa()
button.addEventListener('click', adicionarNovaTarefa)