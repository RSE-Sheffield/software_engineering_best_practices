from pathlib import Path
import re

from yaml import safe_load

from nbconvert.preprocessors import Preprocessor

class HighlightExercises(Preprocessor):
    def preprocess(self, notebook, resources):
        for cell in notebook.cells:
            if "tags" in cell.metadata:
                if "exercise" in cell.metadata["tags"]:
                    cell.custom_class = "exercise"
        return notebook, resources


class PageLinks(Preprocessor):
    def preprocess(self, notebook, resources):
        name = resources["metadata"]["name"]
        files = sorted(f.name[:-6] for f in Path(".").glob("*.ipynb") if re.match(r"\d\d.*", f.name))

        if len(files) < 2:
            return notebook, resources

        try:
            index = files.index(name)
        except ValueError:
            return notebook, resources

        resources["metadata"]["name"] = files[index]

        if index == 0:
            previous_file = None
            next_file = files[1]
        elif index == len(files) - 1:
            previous_file = files[-2]
            next_file = None
        else:
            previous_file = files[index - 1]
            next_file = files[index + 1]

        if index == 1:
            previous_file = "index"


        source = ""
        if previous_file is not None:
            source += f'[<font size=\"5\">Previous</font>]({previous_file}.html)'
        if previous_file is not None and next_file is not None:
            source += '<font size=\"5\"> | </font>'
        if next_file is not None:
            source += f'[<font size=\"5\">Next</font>]({next_file}.html)'


        notebook.cells.append({"cell_type": "markdown", "metadata": {}, "source": source})

        return notebook, resources


class SetTitle(Preprocessor):
    def preprocess(self, notebook, resources):
        with open("config.yaml") as f:
            notebook["metadata"]["course_title"] = safe_load(f)["course_title"]
        return notebook, resources


class HideWriteFileMagic(Preprocessor):
    def preprocess(self, notebook, resources):
        execution_count = 0
        for cell in notebook.cells:
            if cell["source"].startswith("%%writefile"):
                file_name = cell["source"].split("\n")[0].split()[1]
                cell.metadata["writefile"] = file_name

                to_remove = len(cell["source"].split("\n")[0])
                cell["source"] = cell["source"][to_remove:]

                cell["outputs"] = []
            else:
                if "execution_count" in cell:
                    execution_count += 1
                    cell.execution_count = execution_count
        return notebook, resources
