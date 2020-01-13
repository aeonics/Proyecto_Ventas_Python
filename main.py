clients = 'pablo, ricardo, '

#Crear CLientes
def create_client(client_name):
    global clients #variable global y s epuede usar dentro de la funcion
    if client_name not in clients:
        clients += client_name
        _add_comma()
    else:
        _not_in_list()

#Listar clientes
def list_clients():
    global clients
    print (clients)

#Actualizar el cliente
def update_client(client_name, updated_client_name):
    global clients

    if client_name in clients:
        clients = clients.replace(client_name + ', ', updated_client_name + ', ')
    else:
        _not_in_list()

#Borrar cliente
def delete_client(client_name):
    global clients

    if client_name in clients:
        clients = clients.replace(client_name + ', ', '')
    else:
        _not_in_list()

#Añadir una coma
def _add_comma():
    global clients
    clients += ','

#Pantalla de menu
def _print_welcome():
    print('WELCOME TO SALES')
    print('*'*50)
    print('What would like to do? ')
    print('[C]reate client')
    print('[D]elete client')
    print('[U]pdate client')

#Obtener el nombre del cliente
def _get_client_name():
    return input('What\'s client name: ')

#mensajes sin interaccion
def _not_in_list():
    print('Client not in list')

#Main
if __name__ == "__main__":
    _print_welcome()
#Pedir al usuario opcion
    command = input('')
    if command.lower() == 'c':
        client_name = _get_client_name()
        create_client(client_name)
        list_clients()
    elif command.lower() == 'd':
        client_name = _get_client_name()
        delete_client(client_name)
        list_clients()
    elif  command.lower() == 'u':
        client_name = _get_client_name()
        updated_client_name = input('What\'s the updated client name==> ')
        update_client(client_name, updated_client_name)
        list_clients()
    else:
        print('Invalid command!! ')
