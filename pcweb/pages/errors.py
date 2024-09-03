import reflex as rx
from pcweb.templates.webpage import webpage
from pcweb.flexdown import xd2 as xd
from pcweb import constants
from pcweb.components.webpage.pill import pill
from pcweb.components.webpage.comps import h1_title


def errors_content() -> rx.Component:
    return rx.el.ul(
        xd.render_file("errors.md"),
        class_name="flex flex-col gap-6 w-full",
    )


@webpage(path="/errors", title="Common Errors · Reflex")
def errors() -> rx.Component:
    return rx.el.section(
        # pill(text="Common Errors"),
        rx.box(
            h1_title(title="Common Errors"),
            rx.box(
                rx.el.h2(
                    "We've compiled a list of the most common errors users face when using Reflex. If you have encountered an error that isn't answered here, feel free to reach out to us on our ",
                    rx.link(
                        "Discord",
                        underline="always",
                        href=constants.DISCORD_URL,
                        class_name="text-violet-9",
                    ),
                    ".",
                ),
                class_name="border-slate-4 bg-slate-2 p-4 md:p-6 border rounded-xl w-full md:font-md text-slate-11 text-small text-start text-wrap",
            ),
            class_name="section-header",
        ),
        errors_content(),
        id="common-errors",
        class_name="section-content",
    )
