import json


def is_phishing(domain_info: json, suspicious_domains: list):
    reason = ""
    
    leaf_cert = domain_info.get('leaf_cert', {})
    # leaf cert not found
    if not leaf_cert:
        return False 
    
    # get data
    all_domains = leaf_cert.get('all_domains', [])
    
    # Suspicious indicators
    suspicious_domains.extend([])
    
    # Check if any suspicious domain is present
    # for domain in all_domains:
    #     if any(suspicious_domain in domain for suspicious_domain in suspicious_domains):
    #         return True, "Domain name found in sucpicious domains."

    for domain in all_domains:
        for suspicious_domain in suspicious_domains:
            if suspicious_domain in domain:
                return True, f"Domain name '{domain}' found in suspicious domains due to match with '{suspicious_domain}'."

    return False, reason
