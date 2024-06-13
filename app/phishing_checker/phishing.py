import json


def is_phishing(domain_info: json, suspicious_domains: list):
    reason = ""
    
    leaf_cert = domain_info.get('leaf_cert', {})
    # leaf cert not found
    if not leaf_cert:
        return False 
    
    # get data
    all_domains = leaf_cert.get('all_domains', [])
    subject_alt_name = leaf_cert.get('extensions', {}).get('subjectAltName', '')
    issuer = leaf_cert.get('issuer', {})
    not_before = leaf_cert.get('not_before', 0)
    not_after = leaf_cert.get('not_after', 0)
    
    # Suspicious indicators
    suspicious_domains.extend([])
    
    # Check if any suspicious domain is present
    for domain in all_domains:
        if any(suspicious_domain in domain.lower() for suspicious_domain in suspicious_domains):
            return True, "Domain name found in sucpicious domains."

    return False, reason
