const express = require('express');
const app = express();

const PORT = 3000;

app.get('/', (req, res) => {
    res.send('Oiiii');
});

app.get('/users/:userId/books/:bookId', (req, res) => {
    console.log(req.params);
    const { userId, bookId } = req.params
    console.log(userId);
    console.log(bookId);
    res.send(req.params);
});

app.listen(PORT, () => {
    console.log(`O servidor está funcionando na porta: ${PORT}`);
});

const mongoose = require('mongoose');

mongoose.connect('mongodb+srv://juliareisrodrigues5:12345@cluster0.khnin1m.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0', {
    useNewUrlParser: true,
    useUnifiedTopology: true,
    useFindAndModify: false,
    useCreateIndex: true
}).then(() => {
    console.log('Conexão estabelecida ');
}).catch((error) => {
    console.error('Erro ao conectar com banco', error);
});