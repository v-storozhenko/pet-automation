"""
Пример нагрузочного тестирования.

Для запуска:
- locust -f main.py
- открываем веб-интерфейс (по дефолту) http://localhost:8089
"""

from locust import HttpUser, task, between


class WebsiteUser(HttpUser):
    """
    Клас-пример для нагрузочного тестирования.
    """
    host = "https://www.google.com/"  # Указываем адрес API
    wait_time = between(1, 3)  # Пауза между запросами

    @task
    def get_main(self):
        """Пример метода-задачи."""
        self.client.get("/")
