import time
import logging

def trace_request(request_id: str, service_chain: list[str]):
    """Follow one request through every service hop and log timing."""
    timings = {}
    for service in service_chain:
        start = time.monotonic()
        response = call_service(service, request_id)
        elapsed_ms = (time.monotonic() - start) * 1000
        timings[service] = elapsed_ms
        logging.info(f"[{request_id}] {service}: {elapsed_ms:.1f}ms")

    total = sum(timings.values())
    bottleneck = max(timings, key=timings.get)
    logging.warning(f"[{request_id}] Total: {total:.1f}ms | Bottleneck: {bottleneck}")
    return timings
