import grpc
from concurrent import futures
import time

import mensageria_pb2
import mensageria_pb2_grpc

class MensageriaService(mensageria_pb2_grpc.MensageriaServiceServicer):
    def EnviarMensagem(self, request, context):
        print(f"Mensagem recebida: {request.mensagem}, para: {request.destinatario}")
        return mensageria_pb2.MensagemResponse(status="Mensagem entregue com sucesso!")

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    mensageria_pb2_grpc.add_MensageriaServiceServicer_to_server(MensageriaService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Servidor gRPC iniciado na porta 50051")
    try:
        while True:
            time.sleep(86400)  
    except KeyboardInterrupt:
        server.stop(0)

if __name__ == '__main__':
    serve()
