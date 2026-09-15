// Define the function api and function key url
const functionUrl = 'https://homerunfunction-ajbbb0hpe7ajahdt.eastus-01.azurewebsites.net/api/theshow';

// Make a GET request
fetch(functionUrl)
  .then(response => {
    if (!response.ok) {
      throw new Error('Network response was not ok');
    }
    return response.json();
  })
  .then(data => {
    document.getElementById("yordan-homers").textContent = data.Homeruns;
  })
  .catch(error => {
    console.error('Error:', error);
  });