

$(document).ready(function() {

    $('.chat').on('click', function(e) {
    let pk_response = e.target.id;

    fetch(`http://127.0.0.1:8000/response/${ pk_response }/messages/`)
    .then((response) => {
        return response.text();

    })
    .then((data) => {
        console.log(data)
        obj = document.getElementById('message-modal-body');
        obj.innerHTML = data
    });

    })
    })

