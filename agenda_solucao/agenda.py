# SEÇÃO DOS MÉTODOS
def add_contact(contacts, contact_name, contact_phone, contact_email):
  contact = {"Nome": contact_name, "Telefone": contact_phone, "E-mail": contact_email, "Favorite": False}
  contacts.append(contact)
  print(f"\nContato {contact_name} foi adicionado com sucesso!")
  return

def list_contacts(contacts):
  if len(contacts) > 0:
    for indice, contact in enumerate(contacts, start=1):
      contact_name = contact["Nome"]
      contact_phone = contact["Telefone"]
      contact_email = contact["E-mail"]
      favorite = "Sim" if contact["Favorite"] else "Não"
      print(f"{indice} - Nome: {contact_name} - Telefone: {contact_phone} - E-mail: {contact_email} - Favorito: {favorite}")
    return True
  else:
    print("Não há contatos na agenda. Tente adicionar novos.")
    return False

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
    if list_contacts(contacts):
      contact_number = input("Digite o número do contato na lista: ")
      edit_contacts(contacts, contact_number)
  elif choosen_option == '4':
    print(f"Opção {choosen_option} escolhida.")
  elif choosen_option == '5':
    print(f"Opção {choosen_option} escolhida.")
  elif choosen_option == '6':
    print(f"Opção {choosen_option} escolhida.")
  elif choosen_option == '7':
    print("Agenda encerrada. Até a próxima! o/")
    break
  else:
    print("Opção inválida. Tente novamente.")
