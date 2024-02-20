class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        domain_counts = {}
    
        for cpdomain in cpdomains:
            count, domain = cpdomain.split(" ")
            count = int(count)

            subdomains = domain.split(".")
            for i in range(len(subdomains)):
                subdomain = ".".join(subdomains[i:])
                domain_counts[subdomain] = domain_counts.get(subdomain, 0) + count

        result = [f"{count} {domain}" for domain, count in domain_counts.items()]
        return result
