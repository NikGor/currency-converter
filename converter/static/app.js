const API_BASE_URL = `${window.location.protocol}//${window.location.hostname}:8000`;

document.getElementById('convert-form').addEventListener('submit', function(e) {
    e.preventDefault();

    // Получение данных из формы
    var amount = document.getElementById('amount1').value;
    var currency1 = document.getElementById('currency1').value;
    var currency2 = document.getElementById('currency2').value;

    // Отправка запроса к API
    fetch(`${API_BASE_URL}/convert`, { // Убедитесь, что endpoint соответствует FastAPI маршруту
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ amount: amount, currency_from: currency1, currency_to: currency2 })
    })
    .then(response => response.json())
    .then(data => {
        if (data.result) {
            document.getElementById('result').value = data.result;
        } else {
            alert(data.error);
        }
    })
    .catch(error => console.error('Error:', error));
});

document.addEventListener('DOMContentLoaded', (event) => {
// Определение базового URL для API
    const API_DOCS_URL = `${window.location.protocol}//${window.location.hostname}:8000/docs`;

    // Находим элемент ссылки по классу 'nav-link' и тексту 'Documentation'
    const docsLink = Array.from(document.getElementsByClassName('nav-link')).find(link => link.textContent === 'Documentation');

    // Если такой элемент существует, обновляем атрибут 'href'
    if(docsLink) {
      docsLink.setAttribute('href', API_DOCS_URL);
}
});