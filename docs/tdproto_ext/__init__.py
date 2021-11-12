from __future__ import annotations

from typing import Any, Dict, Optional, Sequence, Union

from docutils import nodes
from docutils.parsers.rst import Directive
from docutils.parsers.rst.directives import unchanged_required
from sphinx import addnodes
from sphinx.addnodes import Element
from sphinx.application import Sphinx
from sphinx.builders import Builder
from sphinx.domains import Domain
from sphinx.environment import BuildEnvironment
from sphinx.roles import XRefRole

OMIT_EMPTY_STR = 'Maybe omitted'
MAYBE_NULL_STR = 'Might be null'

TDPROTO_TARGETS: Dict[Any, Any] = {}


class TdprotoStructFieldLine(nodes.line, addnodes.translatable):

    def preserve_original_messages(self) -> None:
        original_messages = [self.children[-1].rawsource]
        for c in self.children:
            if isinstance(c, nodes.abbreviation):
                original_messages.append(c.attributes['explanation'])

        self['rawentries'] = original_messages

    def apply_translated_message(self,
                                 original_message: str,
                                 translated_message: str) -> None:
        if (original_message == OMIT_EMPTY_STR
                or original_message == MAYBE_NULL_STR):
            for c in self.children:
                if isinstance(c, nodes.abbreviation):
                    c.attributes['explanation'] = translated_message

        else:
            self.children[-1] = nodes.inline(text=translated_message)

    def extract_original_messages(self) -> Sequence[str]:
        return self['rawentries']


class TdprotoSimple(Directive):
    required_arguments = 1
    has_content = True
    option_spec = {
        'tdpackage': unchanged_required,
    }

    def run(self) -> list[Any]:
        self.assert_has_content()

        package_name = self.options['tdpackage']

        section = nodes.section()
        section.line = self.lineno
        section.lineno = self.lineno

        td_title = self.arguments[0]
        title = nodes.title(text=td_title)
        section['ids'].append(f"{package_name}-{td_title}")
        TDPROTO_TARGETS[(package_name, td_title)] = section

        paragraph = nodes.paragraph()
        self.state.nested_parse(self.content, self.content_offset, paragraph)

        section.extend([title, paragraph])

        return [section]


class TdprotoStruct(Directive):
    required_arguments = 1
    has_content = True
    option_spec = {
        'tdpackage': unchanged_required,
    }

    def run(self) -> list[Any]:
        self.assert_has_content()

        package_name = self.options['tdpackage']

        section = nodes.section()
        section.line = self.lineno
        section.lineno = self.lineno

        td_title = self.arguments[0]
        title = nodes.title(text=td_title)
        section['ids'].append(f"{package_name}-{td_title}")
        TDPROTO_TARGETS[(package_name, td_title)] = section

        structure_description = []
        fields_list = nodes.bullet_list()
        fields_list.append(nodes.line(text='Fields:'))

        for x in self.content:
            if not x.startswith(':field '):
                structure_description.append(x)
                continue

            field_options_str, field_text = tuple(x.split(':',
                                                          maxsplit=2
                                                          )[1:])
            field_text = field_text.lstrip(' ')

            field_options_list = field_options_str.split()

            field_line = TdprotoStructFieldLine()

            for i, option in enumerate(field_options_list):
                if i == 0:
                    ...
                elif i == 1:
                    field_line.append(nodes.literal(text=option))
                elif i == 2:
                    if '`' in option:
                        is_array = False

                        if option.startswith('array'):
                            is_array = True

                        reference_target = option.split('`')[1]
                        reference_name = reference_target.split('-')[1]

                        new_ref = addnodes.pending_xref(
                            refdomain='tdproto',
                            reftarget=reference_name,
                            reftype='tdmodels',
                            refdoc='data_index',
                            refexplicit=True,
                            refwarn=True,
                        )
                        ref_name = option.replace(
                            f"`{reference_target}`", reference_name)
                        new_ref.append(nodes.inline(text=ref_name))

                        if is_array:
                            start_node = nodes.inline(text=' (array[')
                        else:
                            start_node = nodes.inline(text=' (')

                        start_node.append(new_ref)

                        if is_array:
                            start_node.append(nodes.inline(text='])'))
                        else:
                            start_node.append(nodes.inline(text=')'))

                        field_line.append(start_node)
                    else:
                        field_line.append(nodes.inline(text=f" ({option})"))
                elif i == 3:
                    if option == 'omitempty':
                        omit_empty_abbreviation = nodes.abbreviation(
                            text=' 💥 ')
                        omit_empty_abbreviation.attributes['explanation'] \
                            = OMIT_EMPTY_STR

                        field_line.append(omit_empty_abbreviation)
                    elif option == 'nullable':
                        maybe_null_abbreviation = nodes.abbreviation(
                            text=' 0️⃣ ')
                        maybe_null_abbreviation.attributes['explanation'] \
                            = MAYBE_NULL_STR

                        field_line.append(maybe_null_abbreviation)
                    else:
                        raise ValueError('Unknown modifier')
                else:
                    raise ValueError('Too many options')

            field_line.append(nodes.inline(text=" — "))
            field_line.append(nodes.inline(text=field_text))

            fields_list.append(field_line)

        paragraph = nodes.paragraph()
        self.state.nested_parse(
            self.content[:2],
            self.content_offset,
            paragraph,
        )

        section.extend([title, paragraph, fields_list])

        return [section]


DATA_INDEX_DOC_NAME = 'data_index'


class TdprotoDomain(Domain):
    name = 'tdproto'
    label = 'Tdproto'

    directives = {
        'struct': TdprotoStruct,
        'enum': TdprotoSimple,
        'type': TdprotoSimple,
    }
    initial_data: Dict[Any, Any] = {
        'structs': [],
    }
    roles = {
        'tdforms': XRefRole(),
        'tdmodels': XRefRole(),
    }

    def resolve_xref(
        self, env: BuildEnvironment, fromdocname: str, builder: Builder,
        type: str, target: str, node: nodes.pending_xref, contnode: Element
    ) -> Optional[Element]:
        reftarget = node.attributes['reftarget']
        td_package_ref = node.attributes['reftype']

        tdproto_target = TDPROTO_TARGETS.get((td_package_ref, reftarget))
        if tdproto_target is None:
            return None

        refuri = (
            builder.get_relative_uri(fromdocname, DATA_INDEX_DOC_NAME)
            + f"#{td_package_ref}-{reftarget}"
        )

        return nodes.reference(
            text=reftarget,
            refuri=refuri,
            internal=False)


def setup(app: Sphinx) -> dict[str, Union[str, bool]]:
    app.add_domain(TdprotoDomain)
    app.add_node(TdprotoStructFieldLine)

    return {
        'version': 'unstable',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
