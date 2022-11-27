from PyQt6 import uic, QtWidgets, QtGui
import sys
import caminhos as cm
from database import ControlBase
from datetime import date, datetime


class RenderApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(RenderApp, self).__init__()
        uic.loadUi(cm.MODULO_CADASTRO, self)
        self.findCampos()  # localiza os campos (label, label edit)
        self.findButtons()  # Localiza os botoes da aplicação
        self.controle()  # Controle que inicia alguma funcão ao iniciar o app
        self.eventoButtons()
        self.show()

    def findCampos(self):  # Localizar os Botoes disponivel na tela
        self.codigo = self.findChild(QtWidgets.QLineEdit, 'codigo_input')
        self.dt_cadastro = self.findChild(
            QtWidgets.QDateEdit, 'dt_cadastro_input')
        self.nome_cliente = self.findChild(QtWidgets.QLineEdit, 'nome_input')
        self.dt_ani = self.findChild(QtWidgets.QDateEdit, 'data_input')
        self.bairro = self.findChild(QtWidgets.QLineEdit, 'bairro_input')
        self.cep = self.findChild(QtWidgets.QLineEdit, 'cep_input')
        self.celular = self.findChild(QtWidgets.QLineEdit, 'celular_input')
        self.endereco = self.findChild(QtWidgets.QLineEdit, 'endereco_input')
        self.numero = self.findChild(QtWidgets.QLineEdit, 'numero_input')
        self.email = self.findChild(QtWidgets.QLineEdit, 'email_input')
        self.obs_cliente = self.findChild(QtWidgets.QTextEdit, 'obs_cli_input')
        self.st_cadastro = self.findChild(QtWidgets.QLabel, 'st_att')
        self.cidade = self.findChild(QtWidgets.QLineEdit, 'cidade_input')
        self.estado = self.findChild(QtWidgets.QLineEdit, 'estado_input')

    def findButtons(self):
        self.salvar = self.findChild(QtWidgets.QPushButton, 'salvar')
        self.cancelar = self.findChild(QtWidgets.QPushButton, 'cancelar')
        self.novo_cadastro = self.findChild(
            QtWidgets.QPushButton, 'novo_cadastro')
        self.excluir = self.findChild(QtWidgets.QPushButton, 'excluir')
        self.atualizar = self.findChild(QtWidgets.QPushButton, 'atualizar')
        self.exibir_cadastro = self.findChild(
            QtGui.QAction, 'exibir_cadastros')
        self.tela_cadastro = self.findChild(QtGui.QAction, 'actionCadastros')
        self.frame_cadastro = self.findChild(QtWidgets.QFrame, 'frameCadastro')
        self.table_cadastro = self.findChild(
            QtWidgets.QTableWidget, 'lista_cadastro')
        self.consulta_cep = self.findChild(
            QtWidgets.QPushButton, 'consultar_cep')

    def controle(self):  # chama o campo codigo, para validar no eventoButton
        self.frame_cadastro.close()
        self.excluir.close()
        self.atualizar.close()
        self.codigo.setReadOnly(False)
        # Setar a data de hoje ao iniciar o app
        self.dt_cadastro.setDate(date.today())
        self.dt_ani.setDate(date.today())

    def campoLido(self):
        self.codigo_lido = self.codigo.text()
        self.dt_cadastro_li = self.dt_cadastro.text()
        self.nome_cli_lido = self.nome_cliente.text()
        self.dt_ani_lido = self.dt_ani.text()
        self.bairro_lido = self.bairro.text()
        self.cep_lido = self.cep.text()
        self.celular_lido = self.celular.text()
        self.endereco_lido = self.endereco.text()
        self.numero_lido = self.numero.text()
        self.email_lido = self.email.text()
        self.obs_cliente_l = self.obs_cliente.toPlainText()
        self.cidade_lido = self.cidade.text()
        self.estado_lido = self.estado.text()

    def cadastroCliente(self):
        self.campoLido()  # iniciar
        if ControlBase().existeCadastro(self.codigo_lido):
            self.inserirCadastro()
        elif ControlBase().retornaCadastro(self.codigo_lido)[1]:
            self.codigo.setReadOnly(True)
            self.puxarCadastro()
            self.excluir.show()
            self.atualizar.show()

    def inserirCadastro(self):
        ControlBase().inserirCadastro(self.codigo_lido, self.dt_cadastro_li, self.nome_cli_lido, self.dt_ani_lido, self.bairro_lido, self.cep_lido,
                                      self.endereco_lido, self.numero_lido, self.email_lido, self.celular_lido, self.obs_cliente_l, self.cidade_lido, self.estado_lido)
        self.st_cadastro.setText('Cadastrado')

    def puxarCadastro(self):
        self.campoLido()
        # ele pega [((dados), True)], pega dados
        self.dados = ControlBase().retornaCadastro(self.codigo_lido)[0][0]
        self.codigo.setText(str(self.dados[0]))
        self.dt_cadastro_li = self.dt_cadastro.setDate(
            datetime.strptime(self.dados[1], '%d/%m/%Y').date())
        self.nome_cli_lido = self.nome_cliente.setText(str(self.dados[2]))
        self.dt_ani_lido = self.dt_ani.setDate(
            datetime.strptime(self.dados[3], '%d/%m/%Y').date())
        self.bairro_lido = self.bairro.setText(str(self.dados[4]))
        self.cep_lido = self.cep.setText(str(self.dados[5]))
        self.celular_lido = self.celular.setText(str(self.dados[9]))
        self.endereco_lido = self.endereco.setText(str(self.dados[6]))
        self.numero_lido = self.numero.setText(str(self.dados[7]))
        self.email_lido = self.email.setText(str(self.dados[8]))
        self.obs_cliente_l = self.obs_cliente.setPlainText(str(self.dados[10]))
        self.cidade_lido = self.cidade.setText(str(self.dados[11]))
        self.estado_lido = self.estado.setText(str(self.dados[12]))

    def novoCadastro(self):
        self.codigo.clear()
        self.nome_cliente.clear()
        self.celular.clear()
        self.bairro.clear()
        self.cep.clear()
        self.endereco.clear()
        self.email.clear()
        self.obs_cliente.clear()
        self.st_cadastro.clear()
        self.numero.clear()
        self.cidade.clear()
        self.estado.clear()
        self.dt_cadastro.setDate(date.today())
        self.dt_ani.setDate(date.today())
        self.controle()

    def atuliazarCadastros(self):
        self.campoLido()
        dados = ControlBase().atualizarCadastro(self.codigo_lido, self.dt_cadastro_li, self.nome_cli_lido, self.dt_ani_lido, self.bairro_lido, self.cep_lido,
                                                self.endereco_lido, self.numero_lido, self.email_lido, self.celular_lido, self.obs_cliente_l, self.cidade_lido, self.estado_lido)
        self.st_cadastro.setText('Atualizado')

    def excluirCadatros(self):
        self.campoLido()
        if ControlBase().existeCadastro(self.codigo_lido) == False:
            ControlBase().excluirCadastro(self.codigo_lido)
            self.st_cadastro.setText('Excluido')
            self.novoCadastro()
        else:
            self.st_cadastro.setText('Não Existe')

    def menu(self):
        cadastros = ControlBase().exibircadastro()
        self.frame_cadastro.show()
        self.table_cadastro.setRowCount(len(cadastros))
        for qntCadastro in range(0, len(cadastros)):
            for qtnInfoCadastro in range(0, len(cadastros[qntCadastro])):
                if qtnInfoCadastro < 10:
                    self.table_cadastro.setItem(
                        qntCadastro, qtnInfoCadastro, QtWidgets.QTableWidgetItem(str(cadastros[qntCadastro][qtnInfoCadastro])))
                elif qtnInfoCadastro > 10:
                    self.table_cadastro.setItem(
                        qntCadastro, qtnInfoCadastro-1, QtWidgets.QTableWidgetItem(str(cadastros[qntCadastro][qtnInfoCadastro])))

    def telaCadastro(self):
        self.frame_cadastro.close()

    def consulatrCep(self):
        import re
        import requests
        self.campoLido()
        cep = re.sub('[^0-9]', '', self.cep_lido)  # 85000-000 para 85000000
        reques = requests.get(f'https://viacep.com.br/ws/{cep}/json/').json()
        self.bairro_lido = self.bairro.setText(reques['bairro'])
        self.cep_lido = self.cep.setText(reques['cep'])
        self.endereco_lido = self.endereco.setText(reques['logradouro'])
        self.cidade_lido = self.cidade.setText(reques['localidade'])
        self.estado_lido = self.estado.setText(reques['uf'])

    def eventoButtons(self):
        # cadastrar o usuario
        self.salvar.clicked.connect(self.cadastroCliente)
        self.atualizar.clicked.connect(self.atuliazarCadastros)
        self.cancelar.clicked.connect(self.novoCadastro)
        self.novo_cadastro.clicked.connect(self.novoCadastro)
        self.excluir.clicked.connect(self.excluirCadatros)
        self.exibir_cadastro.triggered.connect(self.menu)
        self.tela_cadastro.triggered.connect(self.telaCadastro)
        self.consulta_cep.clicked.connect(self.consulatrCep)


app = QtWidgets.QApplication(sys.argv)
janela = RenderApp()
app.exec()
