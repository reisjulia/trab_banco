                                                      Projeto AlphaVidas

Primeiramente usei como base o código enviado no ava que foi feito em aula e o código do período passado, utilizei o mongodb para armazenar os nomes, emails e senhas dos pacientes . 
Crei a pasta venv e o app.py, onde utilizei importei a biblioteca Flask e o Flask-PyMongo para me conectar ao mongodb pelo 
link no app.py e server.js mongodb+srv://juliareisrodrigues5:123@cluster0.9vj78v4.mongodb.net/teste?retryWrites=true&w=majority&appName=Cluster0. Já no server.js, utilizando o espress pelo node.js,
aproveitando o código que tinha,criei e defini rotas utilizando o app.get para lidarem com as requisições HTTP relacionadas ao cadastro(create) update e delete, e também para a página inicial definida como /. No create, 
as informações inseridas pelos pacientes no cadastro são inseridos no mongodb, onde o espress lida com as rotas criadas para as páginas em html para o login /alpha, para fazer o cadastro na rota /cadastro_pac, 
e depois que ele fazer o login direcionado para a rota /bemvindo. Além disso, também coloquei uma rota de POST para o login onde os dados do usuário são verificadas no mongodb.
O HTML e CSS (login/ bemvindo e cadastro_pac), arquivo login.html contém uma aba de login, onde o usuário insere seu e-mail e senha. Se as credenciais forem válidas, o usuário é redirecionado para a página de boas-vindas. 
Caso contrário, é exibida uma mensagem de erro. No app.py, utilizei a biblioteca flask junto com o Flask-PyMongo para se conectar ao banco de dados MongoDB, já informado o link acima. 
