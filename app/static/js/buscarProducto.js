var totalSubtotal = [];
var totalIva = [];
var totalBruto = [];

async function callData() {
    let id = document.getElementById('id').value;
    let nombre = document.getElementById('nombre').value;
    let info = { nombre: nombre, id: id };
    try {
        let data = await fetch('/cashier/search_product/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(info)
        });
        if (data.ok) {
            let json = await data.json();
            insertDataRow(json);
        }
    } catch (e) {
        console.error(e);
    }
}
function insertDataRow(data) {
    let table = document.getElementById("data-table").getElementsByTagName("tbody")[0];
    let input = document.createElement("input");
    input.className = "form-control";
    input.type = "number";
    input.placeholder = "Cantidad";
    input.id = "quantity";
    input.value = 1;
    data.forEach(item => {
        let row = table.insertRow();
        var rowIndex = row.rowIndex;
        let cellID = row.insertCell(0);
        let cellName = row.insertCell(1);
        let cellOption = row.insertCell(2);
        let cellPrice = row.insertCell(3);
        let cellIva = row.insertCell(4);
        let cellQuantity = row.insertCell(5);
        let cellTotal = row.insertCell(6);

        cellID.textContent = item.idProducto;
        cellName.textContent = item.nombreProducto;
        let button = document.createElement("button");
        button.className = 'btn btn-danger';
        button.innerHTML = `<i class="fa-solid fa-xmark"></i>`
        button.type = 'button';
        button.onclick = function () {
            deleteRow(rowIndex);
        }
        cellOption.appendChild(button);
        cellPrice.textContent = item.precioCompra;
        cellIva.textContent = item.ivaProducto;
        input.onchange = () => {
            estimatePrice(input.value, cellPrice.textContent, cellTotal, cellIva.textContent, rowIndex);
        }
        estimatePrice(input.value, cellPrice.textContent, cellTotal, cellIva.textContent, rowIndex);
        cellQuantity.appendChild(input); 
    });
}

function estimatePrice(quantity, value, cellTotal, iva, row) {
    let subtotal = parseFloat(quantity) * parseFloat(value);
    iva = (subtotal * iva) / 100;
    let total = subtotal + iva;
    cellTotal.textContent = total.toFixed(2);
    updatesRegister(subtotal, total, iva, row);
}
function updatesRegister(subtotal, total, iva, row) {
    totalSubtotal[row] = subtotal;
    totalIva[row] = iva;
    totalBruto[row] = total;
    document.getElementById('subtotal').innerText = totalSubtotal.reduce((a , b) => a + b, 0);
    document.getElementById('total').innerText = totalBruto.reduce((a , b) => a + b, 0);
    document.getElementById('iva').innerText = totalIva.reduce((a , b) => a + b, 0);
}

function deleteRow(row) {
    console.log(row);
    let table = document.querySelector("table");
    table.deleteRow(row);
    updatesRegister(0,0,0,row);
}
let buscar = document.getElementById('search');
buscar.addEventListener('click', callData);