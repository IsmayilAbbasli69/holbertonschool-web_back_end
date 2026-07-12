const express = require('express');
const fs = require('fs');

function getStudentsReport(path) {
  return fs.promises.readFile(path, 'utf8')
    .then((data) => {
      const rows = data.split('\n').filter((line) => line.trim() !== '');
      const students = rows.slice(1);
      const byField = {};

      students.forEach((student) => {
        const [firstname, , , field] = student.split(',');
        if (!byField[field]) {
          byField[field] = [];
        }
        byField[field].push(firstname);
      });

      const lines = [`Number of students: ${students.length}`];
      Object.keys(byField).forEach((field) => {
        lines.push(`Number of students in ${field}: ${byField[field].length}. List: ${byField[field].join(', ')}`);
      });
      return lines.join('\n');
    })
    .catch(() => {
      throw new Error('Cannot load the database');
    });
}

const app = express();

app.get('/', (req, res) => {
  res.status(200).type('text/plain').send('Hello Holberton School!');
});

app.get('/students', (req, res) => {
  const dbPath = process.argv[2];
  getStudentsReport(dbPath)
    .then((report) => {
      res.status(200).type('text/plain').send(`This is the list of our students\n${report}`);
    })
    .catch((error) => {
      res.status(200).type('text/plain').send(`This is the list of our students\n${error.message}`);
    });
});

app.listen(1245);

module.exports = app;
