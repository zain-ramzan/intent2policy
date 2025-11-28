def intent_to_policy(intent: dict):
    action = intent.get("action", "deny")
    proto = intent.get("protocol", "any")
    src = intent.get("source", "any")
    dst = intent.get("destination", "any")
    proto_map = {"ssh":"22", "http":"80", "https":"443"}
    port = proto_map.get(proto.lower(), "any")
    rule = f"{action} {proto} from {src} to {dst}"
    if port != "any":
        rule += f" port {port}"
    return rule

def detect_conflicts(intents):
    conflicts = []
    seen = {}
    for p in intents:
        key = (p.get("source"), p.get("destination"), p.get("protocol"))
        if key in seen and seen[key] != p.get("action"):
            conflicts.append({"key": key, "actions": [seen[key], p.get("action")]})
        else:
            seen[key] = p.get("action")
    return conflicts
