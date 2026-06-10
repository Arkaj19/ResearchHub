from sqlalchemy import Column,String, Text, DateTime, func
from sqlalchemy.dialects.postgresql import UUID
import uuid
from db.database import Base

class ResearchJob(Base):
    __tablename__ = "research_jobs"

    id            = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    query         = Column(Text, nullable=False)
    status        = Column(String(20), nullable=False, default="Pending")
    created_at    = Column(DateTime(timezone=True), server_default=func.now())
    updated_at    = Column(DateTime(timezone=True), onupdate=func.now())
    result        = Column(Text, nullable=True)
    error_message = Column(Text, nullable=True)

    