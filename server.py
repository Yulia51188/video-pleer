from livereload import Server, shell


server = Server()

server.watch('index.html', shell('make html', cwd='.'))

server.serve(root='.')
