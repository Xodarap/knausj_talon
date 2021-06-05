from talon import Module, Context, actions, ui, imgui, settings

mod = Module()
ctx = Context()
ctx.matches = r"""
mode: user.javascript
mode: command 
and code.language: javascript
"""
# tbd
# ctx.lists["user.code_functions"] = {
#     "integer": "int.TryParse",
#     "print": "Console.WriteLine",
#     "string": ".ToString",
# }

ctx.lists["self.react_sizes"] = {
    "small": "sm",
    "medium": "md",
    "large": "lg",
    "extra-large": "xl",
}

mod.list("react_sizes", desc="react sizes")
@mod.capture(rule="{self.react_sizes}")
def react_sizes(m) -> str:
    "Returns a string"
    return m.react_sizes

ctx.lists["self.alphabet"] = {
    "foxtrot": "f",
    'golf': 'g',
    'hotel': 'h',
    "kilo": 'k',
    "Romeo": "r",
    "Sierra": "s",
    "Tango": "t",
    "uniform": "u",
    "Victor": "v",
}

mod.list("alphabet", desc="react sizes")
@mod.capture(rule="{self.alphabet}")
def alphabet(m) -> str:
    "Returns a string"
    return m.alphabet

ctx.lists["self.elements"] = {
    "div": "div",
    'alpha': 'a'
}
mod.list("elements", desc="react sizes")
@mod.capture(rule="{self.elements}")
def elements(m) -> str:
    "Returns a string"
    return m.elements


@ctx.action_class("user")
class user_actions:
    def code_insert_function(text: str, selection: str):
        if selection:
            text = text + "({})".format(selection)
        else:
            text = text + "()"

        actions.insert(text)
        actions.edit.left()

    def code_private_function(text: str):
        """Inserts private function declaration"""
        result = "function {}".format(
            actions.user.formatted_text(
                text, settings.get("user.code_private_function_formatter")
            )
        )

        actions.user.code_insert_function(result, None)

    # def code_private_static_function(text: str):
    #     """Inserts private static function"""
    #     result = "private static void {}".format(
    #         actions.user.formatted_text(
    #             text, settings.get("user.code_private_function_formatter")
    #         )
    #     )

    #     actions.user.code_insert_function(result, None)

    def code_protected_function(text: str):
        result = "function {}".format(
            actions.user.formatted_text(
                text, settings.get("user.code_protected_function_formatter")
            )
        )

        actions.user.code_insert_function(result, None)

    # def code_protected_static_function(text: str):
    #     result = "protected static void {}".format(
    #         actions.user.formatted_text(
    #             text, settings.get("user.code_protected_function_formatter")
    #         )
    #     )

    #     actions.user.code_insert_function(result, None)

    def code_public_function(text: str):
        result = "export function {}".format(
            actions.user.formatted_text(
                text, settings.get("user.code_public_function_formatter")
            )
        )

        actions.user.code_insert_function(result, None)
    def code_import_component(text: str):
        actions.insert("import {} from 'components/{}';\n".format(
            actions.user.formatted_text(text, 'PUBLIC_CAMEL_CASE'),
            actions.user.formatted_text(text, 'SNAKE_CASE')
        ))
    def code_element(text: str):
        actions.insert("<{}>".format(
            actions.user.formatted_text(text, 'PUBLIC_CAMEL_CASE')
        ))
        actions.edit.left(3)
    def code_element_self_closing(text: str):
        actions.insert("<{} />".format(
            actions.user.formatted_text(text, 'PUBLIC_CAMEL_CASE')
        ))
        actions.edit.left(2)
    def code_helement(text: str):
        actions.insert("<{}>".format(
            actions.user.formatted_text(text, 'ALL_LOWERCASE')
        ))
        actions.edit.left(3)
    def code_helement_self_closing(text: str):
        actions.insert("<{} />".format(
            actions.user.formatted_text(text, 'ALL_LOWERCASE')
        ))
        actions.edit.left(2)
    def code_element_close(text: str):
        actions.insert("</{}>".format(
            actions.user.formatted_text(text, 'PUBLIC_CAMEL_CASE')
        ))
    # def code_public_static_function(text: str):
    #     result = "public static void {}".format(
    #         actions.user.formatted_text(
    #             text, settings.get("user.code_public_function_formatter")
    #         )
    #     )

    #     actions.user.code_insert_function(result, None)

    