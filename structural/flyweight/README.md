# Flyweight, Como implementar:  

1 - Divida os campos de uma classe que irá se tornar um flyweight em duas partes:
2 - o estado intrínseco: os campos que contém dados imutáveis e duplicados para muitos objetos
3 - o estado extrínseco: os campos que contém dados contextuais únicos para cada objeto
4 - Deixe os campos que representam o estado intrínseco dentro da classe, mas certifique-se que eles sejam imutáveis. Eles só podem obter seus valores iniciais dentro do construtor.
5 - Examine os métodos que usam os campos do estado extrínseco. Para cada campo usado no método, introduza um novo parâmetro e use-o ao invés do campo.
6 - Opcionalmente, crie uma classe fábrica para gerenciar o conjunto de flyweights. Ela deve checar por um flyweight existente antes de criar um novo. Uma vez que a fábrica está rodando, os clientes devem pedir flyweights apenas através dela. Eles devem descrever o flyweight desejado ao passar o estado intrínseco para a fábrica.
7 - O cliente deve armazenar ou calcular valores para o estado extrínseco (contexto) para ser capaz de chamar métodos de objetos flyweight. Por conveniência, o estado extrínseco junto com o campo de referência flyweight podem ser movidos para uma classe de contexto separada.


![img](./img/example.png)
