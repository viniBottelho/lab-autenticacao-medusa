# Referências

[Início](../README.md) · [Anterior: conclusões](08-conclusoes.md)

Fontes consultadas em **22 de outubro de 2026**. Os resultados vêm dos registros do laboratório; as referências apoiam a classificação dos achados e as recomendações.

## Classificação das fraquezas

- **MITRE. [CWE-1393: Use of Default Password](https://cwe.mitre.org/data/definitions/1393.html).** Aplicada às senhas padrão aceitas no FTP, SMB e DVWA. É uma especialização da [CWE-1392: Use of Default Credentials](https://cwe.mitre.org/data/definitions/1392.html), mais ampla.
- **MITRE. [CWE-307: Improper Restriction of Excessive Authentication Attempts](https://cwe.mitre.org/data/definitions/307.html).** Apoia a discussão dos controles de tentativas no código e no comportamento do DVWA. O alcance da associação é explicado no capítulo do teste.
- **MITRE. [CWE-598: Use of HTTP Request With Sensitive Query String](https://cwe.mitre.org/data/definitions/598.html).** Aplicada às senhas presentes na URL e nos logs do Apache.

## Autenticação e operação

- **OWASP. [Authentication Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html).** Recomendações para MFA, limitação de tentativas e bloqueio com recuperação.
- **OWASP. [Credential Stuffing Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Credential_Stuffing_Prevention_Cheat_Sheet.html).** Contexto de password spraying e de controles complementares de detecção e prevenção.
- **OWASP. [Logging Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html).** Orientações para registro de eventos, proteção dos logs e exclusão de senhas e tokens.
- **OWASP. [Password Storage Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html).** Apoio à recomendação de substituir o uso de MD5 por armazenamento adequado de senhas em uma aplicação real.

## Ferramentas e configuração

- **Kali Linux. [Medusa](https://www.kali.org/tools/medusa/).** Parâmetros e organização das entradas. A versão usada foi 2.3, conforme o inventário local.
- **Samba. [smb.conf — documentação 3.6](https://www.samba.org/samba/docs/3.6/man-html/smb.conf.5.html).** Contexto de `restrict anonymous` e de acesso de convidado.
- **Samba. [smbcontrol — documentação 3.6](https://www.samba.org/samba/docs/3.6/man-html/smbcontrol.1.html).** Depuração e recarga de configuração.
- **Samba. [smbpasswd — documentação 3.6](https://www.samba.org/samba/docs/3.6/man-html/smbpasswd.8.html).** Alteração de senha no banco do Samba.
- **Python. [http.server](https://docs.python.org/3/library/http.server.html).** Recurso usado na transferência temporária dos arquivos ao Windows.

O alvo executava Samba 3.0.20-Debian. A documentação 3.6 foi usada como apoio, sem pressupor equivalência entre todas as opções das versões. Os registros locais mostram a configuração, os níveis de depuração e o efeito do reteste.

## Referências locais

O [inventário](../evidencias/ambiente/inventario-kali.txt) e o [Nmap](../evidencias/reconhecimento/servicos-iniciais.nmap) registram ferramentas e serviços. A ajuda dos módulos [web-form](../evidencias/dvwa/low-ajuda-web-form.txt) e [smbnt](../evidencias/smb/03-ajuda-smbnt.txt) documenta as opções da instalação utilizada.

As capturas dos códigos [Low](../images/dvwa-low-03-codigo.png), [Medium](../images/dvwa-medium-01-codigo.png) e [High](../images/dvwa-high-01-codigo.png) são a base para comparar o DVWA 1.0.7. A implementação atual do projeto não foi usada como substituta dessa versão histórica. Os demais registros estão no [índice das evidências](07-evidencias.md).
