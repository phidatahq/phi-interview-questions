from datetime import datetime

from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql.expression import text
from sqlalchemy.types import BigInteger, DateTime, String

from db.tables.base import Base


class MetricsTable(Base):
    """
    Table for storing metrics.
    """

    __tablename__ = "metrics"

    metric: Mapped[str] = mapped_column(String, primary_key=True, index=True)
    value: Mapped[int] = mapped_column(BigInteger, nullable=False, default=0)
    last_updated: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=text("now()"), onupdate=text("now()")
    )
