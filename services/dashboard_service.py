from database import Database

class DashboardService:
    def __init__(self):
        self.db = Database()

    def obter_estatisticas(self):
        conn = self.db.connect()
        cursor = conn.cursor()
        
        cursor.execute("SELECT COUNT(*) FROM funcionarios")
        total_funcionarios = cursor.fetchone()[0]
        
        cursor.execute("SELECT COUNT(*) FROM departamentos")
        total_departamentos = cursor.fetchone()[0]
        
        cursor.execute("SELECT COUNT(*) FROM cargos")
        total_cargos = cursor.fetchone()[0]
        
        cursor.close()
        return {
            "total_funcionarios": total_funcionarios,
            "total_departamentos": total_departamentos,
            "total_cargos": total_cargos
        }
