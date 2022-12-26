import sys
import dns.resolver

if len(sys.argv) != 3:
    exit(1)


def get_dns_records(domain):
    # Create a DNS resolver
    resolver = dns.resolver.Resolver()

    # Perform the DNS lookup
    try:
        answers = resolver.resolve(domain, sys.argv[2])
        return [rdata for rdata in answers]
    except dns.resolver.NXDOMAIN:
        return []


if __name__ == "__main__":
    records = get_dns_records(sys.argv[1])
    if records:
        print(f"DNS records for {sys.argv[1]}:")
        for rdata in records:
            print(rdata)
    else:
        print(f"No DNS records found for {sys.argv[1]}")
