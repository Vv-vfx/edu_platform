console.log('update_token.js is loaded!')

window.updateToken = function() {
    // console.log('Old Token: ', authToken);
    let oldAuthToken = localStorage.getItem('authToken')
    fetch('http://127.0.0.1:8000/api/update_token/', {
        method: 'POST',
        headers: {
            'Authorization': 'Token ' + oldAuthToken,
            'Content-Type': 'application/json'
        },
    })
    .then(response => response.json())
    .then(data => {
        console.log('New Token:', data.new_token);
        // Обновляем токен на странице
        document.getElementById('authToken').innerText = data.new_token;
        // Обновляем токен на клиенте, сохраняем новый токен в localStorage
        localStorage.setItem('authToken', data.new_token);


    })
    .catch(error => console.error('Error:', error));
}

function aaa() {
    console.log('aaa called')
}
