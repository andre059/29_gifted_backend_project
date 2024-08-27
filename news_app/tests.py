from datetime import datetime
import os
import shutil
from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from django.contrib.admin.sites import AdminSite
from django.core.exceptions import ValidationError
from django.db.utils import IntegrityError
from .models import News, NewsImage
from .admin import NewsAdmin

class MockRequest:
    pass

class NewsAppTest(TestCase):

    def setUp(self):
        self.site = AdminSite()
        self.news_admin = NewsAdmin(News, self.site)
        self.news = News.objects.create(
            created_at=datetime.now(),
            title="Test News",
            content="This is a test content.",
            short_description="Short description",
            video="https://example.com/video"
        )

    def test_news_creation(self):
        """Тестирование создания новости и проверка полей"""
        self.assertEqual(self.news.title, "Test News")
        self.assertEqual(self.news.content, "This is a test content.")
        self.assertEqual(self.news.short_description, "Short description")
        self.assertEqual(self.news.video, "https://example.com/video")

    def test_news_image_creation_and_deletion(self):
        """Тестирование создания и удаления изображения для новости"""
        image = SimpleUploadedFile("test_image.jpg", b"file_content", content_type="image/jpeg")
        news_image = NewsImage.objects.create(news=self.news, image=image)
        self.assertTrue(os.path.exists(news_image.image.path))

        news_image.delete()
        self.assertFalse(os.path.exists(news_image.image.path))

    def test_news_image_creation_and_deletion(self):
        """Тестирование создания и удаления изображения для новости"""
        image = SimpleUploadedFile("test_image.jpg", b"file_content", content_type="image/jpeg")
        news_image = NewsImage.objects.create(news=self.news, image=image)
        self.assertTrue(os.path.exists(news_image.image.path))

        # Удаляем изображение
        news_image.delete()
        self.assertFalse(os.path.exists(news_image.image.path))



    def test_deletion_of_news_without_images(self):
        """Тестирование удаления новости без изображений"""
        # Удаляем новость, которая не имеет связанных изображений
        try:
            self.news.delete()
        except Exception as e:
            self.fail(f"Deletion of news without images raised an exception: {e}")

    def test_news_creation_with_empty_fields(self):
        """Тестирование создания новости с пустыми обязательными полями"""
        with self.assertRaises((IntegrityError, ValidationError)):
            News.objects.create(
                created_at=None,
                title="",
                content="",
                short_description="",
                video=""
            )
