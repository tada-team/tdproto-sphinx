from __future__ import annotations

from typing import Sequence, Union, Any

from docutils import nodes
from sphinx import addnodes
from sphinx.application import Sphinx
from docutils.parsers.rst import Directive
from sphinx.domains import Domain

from typing import Dict

OMIT_EMPTY_STR = 'Maybe omitted'
MAYBE_NULL_STR = 'Might be null'


class TdprotoStructFieldLine(nodes.line, addnodes.translatable):

    def preserve_original_messages(self) -> None:
        return  # Do not preserve anything

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
        return [self.children[-1].rawsource, OMIT_EMPTY_STR, MAYBE_NULL_STR]


class TdprotoStruct(Directive):
    required_arguments = 1
    has_content = True

    def run(self) -> list[Any]:
        self.assert_has_content()

        title = nodes.title(text=self.arguments[0])

        structure_description = []
        fields_list = nodes.bullet_list()
        fields_list.append(nodes.paragraph(text='Fields:'))

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
                        reference_target = option.split('`')[1]
                        reference_name = reference_target.split('-')[1]

                        new_ref = addnodes.pending_xref(
                            refdomain='std',
                            reftarget=reference_target.lower(),
                            reftype='ref',
                            refexplicit=True,
                            refwarn=True,
                        )
                        ref_name = option.replace(
                            f"`{reference_target}`", reference_name)
                        new_ref.append(nodes.inline(text=ref_name))
                        start_node = nodes.inline(text=' (')
                        start_node.append(new_ref)
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

        paragraph = nodes.paragraph(text='\n'.join(structure_description))

        return [title, paragraph, fields_list]


class TdprotoDomain(Domain):
    name = 'tdproto'
    label = 'Tdproto'

    directives = {
        'struct': TdprotoStruct,
    }
    initial_data: Dict[Any, Any] = {
        'structs': [],
    }


def setup(app: Sphinx) -> dict[str, Union[str, bool]]:
    app.add_domain(TdprotoDomain)
    app.add_node(TdprotoStructFieldLine)

    return {
        'version': 'unstable',
        'parallel_read_safe': True,
        'parallel_write_safe': True,
    }
