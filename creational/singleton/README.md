# Singleton como implementar:
Adicione um campo privado estático na classe para o armazenamento da instância singleton.

Declare um método de criação público estático para obter a instância singleton.

Implemente a “inicialização preguiçosa” dentro do método estático. Ela deve criar um novo objeto na sua primeira chamada e colocá-lo no campo estático. O método deve sempre retornar aquela instância em todas as chamadas subsequentes.

Faça o construtor da classe ser privado. O método estático da classe vai ainda ser capaz de chamar o construtor, mas não os demais objetos.

Vá para o código cliente e substitua todas as chamadas diretas para o construtor do singleton com chamadas para seu método de criação estático.

![image](./img/structure-pt-br.png)
