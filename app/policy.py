from dataclasses import dataclass, field

@dataclass
class Policy:
    per_purchase_cap: float = 50.0
    daily_budget: float = 150.0
    approval_threshold: float = 25.0
    allowed_categories: set = field(
        default_factory=lambda: {"electronics", "books", "software", "services"}
    )

def evaluate(amount: float, category: str, spent_today: float, policy: Policy) -> dict:
    if amount <= 0:
        return {"decision": "deny", "reason": "Amount must be positive"}
    if category not in policy.allowed_categories:
        return {"decision": "deny", "reason": f"Category '{category}' is not allowed"}
    if amount > policy.per_purchase_cap:
        return {"decision": "deny", "reason": f"${amount:.2f} exceeds the per-purchase cap of ${policy.per_purchase_cap:.2f}"}
    if spent_today + amount > policy.daily_budget:
        return {"decision": "deny", "reason": "Would exceed the daily budget"}
    if amount > policy.approval_threshold:
        return {"decision": "needs_approval", "reason": f"Above the ${policy.approval_threshold:.2f} auto-approve threshold"}
    return {"decision": "approve", "reason": "Within all limits"}