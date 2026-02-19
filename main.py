import argparse
from services.run_service import run_pipeline
from services.report_service import generate_report
from services.export_service import export_csv
from storage.db import get_connection
from storage.schema import init_db


def parse_args():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="command")

    run_cmd = subparsers.add_parser("run")
    run_cmd.add_argument("--market", default="givataym", help="Market to scrape (default: givataym)")

    report_cmd = subparsers.add_parser("report")
    report_cmd.add_argument("--market", required=True)
    report_cmd.add_argument("--date", required=True)

    export_cmd = subparsers.add_parser("export")
    export_cmd.add_argument("--market", required=True)
    export_cmd.add_argument("--date", required=True)

    return parser.parse_args()


def main():
    args = parse_args()

    if args.command == "run":
        run_pipeline(args.market)

    elif args.command == "report":
        generate_report(args.market, args.date)

    elif args.command == "export":
        export_csv(args.market, args.date)

    else:
        print("Invalid command")


if __name__ == "__main__":
    main()

