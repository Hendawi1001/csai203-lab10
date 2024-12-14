import unittest
from app import app, tasks, add_task, get_tasks

class TestToDoApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
        tasks.clear()  

    def test_add_task_function(self):
        add_task("Hello world")
        self.assertIn("Hello world", get_tasks())

    def test_get_tasks_function(self):
        add_task("Abdalrahman")
        self.assertEqual(get_tasks(), ["Abdalrahman"])

    def test_add_task_route(self):
        response = self.app.post('/add-task', data={'task': 'im good'})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'im good', response.data)

if __name__ == '__main__':
    unittest.main()
