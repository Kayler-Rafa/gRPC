# Serviço de Mensageria com gRPC

Este projeto é uma implementação simples de um serviço de mensageria remota utilizando gRPC em Python. O serviço permite o envio de mensagens para destinatários definidos, retornando um status de confirmação após o envio.

## Estrutura do Projeto

- **mensageria.proto**: Arquivo que define o contrato do serviço (request, response e método).
- **mensageria_pb2.py**: Arquivo gerado automaticamente a partir do arquivo `.proto`. Contém as classes de dados.
- **mensageria_pb2_grpc.py**: Arquivo gerado automaticamente que contém o código do serviço gRPC.
- **mensageria_server.py**: Implementação do servidor gRPC que processa as mensagens enviadas pelos clientes.
- **mensageria_client.py**: Cliente gRPC que envia mensagens ao servidor.

## Como Executar

### Pré-requisitos

- **Python 3.7+**
- **gRPC para Python**: Instale as dependências necessárias executando:
  ```bash
  pip install grpcio grpcio-tools
  }}}

### Passo a Passo

1. **Clonar o repositório**:
   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git
   cd seu-repositorio
   }}}

2. **Gerar os arquivos Python a partir do `.proto`**:
   Execute o seguinte comando para gerar os arquivos `mensageria_pb2.py` e `mensageria_pb2_grpc.py`:
   ```bash
   python -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. mensageria.proto
   }}}

3. **Iniciar o servidor**:
   Em um terminal, execute o servidor gRPC:
   ```bash
   python mensageria_server.py
   }}}

4. **Executar o cliente**:
   Em outro terminal, execute o cliente gRPC para enviar uma mensagem:
   ```bash
   python mensageria_client.py
   }}}

   O cliente enviará uma mensagem ao servidor e receberá uma resposta de confirmação.

### Estrutura do Arquivo `mensageria.proto`

O arquivo `mensageria.proto` define o serviço da seguinte maneira:

```proto
syntax = "proto3";

package mensageria;

service MensageriaService {
  rpc EnviarMensagem (MensagemRequest) returns (MensagemResponse) {}
}

message MensagemRequest {
  string mensagem = 1;
  string destinatario = 2;
}

message MensagemResponse {
  string status = 1;
}
}}}

### Exemplo de Uso

1. Ao rodar o **servidor**, ele ficará escutando por mensagens.
2. O **cliente** envia uma mensagem como "Olá!" para um destinatário.
3. O **servidor** processa a mensagem e retorna uma resposta "Mensagem entregue com sucesso!" ao cliente.

### Autor

Feito por **Diniz**.
