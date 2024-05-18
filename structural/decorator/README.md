Adapter, Como implementar
1 - Certifique-se que seu domínio de negócio pode ser representado como um componente primário com múltiplas camadas opcionais sobre ele.

2 - Descubra quais métodos são comuns tanto para o componente primário e para as camadas opcionais. Crie uma interface componente e declare aqueles métodos ali.

3 - Crie uma classe componente concreta e defina o comportamento base nela.

4 - Crie uma classe decorador base. Ela deve ter um campo para armazenar uma referência ao objeto envolvido. O campo deve ser declarado com o tipo da interface componente para permitir uma ligação entre os componentes concretos e decoradores. O decorador base deve delegar todo o trabalho para o objeto envolvido.

5 - Certifique-se que todas as classes implementam a interface componente.

6 - Crie decoradores concretos estendendo-os a partir do decorador base. Um decorador concreto deve executar seu comportamento antes ou depois da chamada para o método pai (que sempre delega para o objeto envolvido).

7 - O código cliente deve ser responsável por criar decoradores e compô-los do jeito que o cliente precisa.

![img](./imgs/example.png)
