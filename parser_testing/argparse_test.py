import argparse
import pprint
from typing import Optional
from typing import Sequence

def positive_int(s: str) -> int:
	try:
		v = int(s)
	except ValueError:
		raise argparse.ArgumentTypeError(f'expected integer, got {s!r}')

	if v <=0:
		raise argparse.ArgumentTypeError(f'expected positive integer, got {v}')

	return v



def main(argv: Optional[Sequence[str]] = None) -> int:

	# Parse arguments

    parser = argparse.ArgumentParser(description='Testing')

    # positional required arguments, no dash
    # - help
    # %(prog)s = name of current file
    # default can be used
    
    #parser.add_argument('filename', help='configuration filename %(prog)s')

    # optional
    # - short (one dash/letter) vs long (required) opts 
    # - aliases
    # - defaults
    # required = True
    parser.add_argument(
    	'-c', '--config', '--jsonfile',
    	default='config.json',
    	help='specify the config file.  (default: %(default)s)',
    )

    # types
    # parser.add_argument(
    # 	'--days',
    # 	type=int,
    # )

    parser.add_argument(
    	'--days',
    	type=positive_int,
    )

    # count
    parser.add_argument('-v', '--verbose', action='count', default=0)

    # boolean options
    # other actions include store_false and const=...
    parser.add_argument('--force', action='store_true')

    # append
    # this example stores log files in a list
    parser.add_argument('--log', action='append', default=[])

    # choices
    parser.add_argument('--color', choices=('auto', 'always', 'never'))


    """
    # sub commands
    subparsers = parser.add_subparsers(dest='command')
    subparsers.required = True

    status_parser = subparsers.add_parser('status')
    status_parser.add_argument('--force', action='store_true')

    checkout_parser = subparsers.add_parser('checkout')
    checkout_parser.add_argument('--verbose', action='count')
    """

    args = parser.parse_args()
    pprint.pprint(vars(args))
    #parser.print_help()
    return 0


if __name__ == '__main__':
	exit(main())