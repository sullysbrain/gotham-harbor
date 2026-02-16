import pathlib

import polars as pl

def build_it():
    df = pl.DataFrame(
        {
            "foo": [1, 2, 3, 4, 5],
            "bar": [6, 7, 8, 9, 10],
            "ham": ["a", "b", "c", "d", "e"],
        }
    )
    return df


def main():
    print("Hello from gotham-harbor!")

    path='/data/my_test.parquet'
    # df = build_it()
    # df.write_parquet(path)

    df = pl.read_parquet(path)
    print(df.head())



if __name__ == "__main__":
    main()
