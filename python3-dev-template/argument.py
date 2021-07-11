# coding:utf-8

from argparse import ArgumentDefaultsHelpFormatter, ArgumentParser, Namespace


class Argument:
    def __init__(self) -> None:
        self.parser: ArgumentParser = ArgumentParser(
            description="hoge",
            formatter_class=ArgumentDefaultsHelpFormatter,
        )
        self.parser.add_argument(
            "-net",
            "--network",
            type=str,
            default="cae",
            dest="net",
            help="Network model",
        )

    def get_args(self) -> Namespace:
        return self.parser.parse_args()
