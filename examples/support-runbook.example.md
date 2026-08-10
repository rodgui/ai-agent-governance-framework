# Example support runbook — Service Desk Knowledge Agent

> Fictitious and sanitized.

## Ownership

- Business owner: Example Business Owner
- Technical owner: Example Technical Owner
- Run owner: Example Run Owner

## Signals and actions

| Signal | First action | Escalation |
|---|---|---|
| unavailable approved source | stop grounded response and inform analyst | Knowledge Owner |
| prohibited-data request | refuse and record security signal | Security and Data Owner |
| repeated unsupported answer | quarantine affected version | Run Authority |
| unexpected tool call | gateway deny, quarantine and preserve evidence | Security and Run Authority |

## Recovery

1. record version, session correlation and affected scope;
2. revoke tool access or block new sessions;
3. preserve authorized evidence with sensitive payload redacted;
4. identify cause and corrective action;
5. run the regression suite;
6. require Run and Design Authority evidence before reactivation.

## Boundaries

This runbook is illustrative and does not replace an organization's incident process, on-call model or legal obligations.
