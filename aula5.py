import sqlite3
class agendadb:
    def __init__(self, arquivo):
        self.conn = sqlite3.connect(arquivo)
        self.cursor = self.conn.cursor()

    def inserir(self, nome, telefone):
        consulta = 'INSERT INTO agenda (nome, telefone) VALUES (?, ? )'
        self.cursor.execute(consulta, (nome, telefone))
        self.conn.commit()

    def editar(self, id, nome, telefone):
        consulta = 'UPDATE OR IGNORE agenda SET nome=?, telefone=? WHERE id=?'
        self.cursor.execute(consulta, (nome, telefone, id))
        self.conn.commit()

    def excluir(self, id):
        consulta = 'DELETE FROM agenda WHERE id=?'
        self.cursor.execute(consulta, (id,))
        self.conn.commit()

    def listar(self):
        self.cursor.execute('SELECT *FROM agenda')
        for linha in self.cursor.fetchall():
            print(linha)

    def fechar(self):
        self.cursor.close()
        self.conn.close()

    def buscar(self, valor):

     if __name__ == '__main__':
      agenda = agendadb('agenda.db')
     #agenda.inserir('silva', '71992138874')
      agenda.editar()