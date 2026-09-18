from pydantic import BaseModel, Field

# The Contract: Explicit schema for customer support tickets
class SupportTicketInput(BaseModel):
    customer_email: str = Field(..., description="The email address of the customer")
    issue_category: str = Field(..., description="Must be one of: billing, technical, general")
    urgency_level: int = Field(..., ge=1, le=5, description="Urgency scale from 1 (low) to 5 (critical)")

def execute_support_lookup(data: SupportTicketInput) -> dict:
    """Simulates looking up or triaging a support ticket based on strict contract parameters."""
    return {
        "status": "success",
        "routed_queue": f"{data.issue_category}_team",
        "message": f"Ticket processed for {data.customer_email} with urgency level {data.urgency_level}."
    }