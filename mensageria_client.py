import grpc
import mensageria_pb2
import mensageria_pb2_grpc

def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = mensageria_pb2_grpc.MensageriaServiceStub(channel)

        request = mensageria_pb2.MensagemRequest(mensagem="Olá!", destinatario="Dinz")
        
        response = stub.EnviarMensagem(request)
        print(f"Resposta do servidor: {response.status}")

if __name__ == '__main__':
    run()
