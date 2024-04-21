var client = [];
const opcion1 = document.getElementById('inlineCheckbox1');
const opcion2 = document.getElementById('inlineCheckbox2');
const opcion3 = document.getElementById('inlineCheckbox3');
async function isClientExist() {
    let cedula = document.getElementById("cedula").value;
    try {
        const data = await fetch('/cashier/search_client/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ 'dni': cedula })
        })
        if (data.ok) {
            let json = await data.json();
            fillData(json);
        }
    } catch (error) {
        console.log(error);
    }
}

function fillData(data) {
    document.getElementById('name').value = data[0].nombreCliente;
    document.getElementById('email').value = data[0].correo;
    document.getElementById('telefono').value = data[0].telefono;
}

async function generateSale() {
    const sale = obtenerDatosTabla();
    console.log(sale);
    client[0] = document.getElementById("cedula").value;
    client[1] = document.getElementById("name").value;
    client[2] = document.getElementById("email").value;
    client[3] = document.getElementById("telefono").value;
    let data = {
        'cliente': client,
        'productos': sale,
        'subtotal': document.getElementById("subtotal").innerText,
        'total': document.getElementById("total").innerText,
        'iva': document.getElementById("iva").innerText,
    }
    try {
        const response = await fetch('/cashier/create_sale/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(data)
        })
        if (response.ok) {

        }
    } catch (error) {
        console.error(error);
    }
}
function obtenerDatosTabla() {
    let tabla = document.getElementById("data-table");
    let filas = tabla.getElementsByTagName("tr");
    let datosTabla = [];
    for (let i = 1; i < filas.length; i++) {
        let celdas = filas[i].getElementsByTagName("td");
        let datosFila = [];
        for (let j = 0; j < celdas.length; j++) {
            if (j == 2) {
                continue;
            }
            else if (j == 5) {
                datosFila.push(celdas[j].getElementsByTagName("input")[0].value);
            } else {
                datosFila.push(celdas[j].innerText);
            }
        }
        datosTabla.push(datosFila);
    }
    return datosTabla;
}
console.log(opcion1)
function validateModalToShow() {
    if (opcion1.checked) {
        const modal1 = document.getElementById("clientModal");
        modal1.classList.add('show');
        modal1.classList.add('d-block');
        modal1.classList.remove('hide');
        modal1.classList.remove('d-none');
    }
    else if (opcion2.checked) {
        const modal2 = document.getElementById("nequiModal");
        modal2.classList.add('show');
        modal2.classList.add('d-block');
        modal2.classList.remove('hide');
        modal2.classList.remove('d-none');
    } else {
        const modal3 = document.getElementById("daviplataModal");
        modal3.classList.add('show');
        modal3.classList.add('d-block');
        modal3.classList.remove('hide');
        modal3.classList.remove('d-none');
    }
}

function changeClientModal(modalId){
    cerrarModal(modalId);
    opcion1.checked = true;
    validateModalToShow();
}
function cerrarModal(modalId) {
    const modal = document.getElementById(modalId);
    modal.classList.remove('show');
    modal.classList.remove('d-block');
    modal.classList.add('hide');
    modal.classList.add('d-none');
}
  

//buscar Cliente
let btnClient = document.getElementById('btnClient');
btnClient.addEventListener('click', isClientExist);
//validar modal
let btnSale = document.getElementById('showModal');
btnSale.addEventListener('click', validateModalToShow);
//Finalizar compra
let btnFinalizar = document.getElementById('makeSale');
btnFinalizar.addEventListener('click', generateSale);