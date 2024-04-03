async function callData(cookie){
    let id = document.getElementById('id').value;
    let nombre = document.getElementById('nombre').value;
    if( id == ""){
        let data = await fetch('/cashier/id/',{
            method: 'GET',
            
        })
    }
}