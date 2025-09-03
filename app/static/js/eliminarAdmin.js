function deleteNote(ide, protocol, url){
    Swal.fire({
        title: "¿Estas seguro?",
        text: "Si lo eliminas ya no lo tendras",
        icon: "warning",
        showCancelButton: true,
        confirmButtonColor: "#3085d6",
        cancelButtonColor: "#d33",
        confirmButtonText: "Si"
      }).then((result) => {
        if (result.isConfirmed) {
            fetch('/admin/delete_'+url+'/'+ide,{
                method: 'DELETE',
                headers: {
                    'Content-Type': 'application/json',
                    'X-CSRFToken': protocol
                }
            })
            . then( res =>{
                if(res.ok){
                    Swal.fire({
                        title: "Eliminado",
                        text: "Ha sido eliminado correctamente",
                        icon: "success"
                      });
                    location.reload();
                } else {
                    Swal.fire({
                        title: "No ha sido eliminado correctamente",
                        text: "Hubo un problema intente nuevamente",
                        icon: "error"
                      });
                }
            })
        }
      });
}
