from netmiko import ConnectHandler

# Informations du routeur
device = {
    'device_type': 'cisco_ios',
    'host': '192.168.56.1',
    'username': 'admin',
    'password': 'admin123',
    'secret': 'enablepass'  # Mot de passe enable
}

try:
    # Connexion au routeur
    net_connect = ConnectHandler(**device)
    net_connect.enable()
    print("[INFO] Connexion établie avec le routeur.")

    # 1. Récupérer la liste des interfaces
    interfaces = net_connect.send_command("show ip interface brief")
    with open("interfaces.txt", "w") as f:
        f.write(interfaces)
    print("[INFO] Liste des interfaces sauvegardée dans interfaces.txt")

    # 2. Lire les commandes depuis le fichier
    with open("commands.txt") as f:
        commands = f.read().splitlines()

    # 3. Envoyer les commandes
    config_output = net_connect.send_config_set(commands)
    print("[INFO] Configuration appliquée :")
    print(config_output)

    # Sauvegarder la configuration
    net_connect.save_config()
    print("[INFO] Configuration sauvegardée sur le routeur.")

except Exception as e:
    print(f"[ERREUR] Une erreur est survenue : {e}")

finally:
    # Déconnexion
    net_connect.disconnect()
    print("[INFO] Déconnexion terminée.")