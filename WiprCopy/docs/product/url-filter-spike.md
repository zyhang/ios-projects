# URL Filter spike checklist

Status: **planned** (decision: spike before locking launch; default target self-hosted PIR).

## Goal

Prove system-wide blocking (Apple URL Filters) is shippable under our privacy bar, on iPhone and Mac.

## Out of scope for spike

- Polished UI, rule packs, App Store copy  
- Full production blocklist size  
- Web Extension (Extra)

## In scope

- [ ] Apple sample / docs: `NEURLFilterManager`, `NEURLFilterControlProvider`, Bloom prefilter, PIR server  
- [ ] App + extension targets on **iOS** and **macOS**  
- [ ] Enable / disable filter from app; persist configuration  
- [ ] Prefilter fetch interval  
- [ ] Block a small fixed set of test URLs system-wide (not only Safari)  
- [ ] Confirm coexistence with VPN and iCloud Private Relay (primary path)  
- [ ] Document what the app process can and cannot observe  
- [ ] Rough ops notes: hosting PIR, tokens, update failure behavior (fail open vs closed)

## Success → next

Default: productionize self-hosted PIR + list pipeline; v1 includes system-wide in base purchase.

## Fail / too heavy → fallback

Keep system-wide in v1 with smaller list and/or lower refresh rate; do **not** drop the primary wedge or relegate it to a core IAP.

## References

- [URL filters](https://developer.apple.com/documentation/networkextension/url-filters)  
- [Filtering traffic by URL](https://developer.apple.com/documentation/networkextension/filtering-traffic-by-url)  
- WWDC25: Filter and tunnel network traffic with NetworkExtension  
- Product decisions: `AGENTS.md`, [overview.md](overview.md)
