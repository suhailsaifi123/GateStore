# Generated by Django 5.0.2 on 2025-06-27 00:17

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("pages", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="SiteSettings",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("site_name", models.CharField(default="GateStore", max_length=100)),
                (
                    "logo",
                    models.ImageField(
                        blank=True,
                        help_text="Upload site logo",
                        null=True,
                        upload_to="site/",
                    ),
                ),
                (
                    "logo_alt",
                    models.ImageField(
                        blank=True,
                        help_text="Alternative logo (dark version)",
                        null=True,
                        upload_to="site/",
                    ),
                ),
                (
                    "favicon",
                    models.ImageField(
                        blank=True,
                        help_text="Site favicon",
                        null=True,
                        upload_to="site/",
                    ),
                ),
                (
                    "contact_email",
                    models.EmailField(default="info@gatestore.com", max_length=254),
                ),
                (
                    "contact_phone",
                    models.CharField(default="+919917554540", max_length=20),
                ),
                (
                    "business_hours",
                    models.CharField(default="Mon-Fri: 9AM-6PM IST", max_length=100),
                ),
                ("address", models.TextField(default="Your business address here")),
                ("facebook_url", models.URLField(blank=True, null=True)),
                ("twitter_url", models.URLField(blank=True, null=True)),
                ("instagram_url", models.URLField(blank=True, null=True)),
                ("linkedin_url", models.URLField(blank=True, null=True)),
                (
                    "meta_title",
                    models.CharField(
                        default="GateStore - Premium Gates for Every Home",
                        max_length=60,
                    ),
                ),
                (
                    "meta_description",
                    models.TextField(
                        default="Discover beautiful, secure gates that enhance your property. Preview, customize, and order with confidence."
                    ),
                ),
                (
                    "meta_keywords",
                    models.CharField(
                        default="gates, security gates, iron gates, wooden gates, gate installation",
                        max_length=200,
                    ),
                ),
                ("maintenance_mode", models.BooleanField(default=False)),
                (
                    "maintenance_message",
                    models.TextField(
                        default="Site is under maintenance. Please check back soon."
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
            options={
                "verbose_name": "Site Setting",
                "verbose_name_plural": "Site Settings",
            },
        ),
        migrations.CreateModel(
            name="AdminActivityLog",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "action",
                    models.CharField(
                        choices=[
                            ("logo_change", "Logo Changed"),
                            ("user_approve", "User Approved"),
                            ("user_reject", "User Rejected"),
                            ("settings_update", "Settings Updated"),
                            ("maintenance_toggle", "Maintenance Mode Toggled"),
                        ],
                        max_length=20,
                    ),
                ),
                ("description", models.TextField()),
                ("ip_address", models.GenericIPAddressField(blank=True, null=True)),
                ("user_agent", models.TextField(blank=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "admin_user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="admin_activities",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "Admin Activity Log",
                "verbose_name_plural": "Admin Activity Logs",
                "ordering": ["-created_at"],
            },
        ),
        migrations.CreateModel(
            name="UserApproval",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("is_approved", models.BooleanField(default=False)),
                ("approved_at", models.DateTimeField(blank=True, null=True)),
                ("approval_notes", models.TextField(blank=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "approved_by",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="approved_users",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="approval",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "User Approval",
                "verbose_name_plural": "User Approvals",
            },
        ),
    ]
