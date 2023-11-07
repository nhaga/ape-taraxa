EXPECTED_OUTPUT = """
taraxa
|── local  (default)
|   └── test  (default)
├── mainnet
│   └── taraxa  (default)
└── testnet
    └── taraxa  (default)
""".strip()


def assert_rich_text(actual: str, expected: str):
    """
    The output from `rich` causes a bunch of extra spaces to
    appear at the end of each line. For easier testing, we remove those here.
    """
    actual = f"taraxa{actual.split('taraxa')[-1]}"

    expected = expected.strip()
    lines = actual.split("\n")
    new_lines = []
    for line in lines:
        if line:
            new_lines.append(line.rstrip())

    actual = "\n".join(new_lines)
    print(actual)
    assert actual == expected


def test_networks(runner, cli):
    result = runner.invoke(cli, ["networks", "list"])
    assert_rich_text(result.output, EXPECTED_OUTPUT)
