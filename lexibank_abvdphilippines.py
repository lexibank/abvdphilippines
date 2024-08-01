import re
from pathlib import Path
from functools import lru_cache
from nameparser import HumanName
from clldutils.misc import slug
from pylexibank.providers import abvd
from pylexibank.util import progressbar
from pylexibank import FormSpec

# a list of words that we are ignoring as being too problematic.
BADWORDS = [
    '8_toturn',
    '10_dirty',

    # keep 'wife' instead - more languages & fewer 'spouse' terms.
    '57_husband',

    # [LAR] All of the 43 Phil. language forms from PML were provided with the
    # meaning 'cut(slice meat)', so are not equivalent to 'cut, hack (wood)'.
    # They have been given cognate counts, however.
    # SJG: worried about the languages from outside PML though, so better to remove this item
    '78_tocuthack',

    # MR: hard to code, LS comments that current cognates do not distinguish PMP *belaq and *silaq.
    '80_tosplit',

    # MR: problematic
    '93_topoundbeat',
    '152_small',
    '158_narrow',
    '159_wide',
    '171_tohide',
    '173_at',   # lots of missing Phil. data, comments suggest uncoded for Phil.
    '174_ininside',
    '185_we',
    '190_other',
    '191_all',
    '193_if',
    '202_six',
    '203_seven',
    '204_eight',
    '205_nine',
    '206_ten',
    '207_twenty',
    '208_fifty',
    '209_onehundred',
    '210_onethousand',
]


def normalize_contributors(l):
    for key in ['checkedby', 'typedby']:
        l[key] = normalize_names(l[key])
    return l


def normalize_names(names):
    res = []
    if names:
        for name in re.split('\s+and\s+|\s*&\s*|,\s+|\s*\+\s*', names):
            name = {
                'Simon': 'Simon Greenhill',
                'D. Mead': 'David Mead',
                'Alex François': 'Alexandre François',
                'Dr Alex François': 'Alexandre François',
                'R. Blust': 'Robert Blust',
            }.get(name, name)
            name = HumanName(name.title())
            res.append('{0} {1}'.format(name.first or name.title, name.last).strip())
    return ' and '.join(res)


@lru_cache(1000)
def get_language_id(wl):
    return "%s_%d" % (slug(wl.language.name, lowercase=False), int(wl.language.id))


class Dataset(abvd.BVD):
    dir = Path(__file__).parent
    id = 'abvdphilippines'
    SECTION = 'austronesian'

    form_spec = FormSpec(
        brackets={"[": "]", "{": "}", "(": ")"},
        separators="/,~",
        missing_data=('-',),
        strip_inside_brackets=False,
        first_form_only=False,
        replacements=[
            ('(lr)', 'l'),
            (' - las-ay', '')
            ],
    )

    def __init__(self, concepticon=None, glottolog=None):
        super().__init__(concepticon, glottolog)
        self.language_ids = [int(r['ID']) for r in self.languages]

    def cmd_makecldf(self, args):
        args.writer.add_sources(*self.etc_dir.read_bib())  # add overall bib
        concepts = args.writer.add_concepts(
            id_factory=lambda c: c.id.split('-')[-1] + '_' + slug(c.english),
            lookup_factory=lambda c: c['ID'].split('_')[0]
        )
        for wl in progressbar(self.iter_wordlists(args.log), desc="cldfify"):
            wl.to_cldf(args.writer, concepts)
            # Now normalize the typedby and checkedby values:
            args.writer.objects['LanguageTable'][-1] = normalize_contributors(
                args.writer.objects['LanguageTable'][-1])
