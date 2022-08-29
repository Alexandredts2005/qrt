#!/usr/bin/python3

# Serveur web en python
# https://www.afternerd.com/blog/python-http-server/

import http.server
import socketserver

# Définition du port
PORT = 8080
# Définition du serveur gestionnaire de requetes
Handler = http.server.SimpleHTTPRequestHandler
httpd = socketserver.TCPServer(("", PORT), Handler)
# Création de l'instance serveur sur le port defini
print("Serveur opérationnel sur le port : ", PORT)
# Start server
httpd.serve_forever()
