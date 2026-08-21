# voc-to-md

import json
import os.path
import sys
import argparse

from markdown2 import Markdown
markdowner = Markdown()


parser = argparse.ArgumentParser(description='vocpopuliconv - convert vocpopuli json exercises to an easy Manon-readable format')
parser.add_argument('exercise_folder', type=str, help='the exercise file which will be converted')
parser.add_argument('header', type=str, help='the header for the top of the file')
parser.add_argument('output_filename', type=str, help='where should the rendered html go to? include extension')

args = parser.parse_args()

def folder_to_markdown(folder_path: str) -> str:
	output_markdown = f"# {args.header}\n\n"

	exercise_paths = [ f.path for f in os.scandir(folder_path) if f.path.endswith(".json") ]
	exercise_paths = sorted(exercise_paths)
	print("Found {} exercises".format(len(exercise_paths)))

	for exercise_path in exercise_paths:
		output_markdown += json_file_to_markdown(exercise_path)

	output_markdown += "\n\nJoepie! Weer iets achter de rug!"

	return output_markdown

def json_file_to_markdown(json_path: str) -> str:
	file_basename = os.path.splitext(os.path.basename(json_path))[0]
	unit_markdown = f"### {file_basename}\n\n"

	with open(json_path, "r") as exercise_reader:
		exercises = json.loads(exercise_reader.read())
		unit_markdown += to_markdown(exercises)

	unit_markdown += "\n\n"

	return unit_markdown

def to_markdown(exercises) -> str:
	markdown = ""

	exercise_no = 1
	for exercise in exercises:
		more_info = ""

		if not "synonyms" in exercise:
			exercise["synonyms"] = ""

		if exercise["definition"] != "" and exercise["synonyms"] != "":
			more_info = " (*{}*; *{}*)".format(exercise["definition"], exercise["synonyms"])
		elif exercise["definition"] != "" and exercise["synonyms"] == "":
			more_info = " (*{}*)".format(exercise["definition"])
		elif exercise["definition"] == "" and exercise["synonyms"] != "":
			more_info = " (*{}*)".format(exercise["synonyms"])

		# corpus_data = exercise["corpus"].replace("*", "\\*").replace("_", "\\_")
		corpus_data = exercise["corpus"].replace("--", "&ndash;")
		corpus_data = corpus_data.replace(exercise["word"], f"XXXXXXX{more_info}")
		options = [ option.strip() for option in exercise["word"].split("/") ]

		written_exercise = f"{exercise_no}. {corpus_data}\n"
		for option in options:
			written_exercise += f"    - {option}\n"

		markdown += written_exercise

		exercise_no += 1

	return markdown


def apply_template(markdown):
	template = """<html>

<head>
    <meta charset="UTF-8">
    <style>
        body {
            font-family: sans-serif;
            line-height: 1.5em;
        }
    </style>
    <meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover" />
</head>

<body>


$JOHANJOHANJOHAN$


</body>

</html>"""

	return template.replace("$JOHANJOHANJOHAN$", markdown)

if not os.path.exists(args.exercise_folder):
	print("Exercise folder doesn't exist")
	sys.exit(0)

markdown = folder_to_markdown(args.exercise_folder)
html = markdowner.convert(markdown).replace("em>", "i>")
html = apply_template(html)

with open(args.output_filename, "w") as output_writer:
	output_writer.write(html)