# Template — Checklist de evidence readiness e decisão G5

Use antes de release, publication ou mudança material. Este checklist organiza evidence readiness; ele não calcula nem concede aprovação. Cada item deve ter owner e evidence ref.

## 1. Registro e escopo

- [ ] Agent ID, versão e ambientes identificados.
- [ ] Finalidade autorizada, usuários, affected parties, regiões e prohibited uses registrados.
- [ ] Business owner, technical owner, run owner e risk owner confirmados.
- [ ] Registry, blueprint e assessments apontam para o mesmo subject/version.

Evidence refs:

## 2. Risk e impact

- [ ] Tier final e rationale aprovados pela authority competente.
- [ ] Assessment identifica método/configuração usada, uncertainty, red flags e limitations.
- [ ] Impact Trigger Screen foi concluído.
- [ ] Impact Assessment completo está referenciado quando houve trigger positivo.
- [ ] Residual risk possui owner, authority, decision, conditions e expiry.
- [ ] Material-change triggers e reassessment path estão definidos.

Evidence refs:

## 3. Dados, identidade e segurança

- [ ] Dados, classificação, origem, retenção e base aplicável registrados.
- [ ] Identidade própria e least privilege validados.
- [ ] Secrets e credenciais usam mecanismo aprovado e rotacionável.
- [ ] Acesso entre domínios, tenants e regiões foi testado.
- [ ] Threat model e riscos de prompt injection/exfiltração foram avaliados.

Evidence refs:

## 4. Tools, autonomia e enforcement

- [ ] Tools possuem classes, scopes, approval mode e limites documentados.
- [ ] Ações state-changing são declaradas e tecnicamente controladas.
- [ ] Ações irreversíveis não dependem apenas de instrução em prompt.
- [ ] Gateway, kill switch, quarantine e rollback foram testados quando aplicáveis.
- [ ] Human accountability boundary está explícita e operacional.

Evidence refs:

## 5. Evaluation e Responsible AI

- [ ] Evaluation suite cobre qualidade, safety e cenários adversariais aplicáveis.
- [ ] Privacy, fairness, transparency, contestability e human oversight foram avaliados conforme contexto/tier.
- [ ] Acceptance criteria, thresholds e limitações estão documentados.
- [ ] Findings abertos possuem disposition, owner e prazo.
- [ ] Affected-party communication e redress estão prontos quando aplicáveis.

Evidence refs:

## 6. Observabilidade, resposta e lifecycle

- [ ] Logs, métricas, alertas e retenção foram validados.
- [ ] Incident owner, escalation path e containment estão operacionais.
- [ ] Support model e handoff para run owner foram aceitos.
- [ ] Attestation, review cadence e triggers de revisão estão definidos.
- [ ] Critérios de suspensão, reativação e sunset estão documentados.

Evidence refs:

## 7. Evidence readiness

- [ ] Evidências têm subject/version, scope, source, timestamp e owner.
- [ ] Missing, failed, not-applicable e pending estão diferenciados.
- [ ] `Not applicable` possui rationale e authority.
- [ ] Contradições e dissent foram preservados.
- [ ] Conditions abertas possuem owner e expiry.

Readiness: `ready` / `ready-with-gaps` / `not-ready`

Gaps e owners:

## 8. Decisão G5 separada

- Gate: `G5`
- Subject/version:
- Scope:
- Decisão: `approve` / `condition` / `hold` / `reject`
- Decision authority:
- Data:
- Rationale:
- Conditions, owners e expiry:
- Residual-risk authority:
- Evidence package:
- Próxima revisão/material-change triggers:
- Decision record ID:

A decisão segue a [policy modular](../docs/governance/policy.md), o [operating model](../docs/governance/operating-model.md) e os [decision gates](../docs/guides/framework-implementation-playbook.md). Readiness, elapsed time ou caixas marcadas não constituem aprovação automática.
