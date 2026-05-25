# HEXG/server.py
# Этот файл просто перенаправляет запуск в настоящий nouz_mcp

import sys
import asyncio

def main():
    try:
        # Импортируем функцию запуска из оригинального пакета
        from nouz_mcp.server import run_server
        
        # Запускаем асинхронный сервер
        asyncio.run(run_server())
        
    except ImportError:
        print("❌ Ошибка: пакет 'nouz-mcp' не установлен.")
        print("Выполни: pip install nouz-mcp")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Ошибка запуска: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()