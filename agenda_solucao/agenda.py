# SEÇÃO DOS MÉTODOS
def adicionar_contato(contacts, contact_name, contact_phone, contact_email):
  contact = {"Nome": contact_name, "Telefone": contact_phone, "E-mail": contact_email, "Favorite": False}
  contacts.append(contact)
  print(f"\nContato {contact_name} foi adicionado com sucesso!")
  return

def visualizar_contatos(contacts):
  if len(contacts) > 0:
    for indice, contact in enumerate(contacts, start=1):
      contact_name = contact["Nome"]
      contact_phone = contact["Telefone"]
      contact_email = contact["E-mail"]
      favorite = "Sim" if contact["Favorite"] else "Não"
      print(f"{indice} - Nome: {contact_name} - Telefone: {contact_phone} - E-mail: {contact_email} - Favorito: {favorite}")
  else:
    print("Não há contatos na agenda. Tente adicionar novos.")

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
    adicionar_contato(contacts, contact_name, contact_phone, contact_email)
  elif choosen_option == '2':
    visualizar_contatos(contacts)
  elif choosen_option == '3':
    print(f"Opção {choosen_option} escolhida.")
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
