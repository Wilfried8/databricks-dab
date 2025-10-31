from __future__ import annotations

from typing import Any, Protocol


class _SparkReader(Protocol):
    def table(self, name: str) -> Any: ...


class _SparkSession(Protocol):
    read: _SparkReader


def _load_databricks_spark() -> _SparkSession:
    """Return the Databricks-provided SparkSession or raise a helpful error."""
    try:
        from databricks.sdk.runtime import spark  # type: ignore
    except Exception as exc:
        raise RuntimeError(
            "Databricks runtime SparkSession not available. "
            "Provide a spark_session instance when calling find_all_taxis() outside Databricks."
        ) from exc
    return spark


def find_all_taxis(spark_session: _SparkSession | None = None) -> Any:
    session = spark_session or _load_databricks_spark()
    return session.read.table("samples.nyctaxi.trips")


def main() -> None:
    find_all_taxis().show(5)


if __name__ == "__main__":
    main()
