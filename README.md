# Projeto-ERP
Projeto de estudo de como funciona um ERP orientado a logistica.

INFORMACOES BASICAS:

O estado atual do codigo ate hoje foi atingido em cerca de 6h liquidas de aprendizado de como funciona a interacao do Python com o SQLite, nao havia experiencia previa.

Embora simples, aprendi muito enquanto tentava entender a estrutura de um banco de dados e como os dados interagem entre si, basicamente aprendi enquanto fazia.

Kardex: o sistema de kardex funciona porem ainda somente para controle de movimentacoes de estoque simples, me baseei nas interacoes que tive com o ERP Protheus onde trabalho.

A fazer: devo implementar um sistema de interacao com xml de notas fiscais e autenticacao de usuarios para registrar quem realizou e como foi realizada uma movimentacao. Projeto sera retomado apos eu criar uma base de conhecimento mais firme Frontend para fazer uma interface amigavel para o ERP.



CODIGO:

linha 1 a 51: criacao das tabelas .db que receberao os dados cadastrados e como elas devem interagir entre si.

Tabelas criadas:
-Produtos: reponsavel por armazenar os produtos cadastrados e informacoes basicas sobre eles

-Enderecos: responsavel por armazenar os enderecos dos produtos cadastrados a fim de facilitar a gestao de material em um estoque amplo (vantajoso inclusive em pequenos estoques)

-Kardex/Movimentacoes: responsavel por arquivar as movimentacoes de estoque, toda movimentacao de estoque deve ser auditavel e registrada em banco de dados.

-Saldos em estoque: responsavel por armazenar a quantidade de pecas de um determinado produto em estoque, armazenando a quantidade disponivel e reservada (caso uma nota fiscal ainda nao tenha sido emitida porem o saldo ja esta comprometido para uma saida)


Linha 53 a 101: criacao das funcoes que podem ser usadas para inserir dados nas tabelas criadas e como eles interagem entre si

Funcoes definidas:
-Cadastrar SKU: adicionar ao banco de dados um novo produto, sua descricao e tambem sincronizar outras tabelas dependentes da tabela produtos.

-Buscar SKU: busca o sku no banco de dados, utilizei somente para testar a busca de dados no SQLite durante o desenvolvimento.

-Enderecar: definir o endereco de determinados produtos cadastrados.

-Buscar endereco: consultar o endereco da sku referida.

-Movimentar saldo: movimentar o saldo e durante a movimentacao registrar todos os dados em uma tabela para poder realizar a auditoria posteriormente.

