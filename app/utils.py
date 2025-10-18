def print_table(rows, headers):
    print("\n" + "-" * 60)
    print(" | ".join(headers))
    print("-" * 60)
    for row in rows:
        print(" | ".join(str(x) for x in row))
    print("-" * 60)
