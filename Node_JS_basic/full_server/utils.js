import fs from 'fs';

const readDatabase = (filePath) => new Promise((resolve, reject) => {
  fs.readFile(filePath, 'utf8', (error, data) => {
    if (error) {
      reject(error);
      return;
    }

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

    resolve(byField);
  });
});

export default readDatabase;
