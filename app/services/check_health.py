import time
from typing import Dict, Any

# In-memory metrics dictionaries
api_calls: Dict[str, int] = {
    "github": 0,
    "stackoverflow": 0,
    "devto": 0,
    "hackernews": 0
}

llm_metrics = {
    "total_tokens": 0,
    "estimated_cost_usd": 0.0
}

resolution_metrics = {
    "total_resolved": 0,
    "total_processing_time_ms": 0.0
}

github_rate_limit = {
    "remaining": "Unknown",
    "total": "Unknown",
    "reset_time": "Unknown"
}


def log_api_call(source: str):
    global api_calls
    if source in api_calls:
        api_calls[source] += 1


def update_github_headers(remaining: str, total: str, reset: str):
    global github_rate_limit
    github_rate_limit["remaining"] = remaining
    github_rate_limit["total"] = total
    github_rate_limit["reset_time"] = reset


def log_llm_usage(tokens: int):
    global llm_metrics
    llm_metrics["total_tokens"] += tokens


def log_resolution(duration_ms: float):
    global resolution_metrics
    resolution_metrics["total_resolved"] += 1
    resolution_metrics["total_processing_time_ms"] += duration_ms


def get_health_report() -> Dict[str, Any]:
    global api_calls, llm_metrics, resolution_metrics, github_rate_limit
    
    total = resolution_metrics["total_resolved"]
    total_time = resolution_metrics["total_processing_time_ms"]
    avg_time = (total_time / total) if total > 0 else 0.0
    
    return {
        "status": "healthy",
        "timestamp_epoch": int(time.time()),
        "github_rate_limiting": github_rate_limit,
        "external_api_calls_by_source": api_calls,
        "llm_observability": llm_metrics,
        "resolution_performance": {
            "profiles_resolved_count": total,
            "average_resolution_time_ms": round(avg_time, 2)
        }
    }