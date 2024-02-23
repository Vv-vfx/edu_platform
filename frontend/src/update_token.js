function updateToken(authToken) {
    console.log(authToken);
    fetch('http://127.0.0.1:8000/api/update_token/', {
        method: 'POST',
        headers: {
            'Authorization': 'Token ' + authToken,
            'Content-Type': 'application/json'
        },
    })
    .then(response => response.json())
    .then(data => {
        console.log('New Token:', data.token);
        // Обновите токен на клиенте
        // Например, сохраните новый токен в localStorage или в переменной
    })
    .catch(error => console.error('Error:', error));
}
