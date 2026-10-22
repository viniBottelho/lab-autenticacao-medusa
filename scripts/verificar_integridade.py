#!/usr/bin/env python3
"""Verifica SHA256SUMS localmente. Não executa operações de rede."""

import hashlib
from pathlib import Path, PurePosixPath
import sys


def main():
    root = Path(__file__).resolve().parent.parent
    manifest = root / "SHA256SUMS"
    if not manifest.is_file():
        print("ERRO: SHA256SUMS não encontrado.")
        return 1
    failed = []
    checked = 0
    seen = set()
    for line_no, line in enumerate(manifest.read_text(encoding="utf-8").splitlines(), 1):
        if not line:
            continue
        try:
            expected, relative = line.split("  ", 1)
            parts = PurePosixPath(relative)
            if (len(expected) != 64 or any(c not in "0123456789abcdef" for c in expected)
                    or parts.is_absolute() or ".." in parts.parts or "\\" in relative
                    or relative in seen or not relative):
                raise ValueError("entrada inválida")
            seen.add(relative)
            file = root.joinpath(*parts.parts)
            file.resolve().relative_to(root)
        except (ValueError, OSError):
            failed.append(f"Linha {line_no}: entrada inválida")
            continue
        if not file.is_file():
            failed.append(f"Ausente: {relative}")
            continue
        digest = hashlib.sha256()
        try:
            with file.open("rb") as stream:
                for block in iter(lambda: stream.read(1024 * 1024), b""):
                    digest.update(block)
        except OSError as exc:
            failed.append(f"Não foi possível ler {relative}: {exc}")
            continue
        checked += 1
        if digest.hexdigest() != expected:
            failed.append(f"Diferente: {relative}")
    if not seen:
        failed.append("Manifesto vazio")
    if failed:
        print("FALHA: a cópia difere do manifesto.")
        print("\n".join(failed))
        return 1
    print(f"OK: {checked} arquivos conferidos com SHA-256.")
    print("Arquivos adicionais não listados não são avaliados.")
    print("O manifesto verifica integridade; não certifica autenticidade histórica.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
