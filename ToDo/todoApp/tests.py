from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from django.urls import reverse

from .models import Todo


class TodoTests(TestCase):

    def setUp(self):
        self.task = Todo.objects.create(
            title="Learn Django",
            description="Finish CRUD assignment",
            completed=False
        )

    # -------------------
    # Model Test
    # -------------------

    def test_task_creation(self):
        self.assertEqual(Todo.objects.count(), 1)
        self.assertEqual(self.task.title, "Learn Django")
        self.assertFalse(self.task.completed)

    # -------------------
    # List View
    # -------------------

    def test_list_tasks(self):
        response = self.client.get(reverse("home"))

        self.assertEqual(response.status_code, 200)

    # -------------------
    # Create View
    # -------------------

    def test_create_task(self):
        response = self.client.post(
            reverse("home"),
            {
                "title": "New Todo",
                "description": "New Description",
                "completed": False,
            },
        )

        self.assertEqual(response.status_code, 302)
        self.assertEqual(Todo.objects.count(), 2)
        self.assertTrue(Todo.objects.filter(title="New Todo").exists())

    # -------------------
    # Update View
    # -------------------

    def test_update_task(self):
        response = self.client.post(
            reverse("update", args=[self.task.id]),
            {
                "title": "Updated Title",
                "description": "Updated Description",
                "completed": "on",
            },
        )

        self.assertEqual(response.status_code, 302)

        self.task.refresh_from_db()

        self.assertEqual(self.task.title, "Updated Title")
        self.assertEqual(self.task.description, "Updated Description")
        self.assertTrue(self.task.completed)

    # -------------------
    # Delete View
    # -------------------

    def test_delete_task(self):
        response = self.client.post(
            reverse("delete", args=[self.task.id])
        )

        self.assertEqual(response.status_code, 302)
        self.assertEqual(Todo.objects.count(), 0)
    
