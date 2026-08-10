# Template — Checklist de decisão de release

Use antes de qualquer release ou mudança material. Cada item deve ter owner e evidência; marcar uma caixa sem evidence ref não satisfaz o gate.

## 1. Registro e escopo

- [ ] Agent ID, versão e ambientes identificados.
- [ ] Finalidade autorizada, usuários, regiões e usos proibidos registrados.
- [ ] Business owner, technical owner e risk owner confirmados.
- [ ] Registry e blueprint apontam para a mesma versão.

Evidence refs:

## 2. Risk tier e decision rights

- [ ] Tier e rationale aprovados pela autoridade competente.
- [ ] Decision rights e segregation of duties são proporcionais ao risco.
- [ ] Human accountability boundary está explícita.
- [ ] Exceptions possuem owner, prazo e expiry.

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

Evidence refs:

## 5. Evaluation e Responsible AI

- [ ] Evaluation suite cobre qualidade, safety e cenários adversariais aplicáveis.
- [ ] Privacy, fairness, transparency e human oversight foram avaliados conforme o tier.
- [ ] Acceptance criteria, thresholds e limitações estão documentados.
- [ ] Findings abertos possuem disposition, owner e prazo.

Evidence refs:

## 6. Observabilidade, resposta e lifecycle

- [ ] Logs, métricas, alertas e retenção foram validados.
- [ ] Incident owner, escalation path e containment estão operacionais.
- [ ] Attestation, review cadence e triggers de revisão estão definidos.
- [ ] Critérios de suspensão, reativação e sunset estão documentados.

Evidence refs:

## 7. Release disposition

- Gate:
- Decisão: `approved` / `conditional` / `rejected` / `expired`
- Decision authority:
- Data:
- Condições:
- Evidence package:
- Próxima revisão:

A decisão deve seguir a [policy modular](../docs/governance/policy.md), o [operating model](../docs/governance/operating-model.md) e os [decision gates](../docs/guides/framework-implementation-playbook.md). Este checklist não constitui aprovação automática.
