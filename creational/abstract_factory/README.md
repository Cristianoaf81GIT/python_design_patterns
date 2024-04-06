# Abstract Factory Como implementar?

1 - Mapeie uma matriz de tipos de produtos distintos versus as variantes desses produtos.

2 - Declare interfaces de produto abstratas para todos os tipos de produto. Então, faça todas as classes concretas de produtos implementar essas interfaces.

3 - Declare a interface da fábrica abstrata com um conjuntos de métodos de criação para todos os produtos abstratos.

4 - Implemente um conjunto de classes fábricas concretas, uma para cada variante de produto.

5 - Crie um código de inicialização da fábrica em algum lugar da aplicação. Ele deve instanciar uma das classes fábrica concretas, dependendo da configuração da aplicação ou do ambiente atual. Passe esse objeto fábrica para todas as classes que constroem produtos.

6 - Escaneie o código e encontre todas as chamadas diretas para construtores de produtos. Substitua-as por chamadas para o método de criação apropriado no objeto fábrica.


