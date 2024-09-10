from phockup.phockup import main, parse_args, setup_logging


def app():
    options = parse_args()
    setup_logging(options)
    main(options)
