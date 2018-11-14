# Generated by Django 2.1.3 on 2018-11-14 15:26

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import grandchallenge.core.validators


class Migration(migrations.Migration):

    dependencies = [("evaluation", "0018_auto_20181112_1456")]

    operations = [
        migrations.RemoveField(model_name="result", name="absolute_url"),
        migrations.AddField(
            model_name="config",
            name="scoring_method_choice",
            field=models.CharField(
                choices=[
                    ("abs", "Use the absolute value of the score column"),
                    (
                        "avg",
                        "Use the mean of the relative ranks of the score and extra result columns",
                    ),
                    (
                        "med",
                        "Use the median of the relative ranks of the score and extra result columns",
                    ),
                ],
                default="abs",
                help_text="How should the rank of each result be calculated?",
                max_length=3,
            ),
        ),
        migrations.AlterField(
            model_name="config",
            name="extra_results_columns",
            field=django.contrib.postgres.fields.jsonb.JSONField(
                blank=True,
                default=list,
                help_text="A JSON object that contains the extra columns from metrics.json that will be displayed on the results page. ",
                validators=[
                    grandchallenge.core.validators.JSONSchemaValidator(
                        schema={
                            "$id": "http://json-schema.org/draft-06/schema#",
                            "$schema": "http://json-schema.org/draft-06/schema#",
                            "definitions": {},
                            "items": {
                                "$id": "#/items",
                                "additionalProperties": False,
                                "properties": {
                                    "error_path": {
                                        "$id": "#/items/properties/error_path",
                                        "default": "",
                                        "examples": ["aggregates.dice.std"],
                                        "pattern": "^(.*)$",
                                        "title": "The Error Path Schema",
                                        "type": "string",
                                    },
                                    "order": {
                                        "$id": "#/items/properties/order",
                                        "default": "",
                                        "enum": ["asc", "desc"],
                                        "examples": ["asc"],
                                        "pattern": "^(asc|desc)$",
                                        "title": "The Order Schema",
                                        "type": "string",
                                    },
                                    "path": {
                                        "$id": "#/items/properties/path",
                                        "default": "",
                                        "examples": ["aggregates.dice.mean"],
                                        "pattern": "^(.*)$",
                                        "title": "The Path Schema",
                                        "type": "string",
                                    },
                                    "title": {
                                        "$id": "#/items/properties/title",
                                        "default": "",
                                        "examples": ["Mean Dice"],
                                        "pattern": "^(.*)$",
                                        "title": "The Title Schema",
                                        "type": "string",
                                    },
                                },
                                "required": ["title", "path", "order"],
                                "title": "The Items Schema",
                                "type": "object",
                            },
                            "title": "The Extra Results Columns Schema",
                            "type": "array",
                        }
                    )
                ],
            ),
        ),
    ]
