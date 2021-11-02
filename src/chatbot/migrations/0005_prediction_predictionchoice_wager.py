# Generated by Django 3.2.8 on 2021-11-02 21:10

import chatbot.model_mixins
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("chatbot", "0004_alter_gamuser_discord_id"),
    ]

    operations = [
        migrations.CreateModel(
            name="Prediction",
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
                ("prediction_text", models.TextField()),
                ("thread_id", models.BigIntegerField(null=True)),
                ("open", models.BooleanField(default=True)),
            ],
            bases=(models.Model, chatbot.model_mixins.AsyncModelMixin),
        ),
        migrations.CreateModel(
            name="PredictionChoice",
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
                ("choice", models.TextField()),
                (
                    "prediction",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="chatbot.prediction",
                    ),
                ),
            ],
            bases=(models.Model, chatbot.model_mixins.AsyncModelMixin),
        ),
        migrations.CreateModel(
            name="Wager",
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
                ("amount", models.IntegerField()),
                (
                    "bettor",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="chatbot.gamuser",
                    ),
                ),
                (
                    "choice",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="chatbot.predictionchoice",
                    ),
                ),
            ],
            bases=(models.Model, chatbot.model_mixins.AsyncModelMixin),
        ),
    ]
