# Implementa-o-de-uma-Aplica-o-Cliente-Servidor-com-Sockets-TCP-e-UDP-em-Python

Implementar uma aplicação cliente/servidor que se comunique usando sockets TCP e UDP, a fim de compreender as diferenças de implementação e uso entre esses dois protocolos de transporte
Aplicação Cliente/Servidor com TCP e UDP

## Descrição
Essa aplicação demonstra a comunicação entre cliente e servidor usando os protocolos TCP e UDP. O servidor escuta em duas portas diferentes, uma para cada protocolo, e responde ao cliente com a mesma mensagem recebida, prefixada pelo protocolo utilizado ("TCP:" ou "UDP:").

### Estrutura dos Arquivos
O projeto contém quatro arquivos principais:

servidor_tcp.py: Inicia um servidor TCP escutando na porta 5000.
servidor_udp.py: Inicia um servidor UDP escutando na porta 5001.
servidor.py: Contém um servidor combinado (TCP e UDP) usando threads para gerenciar conexões simultâneas.
cliente.py: Permite ao usuário enviar uma mensagem ao servidor via TCP ou UDP e exibir a resposta.
Requisitos
Python 3 instalado em seu sistema.
Instruções para Executar o Servidor
Opção 1: Executando o Servidor TCP e o Servidor UDP Separadamente
Servidor TCP:

Abra um terminal.
Navegue até o diretório onde os arquivos do projeto estão salvos.
Execute o seguinte comando para iniciar o servidor TCP na porta 5000:
```bash
python servidor_tcp.py
```
O servidor TCP estará escutando por conexões na porta 5000. Ele exibirá mensagens indicando as conexões recebidas e enviará a resposta com o prefixo "TCP:".

Servidor UDP:

Abra um novo terminal.
Navegue até o diretório do projeto.
Execute o seguinte comando para iniciar o servidor UDP na porta 5001:
```bash
python servidor_udp.py
```
O servidor UDP estará escutando por mensagens na porta 5001 e responderá com o prefixo "UDP:".

Opção 2: Executando o Servidor Combinado (TCP e UDP) com Threads
Abra um terminal.
Navegue até o diretório onde os arquivos do projeto estão salvos.
Execute o seguinte comando para iniciar o servidor combinado:
```bash
python servidor.py
```
O servidor combinado usará threads para gerenciar múltiplas conexões TCP e estará disponível para mensagens UDP simultâneas. Ele escutará na porta 5000 para TCP e na porta 5001 para UDP.

Instruções para Executar o Cliente
Abra um terminal.

Navegue até o diretório onde o arquivo cliente.py está salvo.

Execute o cliente com o comando:
```bash
python cliente.py
```
O cliente solicitará que você escolha um protocolo e digite uma mensagem:
Protocolo: Digite "TCP" para enviar uma mensagem via TCP ou "UDP" para enviar via UDP.
Mensagem: Digite qualquer texto que deseja enviar para o servidor, por exemplo, "Olá servidor!" ou "Ping".
O cliente enviará a mensagem ao servidor usando o protocolo escolhido e exibirá a resposta recebida:
Se você escolheu TCP, a resposta será algo como "TCP: sua_mensagem".
Se você escolheu UDP, a resposta será algo como "UDP: sua_mensagem".

Exemplo de Uso
Exemplo de Execução do Cliente
```bash
Escolha o protocolo:
Escolha o protocolo (TCP/UDP): TCP

Digite a mensagem:
Digite a mensagem a ser enviada: Olá servidor!

O cliente exibirá a resposta do servidor:
Resposta do servidor: TCP: Olá servidor!
```
