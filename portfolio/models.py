from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, help_text="URL-friendly version of the title (auto-generate if unsure)")
    description = models.TextField(help_text="Short summary shown on the projects page")
    tech_stack = models.CharField(max_length=300, help_text="Comma-separated, e.g. Python, Django, PostgreSQL")
    image = models.ImageField(upload_to='projects/', blank=True, null=True)
    github_url = models.URLField(blank=True, null=True)
    live_url = models.URLField(blank=True, null=True)
    featured = models.BooleanField(default=False, help_text="Show this project prominently")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']  # newest first

    def __str__(self):
        return self.title

    def tech_list(self):
        """Splits comma-separated tech_stack into a clean list for the template."""
        return [tech.strip() for tech in self.tech_stack.split(',') if tech.strip()]