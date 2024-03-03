const express = require('express');
const app = express();
const port = 8080;

// Endpoint /check que retorna un código 200 (OK)
app.get('/check', (req, res) => res.sendStatus(200));

// Endpoint / que retorna un objeto JSON
app.get('/', (req, res) => {
  res.json({
    "Instancia": "Instancia #1 - API #1",
    "Curso": "Seminario de Sistemas 1",
    "Estudiante": "Estuardo Sebastian Valle Bances - 202001954"
  });
});

app.listen(port, '0.0.0.0', () => {
    console.log(`Server running on port ${port}`);
  });
  