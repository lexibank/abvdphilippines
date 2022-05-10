"""
Write nexus file.
"""
from pathlib import Path
from lexibank_abvdphilippines import Dataset as Philippines
from nexusmaker import load_cldf
from nexusmaker import NexusMaker, NexusMakerAscertained, \
    NexusMakerAscertainedParameters


def register(parser):
    parser.add_argument("--output",
        default="abvdphilippines.nex",
        help="output file name")
    parser.add_argument("--ascertainment",
        default=None,
        choices=[None, 'overall', 'word'],
        help="set ascertainment mode")
    parser.add_argument("--filter",
        default=None,
        type=Path,
        help="filename containing a list of parameters (one per line) to remove")


def run(args):
    mdfile = Philippines().cldf_dir / "cldf-metadata.json"
    records = list(load_cldf(mdfile, table='FormTable'))
    
    args.log.info('%8d records loaded from %s' % (len(records), mdfile))

    # run filter if given
    if args.filter:
        for param in args.filter.read_text().split("\n"):
            nrecords = len(records)
            records = [r for r in records if r.Parameter.lower() != param.lower()]
            change = nrecords - len(records)
            args.log.info('%8d records removed for parameter %s' % (
                change, param
            ))
            if change == 0:
                args.log.warn("No records removed for parameter %s -- typo?" % param)
    
    args.log.info('%8d records written to nexus %s using ascertainment=%s' % (
        len(records), args.output, args.ascertainment
    ))

    if args.ascertainment is None:
        nex = NexusMaker(data=records)
    elif args.ascertainment == 'overall':
        nex = NexusMakerAscertained(data=records)
    elif args.ascertainment == 'word':
        nex = NexusMakerAscertainedParameters(data=records)
    else:
        raise ValueError("Unknown Ascertainment %s" % args.ascertainment)

    nex.write(filename=args.output)