// Использование токена для запросов к API
function fetchDataWithToken(token) {
    return fetch('http://localhost:8000/api/course/', {
        method: 'GET',
        headers: {
            'Authorization': 'Token ' + token,
            'Content-Type': 'application/json'
        }
    })
        .then(response => response.json())
        .then(data => console.log(data))
        .catch(error => console.error('Error:', error));
}


function fetchResponce(authToken) {
    if (authToken) {
        fetchDataWithToken(authToken);
    } else {
        console.error('No token received');
    }
}

fetchResponce(authToken)

