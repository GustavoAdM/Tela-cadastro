import sqlite3 as sq
import caminhos as cm


class ControlBase():
    def __init__(self) -> None:
        self.banco = sq.connect(cm.CAMINHO_BASE)
        self.cursor = self.banco.cursor()

    def inserirCadastro(self, codigo, dt_cadastro, nome_cliente, dt_aniversario, bairro, cep, endereco='', numero='', email='', celular='', obs_cliente='', cidade='', estado=''):  # Inserir dados na tabela
        self.cursor.execute(
            f'INSERT INTO Pessoa (id, data_cadastro, nome_cliente, data_aniversario, bairro, cep, endereco, numero, email, celular, obs_cliente, cidade, estado) VALUES ("{codigo}", "{dt_cadastro}", "{nome_cliente}", "{dt_aniversario}", "{bairro}", "{cep}", "{endereco}", "{numero}", "{email}", "{celular}", "{obs_cliente}", "{cidade}", "{estado}")')
        self.banco.commit()

    def atualizarCadastro(self, codigo, dt_cadastro, nome_cliente, dt_aniversario, bairro, cep, endereco, numero, email, celular, obs_cliente, cidade, estado):
        self.cursor.execute(f'UPDATE Pessoa SET data_cadastro = ?, nome_cliente = ?, data_aniversario = ?, bairro = ?, cep = ?, endereco = ?, numero = ?, email = ?, celular = ?, obs_cliente = ?, cidade = ?, estado = ? WHERE id = {codigo}',
                            (dt_cadastro, nome_cliente, dt_aniversario, bairro, cep, endereco, numero, email, celular, obs_cliente, cidade, estado))
        self.banco.commit()

    def buscarCadastro(self, codigo):
        busca = self.cursor.execute(
            f'SELECT * FROM Pessoa p WHERE p.id = "{codigo}"')
        busca.fetchall()

    def existeCadastro(self, id=0):
        id.replace(' ', '')
        if id != '' and id != 0 and id.isdigit():
            busca = self.cursor.execute(
                f'''SELECT * FROM Pessoa p WHERE p.id = {int(id)}''').fetchall()
            if len(busca) == 0:
                return True  # retorna verdadeira, para poder cadastrar
            else:
                return False  # para não poder cadastrar

    def retornaCadastro(self, id=0):
        id.replace(' ', '')
        if id != '' and id != 0 and id.isdigit():
            busca = self.cursor.execute(
                f'''SELECT * FROM Pessoa p WHERE p.id = {id}''').fetchall()
            return busca, True
        else:
            return False, False

    def excluirCadastro(self, id=0):
        id.replace(' ', '')
        if id != '' and id != 0 and id.isdigit():
            busca = self.cursor.execute(
                f'''DELETE FROM Pessoa  WHERE id = {int(id)}''').fetchall()
            self.banco.commit()

    def exibircadastro(self):
        busca = self.cursor.execute('''SELECT * FROM Pessoa''')
        return busca.fetchall()
