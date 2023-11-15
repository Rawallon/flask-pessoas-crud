const API_BASE_URL = 'http://localhost:8000/api/pessoas/';

async function fetchData(url, options = {}) {
    const response = await fetch(url, options);
    return await response.json();
}

async function fetchUserData(userId = "", skip = 0) {
    const url = `${API_BASE_URL}${userId}${skip ? `?skip=${skip}` : ""}?limit=100`;
    return await fetchData(url);
}

async function modifyUserData(userId, action, updatedData = null) {
    const url = `${API_BASE_URL}${userId}`;
    const method = action === 'create' ? 'POST' : (action === 'update' ? 'PUT' : 'DELETE');

    const requestOptions = {
        method,
        headers: {
            'Content-Type': 'application/json',
        },
        body: updatedData ? JSON.stringify(updatedData) : undefined,
    };

    return await fetchData(url, requestOptions);
}

function createInputElement(type, id, value) {
    const inputElement = document.createElement('input');
    inputElement.type = type;
    inputElement.id = id;
    inputElement.value = value;
    return inputElement;
}

function renderTableRow(pessoa) {
    const row = document.createElement("tr");
    row.dataset.id = pessoa.id_pessoa;
    row.innerHTML = `
        <td id="pessoa-nome">${pessoa.nome.split(' ')[0]}</td>
        <td id="pessoa-admissao">${new Date(pessoa.data_admissao).toLocaleDateString('pt-BR')}</td>
        <td>
            <div class="custom-buttons">
                <button class="button is-small is-primary details-button" onclick="showModalPessoa(${pessoa.id_pessoa})">
                    <i class="mdi mdi-eye"></i>
                </button>
                <button class="button is-small is-danger delete-button" onclick="askDeletePessoa(${pessoa.id_pessoa})">
                    <span class="icon"><i class="mdi mdi-trash-can"></i></span>
                </button>
            </div>
        </td>
    `;
    return row;
}

async function loadMorePessoas() {
    const tableBody = document.querySelector(".pessoa-table tbody");
    const pessoas = await fetchUserData("", document.querySelectorAll('tr').length - 1);

    pessoas.forEach((pessoa) => {
        tableBody.appendChild(renderTableRow(pessoa));
    });
}

function fillModalWithData(data) {
    document.getElementById("nome").textContent = data.nome;
    document.getElementById("rg").textContent = data.rg;
    document.getElementById("cpf").textContent = data.cpf;
    document.getElementById("data_nascimento").textContent = new Date(data.data_nascimento).toLocaleDateString('pt-BR');
    document.getElementById("data_admissao").textContent = new Date(data.data_admissao).toLocaleDateString('pt-BR');
    document.getElementById("funcao").textContent = data.funcao;
    document.getElementById("edit-button").setAttribute('onclick', `toggleEditFormModal()`)
    document.getElementById("delete-button").setAttribute('onclick', `askDeletePessoa(${data.id_pessoa})`)
    document.getElementById("save-button").setAttribute('onclick', `updateUserData(${data.id_pessoa})`)

    toggleModalButtonVisibility(false);
    document.getElementById("modal-cliente-data").classList.add("is-active");
}

async function showModalPessoa(pessoaId) {
    const userData = await fetchUserData(pessoaId);
    fillModalWithData(userData);
}

async function askDeletePessoa(pessoaId) {
    const deletePessoa = confirm('Tem certeza que deseja remover essa pessoa?')
    if (deletePessoa) {
        await modifyUserData(pessoaId, 'delete');
        document.querySelector(`tr[data-id="${pessoaId}"]`).remove();
        closeAllModals();
    }
}

async function updateUserDataAndUI(userId, editedData) {
    editedData.id_pessoa = userId;
    await modifyUserData(userId, 'update', editedData);

    fillModalWithData(editedData);

    const pessoaRowChild = document.querySelectorAll(`tr[data-id="${userId}"] td`);
    pessoaRowChild[0].innerText = editedData.nome.split(' ')[0];
    pessoaRowChild[1].innerText = new Date(editedData.data_nascimento).toLocaleDateString('pt-BR');
}

function toggleCreateModal() {
    toggleEditFormModal();
    toggleModalButtonVisibility(true);
    document.getElementById("save-button").setAttribute('onclick', `createPessoa()`)
    document.getElementById("modal-cliente-data").classList.add("is-active");
}

function toggleModalButtonVisibility(isHidden) {
    const editButton = document.getElementById("edit-button");
    const saveButton = document.getElementById("save-button");
    const deleteButton = document.getElementById("delete-button");
    if (isHidden) {
        editButton.parentNode.classList.add('is-hidden');
        deleteButton.parentNode.classList.add('is-hidden');
        saveButton.parentNode.classList.remove('is-hidden');
    } else {
        editButton.parentNode.classList.remove('is-hidden');
        deleteButton.parentNode.classList.remove('is-hidden');
        saveButton.parentNode.classList.add('is-hidden');
    }
}

function getModalInputData() {
    return {
        nome: document.getElementById("input-nome").value,
        rg: document.getElementById("input-rg").value,
        cpf: document.getElementById("input-cpf").value,
        data_nascimento: formatLocalDate(document.getElementById("input-data-nascimento").value),
        data_admissao: formatLocalDate(document.getElementById("input-data-admissao").value),
        funcao: document.getElementById("input-funcao").value,
    };
}


async function createPessoa() {
    const editedData = getModalInputData();

    const newPessoaData = await modifyUserData('', 'create', editedData);

    fillModalWithData(newPessoaData);

    document.querySelector(".pessoa-table tbody").appendChild(renderTableRow(newPessoaData));
    toggleModalButtonVisibility(false);
}


async function updateUserData(pessoaId) {
    const editedData = getModalInputData();

    await updateUserDataAndUI(pessoaId, editedData);

    toggleModalButtonVisibility(false);
}

const formatLocalDate = (dateString) => new Date(Date.parse(dateString.replace(/(\d{2})\/(\d{2})\/(\d{4})/, '$3-$2-$1')));

function toggleEditFormModal() {
    const elements = {
        nome: document.getElementById('nome'),
        rg: document.getElementById('rg'),
        cpf: document.getElementById('cpf'),
        'data-nascimento': document.getElementById('data_nascimento'),
        'data-admissao': document.getElementById('data_admissao'),
        funcao: document.getElementById('funcao'),
    };

    Object.keys(elements).forEach(key => {
        const element = elements[key];
        const inputElement = createInputElement('text', `input-${key}`, element.innerText);
        element.innerHTML = '';
        element.appendChild(inputElement);
    });

    toggleModalButtonVisibility(true);
}

function closeModal(modalWrapper) {
    modalWrapper.classList.remove('is-active');
    toggleModalButtonVisibility(false);
}

function closeAllModals() {
    (document.querySelectorAll('.modal') || []).forEach((modalWrapper) => {
        closeModal(modalWrapper);
    });
}

(document.querySelectorAll('.modal-background, .modal-close') || []).forEach((closeButton) => {
    const modalWrapper = closeButton.closest('.modal');
    closeButton.addEventListener('click', () => {
        closeModal(modalWrapper);
    });
});

document.addEventListener('keydown', (event) => {
    if (event.code === 'Escape') {
        closeAllModals();
    }
});

async function renderTable() {
    const tableBody = document.querySelector(".pessoa-table tbody");
    tableBody.innerHTML = "";

    const pessoas = await fetchUserData();

    pessoas.forEach((pessoa) => {
        tableBody.appendChild(renderTableRow(pessoa));
    });
}

renderTable();
