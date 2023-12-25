from django.test import TestCase
from django.utils import timezone
from django.utils.text import slugify

# Create your tests here.
from .models import Video


class VideoModelTestCase(TestCase):
    def setUp(self):
        self.objA = Video.objects.create(title="This is my title", video_id="abs")
        self.objB = Video.objects.create(title="This is my title", state=Video.VideoStateOptions.PUBLISH,
                                         video_id="abd")

    def test_slug_field(self):
        title = self.objA.title
        test_slug = slugify(title)
        self.assertEqual(test_slug, self.objA.slug)

    def test_valid_title(self):
        title = "This is my title"
        qs = Video.objects.filter(title=title)
        self.assertTrue(qs.exists())

    def test_created_count(self):
        qs = Video.objects.all()
        self.assertEqual(qs.count(), 2)

    def test_draft_case(self):
        qs = Video.objects.filter(state=Video.VideoStateOptions.DRAFT)
        self.assertEqual(qs.count(), 1)

    def test_publish_case(self):
        now = timezone.now()
        publish_qs = Video.objects.filter(state=Video.VideoStateOptions.PUBLISH, publish_timestamp__lte=now)
        self.assertTrue(publish_qs.exists())

    def test_publish_manager(self):
        published_qs = Video.Objects.all().published()
        self.assertTrue(published_qs.exists())
