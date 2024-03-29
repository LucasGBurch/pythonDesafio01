# SEÇÃO DOS MÉTODOS

# Adicionar Contatos
def add_contact(contacts, contact_name, contact_phone, contact_email):
  contact = {"Nome": contact_name, "Telefone": contact_phone, "E-mail": contact_email, "Favorito": False}
  contacts.append(contact)
  print(f"\nContato {contact_name} foi adicionado com sucesso!")
  return

# Visualizar Contatos
def list_contacts(contacts):
  if len(contacts) > 0:
    for index, contact in enumerate(contacts, start=1):
      contact_name = contact["Nome"]
      contact_phone = contact["Telefone"]
      contact_email = contact["E-mail"]
      favorite = "Sim" if contact["Favorito"] else "Não"
      print(f"{index} - Nome: {contact_name} - Telefone: {contact_phone} - E-mail: {contact_email} - Favorito: {favorite}")
    return True
  else:
    print("Não há contatos na agenda. Tente adicionar novos.")
    return False

# Editar Contatos
def edit_contacts(contacts, contact_number):
  contact_index = int(contact_number) - 1

  if contact_index >= 0 and contact_index < len(contacts): 
    edit = input("Digite o que você gostaria de editar\nNome, Telefone ou E-mail: ")
    if edit == "Nome" or edit == "Telefone" or edit == "E-mail":
      change = input(f"Digite o novo {edit}: ")
      contacts[contact_index][edit] = change
      print(f"{edit} do contato modificado para {change}.")
      return
    else:
      print("Atributo inválido.")
  else:
    print("Você deve escolher um número existente na lista.")
  return # Caso não haja contatos, só virá a mensagem do list_contacts

# Marcar/Desmarcar Favorito
def mark_unmark_favorite(contacts, contact_number):
  contact_index = int(contact_number) - 1

  if contact_index >= 0 and contact_index < len(contacts):
    print(f"{contacts[contact_index]["Favorito"]}")
    if contacts[contact_index]["Favorito"]:
      contacts[contact_index]["Favorito"] = False
    else:
      contacts[contact_index]["Favorito"] = True
    print(f"Status de Favorito modificado para {contacts[contact_index]["Favorito"]}")
  else:
    print("Você deve escolher um número existente na lista. Tente novamente.")
  return

# Listar Contatos Favoritos
def list_favorite_contacts(contacts):
  favorite_contacts = []
  print("Contatos Favoritos:")
  for index, contact in enumerate(contacts, start=1):
    if contact["Favorito"]:
      favorite_contacts.append(contact)
      contact_name = contact["Nome"]
      contact_phone = contact["Telefone"]
      contact_email = contact["E-mail"]
      print(f"{index} - Nome: {contact_name} - Telefone: {contact_phone} - E-mail: {contact_email}")
  if len(favorite_contacts) == 0:
    print("Não há contatos favoritos. Tente marcar algum na opção anterior!")
  return

# Deletar Contatos Existentes
def delete_contact(contacts, contact_number):
  contact_index = int(contact_number) - 1

  if contact_index >= 0 and contact_index < len(contacts):
    print(f"Contato {contacts[contact_index]["Nome"]} deletado com sucesso.")
    contacts.pop(contact_index)
  else:
    print("Você deve escolher um número existente na lista.")
  return
# ------------------------------------------------------
# SEÇÃO DE EXECUÇÃO DA AGENDA:

contacts = []

while True:
  print("\nBem-vindo à agenda Python! Suas opções:")
  print("1. Adicionar contato")
  print("2. Visualizar contatos cadastrados")
  print("3. Editar um contato")
  print("4. Marcar ou desmarcar contato como favorito")
  print("5. Visualizar contatos favoritos")
  print("6. Deletar um contato")
  print("7. Encerrar agenda")

  choosen_option = input("Digite o número da opção: ")

  if choosen_option == '1':
    contact_name = input("Digite o nome do contato: ")
    contact_phone = input("Digite o número de telefone do contato: ")
    contact_email = input("Digite o e-mail do contato: ")
    add_contact(contacts, contact_name, contact_phone, contact_email)
  elif choosen_option == '2':
    list_contacts(contacts)
  elif choosen_option == '3':
    if list_contacts(contacts): # Já chama a lista e, se não tiver, retorna Falso com o aviso da lista vazia
      contact_number = input("Digite o número do contato na lista que você quer Editar: ")
      edit_contacts(contacts, contact_number)
  elif choosen_option == '4':
    if list_contacts(contacts):
      contact_number = input("Digite o número do contato na lista que você quer (des)favoritar: ")
      mark_unmark_favorite(contacts, contact_number)
  elif choosen_option == '5':
    list_favorite_contacts(contacts)
  elif choosen_option == '6':
    if list_contacts(contacts):
      contact_number = input("Digite o número do contato na lista que você quer Deletar: ")
      delete_contact(contacts, contact_number)
  elif choosen_option == '7':
    print("Agenda encerrada. Até a próxima! o/")
    break
  else:
    print("Opção inválida. Tente novamente.")
