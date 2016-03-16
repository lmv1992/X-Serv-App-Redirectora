#!/usr/bin/python

import webapp
import random

class redirectora (webapp.webApp):
#primero el fichero y luego la clase dentro del fichero
    def process(self, parsedRequest):
        numero = random.randint(1,10000000)
        htmlCode = '300 Found'
        htmlBody = '<html><body><head>Redirigido a: /localhost:1234/'
        htmlBody += str(numero) + '<meta http-equiv="refresh"'
        htmlBody += 'content="3; url=' + str(numero) + '" />'
        return (htmlCode,htmlBody)

if __name__ == "__main__":
    testWebApp = redirectora("localhost", 1234)
