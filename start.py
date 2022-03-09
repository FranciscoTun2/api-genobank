import sys
import multiprocessing
from settings import settings
from run import runweb

server = runweb.GenoBank()
server.start(port = settings.PORT)

# def worker(port):
#     server = runweb.GenoBank()
#     server.start(port = port)

# if __name__ == '__main__':
#     jobs = []
#     ports = [settings.PORT]
#     for port in ports:
#         p = multiprocessing.Process(target=worker, args=(port,))
#         jobs.append(p)
#         p.start()