from docs_drift_demo.cli import build_parser


def test_status_flag_exists():
    parser = build_parser()
    args = parser.parse_args(["--status"])
    assert args.status is True
