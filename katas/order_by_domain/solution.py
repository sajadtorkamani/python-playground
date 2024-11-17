import re
from typing import List
from functools import cmp_to_key


def order_by_domain(domains: List[str]) -> List[str]:
    high_priority_domains = []
    low_priority_domains = []

    for domain in domains:
        tld = get_tld(domain)

        if tld in ['com', 'gov', 'org']:
            high_priority_domains.append(domain)
        else:
            low_priority_domains.append(domain)

    high_priority_domains = sorted(high_priority_domains, key=cmp_to_key(compare_high_priority_domain_tld))
    low_priority_domains = sorted(low_priority_domains, key=cmp_to_key(compare_lower_priority_domain_tld))

    return high_priority_domains + low_priority_domains


def compare_high_priority_domain_tld(domain1: str, domain2: str) -> int:
    domain1_tld_score = get_tld_score(get_tld(domain1))
    domain2_tld_score = get_tld_score(get_tld(domain2))

    if domain1_tld_score == domain2_tld_score:
        if domain1 == domain2:
            return 0

        if domain1 < domain2:
            return -1
        else:
            return 1

    if domain1_tld_score > domain2_tld_score:
        return -1

    return 1


def compare_lower_priority_domain_tld(domain1: str, domain2: str) -> int:
    domain1_tld = get_tld(domain1)
    domain2_tld = get_tld(domain2)

    if domain1_tld == domain2_tld:
        return 0

    if domain1_tld < domain2_tld:
        return -1
    else:
        return 1


def get_tld(domain: str) -> str:
    tld = domain.split('.')[-1]
    return re.sub("[/?|].*", "", tld)


def get_tld_score(tld: str) -> int:
    if tld == 'com':
        return 3

    if tld == 'gov':
        return 2

    if tld == 'org':
        return 1

    return 0
