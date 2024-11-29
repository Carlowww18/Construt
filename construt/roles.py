from rolepermissions.roles import AbstractUserRole

class Gerente(AbstractUserRole):
    available_permissions = {
        'cadastrar_produtos': True,
        'liberar_descontos': True,
        'cadastrar_vendedor': True,
    }

class vendedor(AbstractUserRole):
    available_permissions = {
        'realizar_venda': True,
    }