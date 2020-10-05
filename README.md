# Cotações TRYD

A função irá retornar um Dataframe Pandas com o histórico de cotações diárias dos ativos selecionados.

O Tryd por padrão armazena o histórico de cotações na pasta "C:\Tryd5\workspace\historico", caso seu TRYD esteja instalado em outro diretório, alterar informar na variável 'path'

É necessário que o histórico das cotações estejam salvos localmente, por padrão o Tryd sempre baixa o histórico quando você consulta o gráfico de um ativo (somente no período de tempo selecionado). 
Porém é possível otimizar e atualizar os ativos com histórico local acessando a opção "Gráficos > Gerenciador de Históricos"

Após isso, basta chamar a função informando a lista dos ativos que deseja.

Enjoy!
