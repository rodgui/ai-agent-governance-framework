# Tools

Automação local e reproduzível do framework.

- [Scripts](scripts/README.md) — renderer e validação do repositório.

Novas categorias de validator ou converter só devem ganhar diretório e índice quando existir um artefato real.

## Regras

- deterministic output quando o input não muda;
- erro explícito, nunca aprovação silenciosa;
- no secrets, telemetry externa ou paths pessoais;
- cross-platform quando viável;
- comando e dependency documentados;
- CI executa o mesmo entry point local.
