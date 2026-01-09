import re

from docutils import nodes
from docutils.parsers.rst import Directive, directives
from docutils.core import publish_parts
from pelican import signals

jinja_env = None
jinja_settings = None

def set_env(generator):
    global jinja_env
    global jinja_settings
    jinja_env = generator.env
    jinja_settings = generator.settings


def parse_link(raw):
    match = re.match(r"^(.*)\s*<([^>]+)>$", raw)
    if not match:
        raise ValueError(f"Invalid link format '{raw}'")
    uri = match[2]
    title = match[1] if match[1] else match[2]
    return title.strip(), uri.strip()


class ProjectDirective(Directive):
    """
    A project in the projects modal.
    """

    required_arguments = 0
    option_spec = {
        "title": str,
        "links": directives.unchanged,
        "image": directives.uri
    }
    has_content = True

    def run(self):
        # Check that the project directive is inside a projects directive
        parent = self.state.parent
        if not "projects-modal" in parent["classes"]:
            return [self.state_machine.reporter.error(
                "Found a 'project' directive outside of 'projects'",
                nodes.literal_block(self.block_text, self.block_text),
                line=self.lineno
            )]

        try:
            title = self.options["title"]
        except KeyError:
            raise AttributeError("Missing option 'title'")
        try:
            image = self.options["image"]
        except KeyError:
            raise AttributeError("Missing option 'image'")
        raw_links = self.options.get("links", "")
        links = [parse_link(link.strip()) for link in raw_links.split(",")] if raw_links else []

        anchor = f"projects-popup-{title.lower().replace(" ", "-")}"

        template = jinja_env.get_template("snippets/project.html")
        return [nodes.raw("", template.render(
            project_title = title,
            project_image = image,
            project_links = links,
            project_anchor = anchor,
            project_content = publish_parts(
                source="\n".join(self.content),
                writer_name="html",
                settings_overrides={
                    "initial_header_level": 3
                }
            )["fragment"],
            **jinja_settings
        ), format="html")]

class ProjectsDirective(Directive):
    """
    The projects list modal.
    """

    has_content = True

    def run(self):
        node = nodes.bullet_list(classes=["projects-modal"])
        self.state.nested_parse(self.content, self.content_offset, node)

        return [node]


signals.generator_init.connect(set_env)
directives.register_directive("project", ProjectDirective)
directives.register_directive("projects", ProjectsDirective)
