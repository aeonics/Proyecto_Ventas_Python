import sys #sys.exit perimte terminar la ejecución del script devolviendo un valor (en Unix/Linux esto se considera una muy buena práctica ya que permite encadenar comandos en función de si terminaron bien, retornando 0 o si tuvieron aglún problema, un valor diferente a 0).

clients =['pablo', 'ricardo']

#Crear CLientes
def create_client(client_name):
    global clients #variable global y s epuede usar dentro de la funcion
    if client_name not in clients:
        clients.append(client_name)
        
    else:
        _not_in_list()

#Listar clientes
def list_clients():
    
    for idx, client in enumerate(clients):#enumeramos la lista pero con indice
        print('{}: {}'.format(idx,client))


#Actualizar el cliente
def update_client(client_name, updated_name):
    global clients

    if client_name in clients:
        index = clients.index(client_name)
        clients[index] = updated_name
    else:
        _not_in_list()

#Borrar cliente
def delete_client(client_name):
    global clients

    if client_name in clients:
        clients.remove(client_name)
    else:
        _not_in_list()


#Encuentra el cliente
def search_client(client_name):
    for client in clients:
        if client != client_name:
            continue
        else:
            return True




#Pantalla de menu
def _print_welcome():
    print('WELCOME TO SALES')
    print('*'*50)
    print('What would like to do? ')
    print('[L]ist clients')
    print('[C]reate client')
    print('[D]elete client')
    print('[U]pdate client')
    print('[S]earch client')

#Obtener el nombre del cliente
def _get_client_name():
    client_name = None
    while not client_name:
        client_name= input ('What\'s client name: ')
        if client_name.lower() == 'exit':
            client_name = None
            break

    if not client_name:
        sys.exit()

    return client_name

#mensajes sin interaccionc
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
    elif command.lower() == 's':
        client_name =_get_client_name()
        found = search_client(client_name)#found es true o false
        if found:
            print('The client is in the client\'s list')
        else:
            print('The client : {}  is not in our client\'s list'.format(client_name))
    elif command.lower() == 'l':
        list_clients()
    else:
        print('Invalid command!! ')
