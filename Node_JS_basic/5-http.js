const http = require('http');
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

const app = http.createServer((req, res) => {
  res.statusCode = 200;
  res.setHeader('Content-Type', 'text/plain');

  if (req.url === '/') {
    res.end('Hello Holberton School!');
    return;
  }

  if (req.url === '/students') {
    const dbPath = process.argv[2];
    getStudentsReport(dbPath)
      .then((report) => {
        res.end(`This is the list of our students\n${report}`);
      })
      .catch((error) => {
        res.end(`This is the list of our students\n${error.message}`);
      });
    return;
  }

  res.end('Hello Holberton School!');
});

app.listen(1245);

module.exports = app;
