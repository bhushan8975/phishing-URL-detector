import tldextract
import re
import whois
import pandas as pd

def extract_features(url):
    features = {}
    features['url_length'] = len(url)
    features['has_ip'] = bool(re.match(r'\d+\.\d+\.\d+\.\d+', url))
    features['has_https'] = url.startswith("https")
    features['special_chars'] = sum([url.count(c) for c in ['@', '-', '=', '%']])
    ext = tldextract.extract(url)
    domain = ext.domain + '.' + ext.suffix
    try:
        domain_info = whois.whois(domain)
        features['domain_age'] = (pd.Timestamp.now() - pd.to_datetime(domain_info.creation_date)).days
    except:
        features['domain_age'] = 0
    return features