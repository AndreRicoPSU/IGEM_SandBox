# Generated by Django 4.1.5 on 2023-03-20 19:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Connector",
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
                ("connector", models.CharField(max_length=20, unique=True)),
                ("description", models.CharField(default="", max_length=200)),
                (
                    "update_ds",
                    models.BooleanField(default=True, verbose_name="Activate"),
                ),
                ("source_path", models.CharField(default="", max_length=300)),
                (
                    "source_web",
                    models.BooleanField(
                        default=True, verbose_name="Source path from Internet"
                    ),
                ),
                ("source_compact", models.BooleanField(default=False)),
                ("source_file_name", models.CharField(max_length=200)),
                ("source_file_format", models.CharField(max_length=200)),
                ("source_file_sep", models.CharField(default=",", max_length=3)),
                ("source_file_skiprow", models.IntegerField(default=0)),
                ("target_file_name", models.CharField(max_length=200)),
                ("target_file_format", models.CharField(max_length=200)),
                (
                    "target_file_keep",
                    models.BooleanField(default=False, verbose_name="Keep file"),
                ),
            ],
            options={
                "verbose_name_plural": "Connector",
            },
        ),
        migrations.CreateModel(
            name="Datasource",
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
                ("datasource", models.CharField(max_length=20, unique=True)),
                ("description", models.CharField(max_length=200)),
                ("category", models.CharField(max_length=20)),
                ("website", models.CharField(max_length=200)),
            ],
            options={
                "verbose_name_plural": "Datasource",
            },
        ),
        migrations.CreateModel(
            name="LogsCollector",
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
                ("source_file_name", models.CharField(max_length=200)),
                ("date", models.DateTimeField(blank=True, default="")),
                ("connector", models.CharField(max_length=200)),
                ("datasource", models.CharField(max_length=200)),
                ("version", models.CharField(max_length=200)),
                ("status", models.BooleanField(default=True)),
                ("size", models.IntegerField(default=0)),
            ],
            options={
                "verbose_name_plural": "Process Log",
            },
        ),
        migrations.CreateModel(
            name="PrefixOpc",
            fields=[
                (
                    "pre_value",
                    models.CharField(
                        max_length=5,
                        primary_key=True,
                        serialize=False,
                        verbose_name="Value Prefix",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Term - Prefix",
            },
        ),
        migrations.CreateModel(
            name="Term",
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
                ("term", models.CharField(max_length=40, unique=True)),
                ("description", models.CharField(max_length=400)),
            ],
            options={
                "verbose_name_plural": "Term",
            },
        ),
        migrations.CreateModel(
            name="TermCategory",
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
                ("term_category", models.CharField(max_length=20, unique=True)),
                ("description", models.CharField(max_length=200)),
            ],
            options={
                "verbose_name_plural": "Term - Category",
            },
        ),
        migrations.CreateModel(
            name="TermGroup",
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
                ("term_group", models.CharField(max_length=20, unique=True)),
                ("description", models.CharField(max_length=200)),
            ],
            options={
                "verbose_name_plural": "Term - Group",
            },
        ),
        migrations.CreateModel(
            name="WordTerm",
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
                ("word", models.CharField(max_length=400, unique=True)),
                ("status", models.BooleanField(default=False, verbose_name="Active?")),
                (
                    "commute",
                    models.BooleanField(default=False, verbose_name="Commute?"),
                ),
                (
                    "term",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="ge.term"
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Word to Terms",
            },
        ),
        migrations.CreateModel(
            name="WordMap",
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
                ("cword", models.CharField(max_length=15, unique=True)),
                ("word_1", models.CharField(max_length=100)),
                ("word_2", models.CharField(max_length=100)),
                ("qtd_links", models.IntegerField(default=0)),
                (
                    "connector",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="ge.connector"
                    ),
                ),
                (
                    "datasource",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="ge.datasource"
                    ),
                ),
                (
                    "term_1",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="term_wordmap_1",
                        to="ge.term",
                    ),
                ),
                (
                    "term_2",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="term_wordmap_2",
                        to="ge.term",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Word Map",
            },
        ),
        migrations.CreateModel(
            name="WFControl",
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
                    "last_update",
                    models.DateTimeField(verbose_name="Last Update Connector"),
                ),
                ("source_file_version", models.CharField(max_length=500)),
                ("source_file_size", models.BigIntegerField(default=0)),
                ("target_file_size", models.BigIntegerField(default=0)),
                (
                    "chk_collect",
                    models.BooleanField(
                        default=False, verbose_name="Collect Processed"
                    ),
                ),
                (
                    "chk_prepare",
                    models.BooleanField(
                        default=False, verbose_name="Prepare Processed"
                    ),
                ),
                (
                    "chk_map",
                    models.BooleanField(default=False, verbose_name="Map Processed"),
                ),
                (
                    "chk_reduce",
                    models.BooleanField(default=False, verbose_name="Reduce Processed"),
                ),
                (
                    "connector",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="ge.connector"
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Workflow",
            },
        ),
        migrations.CreateModel(
            name="TermMap",
            fields=[
                (
                    "ckey",
                    models.CharField(max_length=15, primary_key=True, serialize=False),
                ),
                ("qtd_links", models.IntegerField(default=0)),
                (
                    "connector",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="ge.connector"
                    ),
                ),
                (
                    "term_1",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="term_termmap_1",
                        to="ge.term",
                    ),
                ),
                (
                    "term_2",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="term_termmap_2",
                        to="ge.term",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Terms Map",
            },
        ),
        migrations.CreateModel(
            name="TermHierarchy",
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
                    "term",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="key_child",
                        to="ge.term",
                        verbose_name="Term ID",
                    ),
                ),
                (
                    "term_parent",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="key_parent",
                        to="ge.term",
                        verbose_name="Term Parent ID",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Term - Hierarchy",
            },
        ),
        migrations.AddField(
            model_name="term",
            name="term_category",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="ge.termcategory"
            ),
        ),
        migrations.AddField(
            model_name="term",
            name="term_group",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="ge.termgroup"
            ),
        ),
        migrations.CreateModel(
            name="DSTColumn",
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
                ("status", models.BooleanField(default=False, verbose_name="Active?")),
                (
                    "column_number",
                    models.IntegerField(default=0, verbose_name="Column Sequence"),
                ),
                (
                    "column_name",
                    models.CharField(
                        blank=True, max_length=40, verbose_name="Column Name"
                    ),
                ),
                (
                    "single_word",
                    models.BooleanField(default=False, verbose_name="Single Word"),
                ),
                (
                    "connector",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="ge.connector"
                    ),
                ),
                (
                    "pre_value",
                    models.ForeignKey(
                        default="None",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="ge.prefixopc",
                        verbose_name="Prefix",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Connector - Fields",
            },
        ),
        migrations.AddField(
            model_name="connector",
            name="datasource",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="ge.datasource"
            ),
        ),
        migrations.AddIndex(
            model_name="wordterm",
            index=models.Index(fields=["term"], name="ge_wordterm_term_id_9bd525_idx"),
        ),
    ]