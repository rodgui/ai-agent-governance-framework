# Sources

Registro de fontes primárias usadas pelo framework. Claims temporais devem registrar data de acesso/revisão e ser revalidados conforme o ciclo do artefato.

## Standards, regulation e princípios

| ID | Fonte | Tipo | URL | Acesso | Uso relacionado |
|---|---|---|---|---:|---|
| NIST-001 | AI Risk Management Framework 1.0 | Framework público | <https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf> | 2026-08-09 | Govern, Map, Measure, Manage; lifecycle e governance |
| NIST-002 | Artificial Intelligence Risk Management Framework: Generative Artificial Intelligence Profile (NIST AI 600-1) | Perfil público | <https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf> | 2026-08-09 | GenAI risk, provenance, pre-deployment testing e incident disclosure |
| ISO-001 | ISO/IEC 42001:2023 — Artificial intelligence management system | Norma internacional — página oficial | <https://www.iso.org/standard/81230.html> | 2026-08-09 | AI management system |
| ISO-002 | ISO/IEC 23894:2023 — Guidance on risk management | Norma internacional — página oficial | <https://www.iso.org/standard/77304.html> | 2026-08-09 | AI risk management |
| ISO-003 | ISO/IEC 22989:2022 — AI concepts and terminology | Norma internacional — página oficial | <https://www.iso.org/standard/74296.html> | 2026-08-09 | Terminologia de IA |
| ISO-004 | ISO/IEC 42005:2025 — AI system impact assessment | Norma internacional — página oficial | <https://www.iso.org/standard/42005> | 2026-08-10 | Impact assessment ao longo do lifecycle |
| EU-001 | Regulation (EU) 2024/1689 — Artificial Intelligence Act | Legislação oficial | <https://eur-lex.europa.eu/eli/reg/2024/1689/oj/eng> | 2026-08-09 | Risk management, logging, transparency e human oversight |
| OECD-001 | OECD AI Principles | Princípios intergovernamentais | <https://oecd.ai/en/ai-principles> | 2026-08-09 | Human-centred values, transparency, robustness e accountability |

## Security e threat-informed defense

| ID | Fonte | Tipo | URL | Acesso | Uso relacionado |
|---|---|---|---|---:|---|
| OWASP-001 | Agentic AI — Threats and Mitigations | Guia técnico aberto | <https://genai.owasp.org/resource/agentic-ai-threats-and-mitigations> | 2026-08-09 | Threats, mitigations e agentic security |
| OWASP-002 | OWASP GenAI Security Project | Projeto técnico aberto | <https://owasp.org/www-project-top-10-for-large-language-model-applications/> | 2026-08-09 | LLM, agentic e GenAI application security |
| OWASP-003 | OWASP Top 10 for Agentic Applications 2026 | Guia técnico aberto | <https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/> | 2026-08-10 | Riscos específicos de sistemas agentic e autonomia |
| OWASP-004 | OWASP MCP Top 10 | Projeto técnico aberto | <https://owasp.org/www-project-mcp-top-10/> | 2026-08-10 | Riscos de MCP: misbinding, context spoofing, memória e canais encobertos |
| MITRE-001 | MITRE ATLAS | Knowledge base pública | <https://atlas.mitre.org/> | 2026-08-09 | Threat-informed defense e adversarial techniques |
| CSA-001 | Cloud Security Alliance AI Controls Matrix (AICM) v1.1 | Framework aberto de controles | <https://cloudsecurityalliance.org/artifacts/ai-controls-matrix-v1-1> | 2026-08-10 | Objetivos de controle por domínio e mappings para frameworks de IA |

## Microsoft Customer Zero — application evidence

| ID | Fonte | Tipo | URL | Acesso | Uso relacionado |
|---|---|---|---|---:|---|
| MS-001 | Implementing Agent 365: How we’re governing and managing AI agents at Microsoft | Relato técnico oficial / Customer Zero | <https://www.microsoft.com/insidetrack/blog/implementing-agent-365-how-were-governing-and-managing-ai-agents-at-microsoft/> | 2026-08-09 | Operating model, registry, papéis e observabilidade |
| MS-002 | Deploying Microsoft Agent 365: How we’re extending our infrastructure to manage agents at Microsoft | Relato técnico oficial / Customer Zero | <https://www.microsoft.com/insidetrack/blog/deploying-microsoft-agent-365-how-were-extending-our-infrastructure-to-manage-agents-at-microsoft/> | 2026-08-09 | Control plane, blueprints, telemetria e lifecycle |
| MS-003 | Responsible AI: Why it matters and how we’re infusing it into our internal AI projects at Microsoft | Relato técnico oficial | <https://www.microsoft.com/insidetrack/blog/responsible-ai-why-it-matters-and-how-were-infusing-it-into-our-internal-ai-projects-at-microsoft/> | 2026-08-09 | Responsible AI, impact/release assessment e champions |
| MS-004 | Becoming a Frontier Firm: A guide for deploying AI agents based on our experience at Microsoft | Guia oficial / Customer Zero | <https://www.microsoft.com/insidetrack/blog/becoming-a-frontier-firm-a-guide-for-deploying-ai-agents-based-on-our-experience-at-microsoft/> | 2026-08-09 | Maturidade, adoção, suporte e medição de valor |
| MS-005 | Governing AI agents at scale: Lessons from our journey at Microsoft | Guia oficial / Customer Zero | <https://www.microsoft.com/insidetrack/blog/governing-ai-agents-at-scale-lessons-from-our-journey-at-microsoft/> | 2026-08-09 | Dados AI-ready, matriz de risco, MCP e métricas |

## Hierarquia de evidência

1. legislação, norma e documentação oficial;
2. dados operacionais e system evidence do contexto avaliado;
3. publicações técnicas dos responsáveis pela tecnologia;
4. pesquisa acadêmica ou independente;
5. fontes secundárias reconhecidas;
6. relatos institucionais e opinião.

Hierarquia não elimina análise de atualidade, escopo, conflito de interesse e aplicabilidade.

## Limitações

- Normas ISO completas podem exigir aquisição; as URLs registradas são páginas oficiais, não reprodução do conteúdo protegido. O escopo de cada norma e o motivo de não haver mapeamento control a control estão em [standards de referência](standards/README.md).
- MITRE e OWASP evoluem; mappings devem registrar versão/evidence cutoff.
- Os artigos Microsoft são fontes primárias sobre a abordagem declarada pela empresa e também materiais institucionais. Não constituem auditoria independente nem evidência causal de ROI ou redução de incidentes.
- O framework usa referências para alinhamento; não afirma certificação ou conformidade automática.
