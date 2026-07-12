import express from 'express';
import router from './routes';

const app = express();
const port = 1245;

app.use('/', router);

app.listen(port, () => {
  console.log(`Server listening on port ${port}`);
});

export default app;
