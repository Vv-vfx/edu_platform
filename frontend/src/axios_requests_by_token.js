import axios from "axios";

// Использование токена для запросов к API
function fetchDataWithToken(token) {

    axios.get('http://localhost:8000/api/coursecategory/', {
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


function fetchDataWithTokenAxios() {
    let authToken = localStorage.getItem('authToken');
    if (authToken) {
        fetchDataWithToken(authToken);
    } else {
        console.error('No token received');
    }
}

fetchDataWithTokenAxios(authToken)

