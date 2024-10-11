const path = '/Programação Web/Projeto/XLSX/Dados.xlsx';

fetch(path).then(response => response.arrayBuffer()).then(data => {
    const workbook = XLSX.read(data, { type: 'array'});
    const sheet = workbook.Sheets[workbook.SheetNames[0]];
    const users = XLSX.utils.sheet_to_json(sheet);

    displayUserGrid(users);
}).catch(error => console.error('Erro a carregar este ficheiro:', error));

function displayUserGrid(users){
    const gridContainer = document.getElementById('GridUser');
    const tbody = gridContainer.querySelector('tbody');

    tbody.innerHTML = '';

    users.forEach(user => {
        const row = tbody.insertRow();
        ['Email', 'Telefone', 'NIFs:'].forEach(key => {
            const cell = row.insertCell();
            cell.textContent = user[key];
        });
    });
}