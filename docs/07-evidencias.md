# Índice das evidências

[Início](../README.md) · [Anterior: defesas](06-defesas.md) · [Próximo: conclusões](08-conclusoes.md)

Os arquivos abaixo registram a execução dos testes e os retestes. Os logs permitem buscar linhas e ler a saída completa; as capturas mostram comandos, telas e configurações. Quando uma tela não cabia na janela da VM, registrei partes numeradas. Algumas linhas se repetem entre prints consecutivos; para contar tentativas, use o arquivo textual da rodada.

## Preparação dos arquivos para publicação

A publicação reúne 66 imagens e 44 arquivos originais de outros tipos, além dos documentos e do verificador. Mantive o conteúdo dos arquivos selecionados, incluindo as saídas já sanitizadas durante a coleta. As novas senhas e os cookies ficam ocultos; as credenciais padrão e as listas didáticas permanecem visíveis.

Excluí `dvwa-low-04-medusa.png` porque o fundo do terminal expunha um cookie. O [log do lote Low](../evidencias/dvwa/low-medusa-lista.txt) continua disponível. Também retirei o TAR de transporte, cujo conteúdo já estava extraído, e a duplicata `dvwa-low-05-acess-log.txt`, idêntica a `dvwa-low-05-access-log.txt`.

Quatro imagens receberam nomes mais simples: `ftp-02-medusa.png.png` passou a `ftp-02-medusa.png`; `ip metasploitable.png` passou a `ambiente-01-ip-metasploitable.png`; `print de ip, versão nmap e versão medusa.png` passou a `ambiente-02-inventario-kali.png`; e `reconhecimento-01-serviços.png` passou a `reconhecimento-01-servicos.png`. Os pixels foram preservados.

## Integridade e transferência

O pacote `evidencias-servidor-dio.tar.gz`, de 4.058 bytes, teve o hash comparado no Metasploitable e no Kali:

```text
4d8412c7d9b8de8281aefda2dca70328bcd45deac0a9de9cdb10afcc57425173
```

Os 13 arquivos do pacote foram conferidos com as cópias extraídas na preparação da documentação; eram idênticos. Uma dessas cópias era a duplicata Low descrita acima. O log FTP do reteste defensivo foi transferido separadamente.

O [SHA256SUMS](../SHA256SUMS) registra os hashes dos arquivos do repositório, exceto o próprio manifesto. O [verificador](../scripts/verificar_integridade.py) confere os itens listados e informa arquivos ausentes ou diferentes. Ele não avalia arquivos adicionais nem certifica a autenticidade histórica dos testes.

## Logs, saídas de ferramentas e listas

### Ambiente

- [inventario-kali.txt](../evidencias/ambiente/inventario-kali.txt)

### Reconhecimento

- [conectividade.txt](../evidencias/reconhecimento/conectividade.txt)
- [servicos-iniciais.gnmap](../evidencias/reconhecimento/servicos-iniciais.gnmap)
- [servicos-iniciais.nmap](../evidencias/reconhecimento/servicos-iniciais.nmap)
- [servicos-iniciais.xml](../evidencias/reconhecimento/servicos-iniciais.xml)

### FTP

- [01-controle-manual.txt](../evidencias/ftp/01-controle-manual.txt)
- [02-medusa.txt](../evidencias/ftp/02-medusa.txt)

### DVWA

- [high-medusa-controle-negativo.txt](../evidencias/dvwa/high-medusa-controle-negativo.txt)
- [high-medusa-lista.txt](../evidencias/dvwa/high-medusa-lista.txt)
- [low-ajuda-web-form.txt](../evidencias/dvwa/low-ajuda-web-form.txt)
- [low-medusa-controle-negativo-publico.txt](../evidencias/dvwa/low-medusa-controle-negativo-publico.txt)
- [low-medusa-lista.txt](../evidencias/dvwa/low-medusa-lista.txt)
- [medium-medusa-controle-negativo.txt](../evidencias/dvwa/medium-medusa-controle-negativo.txt)
- [medium-medusa-lista.txt](../evidencias/dvwa/medium-medusa-lista.txt)

### SMB

- [01-enumeracao-anonima.txt](../evidencias/smb/01-enumeracao-anonima.txt)
- [02-politica-senhas.txt](../evidencias/smb/02-politica-senhas.txt)
- [03-ajuda-smbnt.txt](../evidencias/smb/03-ajuda-smbnt.txt)
- [04-controle-negativo.txt](../evidencias/smb/04-controle-negativo.txt)
- [05-password-spraying.txt](../evidencias/smb/05-password-spraying.txt)
- [06-validacao-admin-share.txt](../evidencias/smb/06-validacao-admin-share.txt)
- [07-identidade-compartilhamento.txt](../evidencias/smb/07-identidade-compartilhamento.txt)
- [12-debug-controle-negativo.txt](../evidencias/smb/12-debug-controle-negativo.txt)
- [13-debug-controle-positivo.txt](../evidencias/smb/13-debug-controle-positivo.txt)

### Retestes defensivos

- [01-smb-enumeracao-apos.txt](../evidencias/defesas/01-smb-enumeracao-apos.txt)
- [02-smb-senha-antiga.txt](../evidencias/defesas/02-smb-senha-antiga.txt)
- [03-smb-senha-nova.txt](../evidencias/defesas/03-smb-senha-nova.txt)
- [04-ftp-lista-apos.txt](../evidencias/defesas/04-ftp-lista-apos.txt)
- [05-ftp-senha-nova.txt](../evidencias/defesas/05-ftp-senha-nova.txt)
- [06-ftp-log-servidor.txt](../evidencias/defesas/06-ftp-log-servidor.txt)

### Registros do servidor

- [dvwa-high-log.txt](../evidencias/servidor/extraidos/dvwa-high-log.txt)
- [dvwa-low-05-access-log.txt](../evidencias/servidor/extraidos/dvwa-low-05-access-log.txt)
- [dvwa-medium-log.txt](../evidencias/servidor/extraidos/dvwa-medium-log.txt)
- [ftp-03-logs-servidor.txt](../evidencias/servidor/extraidos/ftp-03-logs-servidor.txt)
- [smb-auth-resumo.txt](../evidencias/servidor/extraidos/smb-auth-resumo.txt)
- [smb-config-defesa.txt](../evidencias/servidor/extraidos/smb-config-defesa.txt)
- [smb-config.txt](../evidencias/servidor/extraidos/smb-config.txt)
- [smb-debug-antes.txt](../evidencias/servidor/extraidos/smb-debug-antes.txt)
- [smb-debug-depois.txt](../evidencias/servidor/extraidos/smb-debug-depois.txt)
- [smb-debug-durante.txt](../evidencias/servidor/extraidos/smb-debug-durante.txt)
- [smb-log-smbd.txt](../evidencias/servidor/extraidos/smb-log-smbd.txt)
- [smb-validacao-logs.txt](../evidencias/servidor/extraidos/smb-validacao-logs.txt)

### Listas usadas nos testes

- [dvwa-senhas.txt](../wordlists/dvwa-senhas.txt): 5 entradas.
- [ftp-senhas.txt](../wordlists/ftp-senhas.txt): 5 entradas.
- [smb-usuarios.txt](../wordlists/smb-usuarios.txt): 3 entradas.

## Capturas de tela

As séries estão agrupadas por assunto. Os arquivos `parte1`, `parte2` e seguintes devem ser lidos nessa ordem.

### Ambiente

- [ambiente-01-ip-metasploitable.png](../images/ambiente-01-ip-metasploitable.png)
- [ambiente-02-inventario-kali.png](../images/ambiente-02-inventario-kali.png)

### Reconhecimento

- [reconhecimento-01-servicos.png](../images/reconhecimento-01-servicos.png)

### FTP inicial

- [ftp-01-controle-manual.png](../images/ftp-01-controle-manual.png)
- [ftp-02-medusa.png](../images/ftp-02-medusa.png)
- [ftp-03-logs-servidor.png](../images/ftp-03-logs-servidor.png)

### DVWA Low

- [dvwa-low-01-falha.png](../images/dvwa-low-01-falha.png)
- [dvwa-low-02-sucesso.png](../images/dvwa-low-02-sucesso.png)
- [dvwa-low-03-codigo.png](../images/dvwa-low-03-codigo.png)
- [dvwa-low-05-log-parte1.png](../images/dvwa-low-05-log-parte1.png)
- [dvwa-low-05-log-parte2.png](../images/dvwa-low-05-log-parte2.png)
- [dvwa-low-05-log-parte3.png](../images/dvwa-low-05-log-parte3.png)
- [dvwa-low-05-log-parte4.png](../images/dvwa-low-05-log-parte4.png)

### DVWA Medium

- [dvwa-medium-01-codigo.png](../images/dvwa-medium-01-codigo.png)
- [dvwa-medium-02-falha.png](../images/dvwa-medium-02-falha.png)
- [dvwa-medium-03-sucesso.png](../images/dvwa-medium-03-sucesso.png)
- [dvwa-medium-04-controle-negativo.png](../images/dvwa-medium-04-controle-negativo.png)
- [dvwa-medium-05-medusa.png](../images/dvwa-medium-05-medusa.png)
- [dvwa-medium-06-log-parte1.png](../images/dvwa-medium-06-log-parte1.png)
- [dvwa-medium-06-log-parte2.png](../images/dvwa-medium-06-log-parte2.png)
- [dvwa-medium-06-log-parte3.png](../images/dvwa-medium-06-log-parte3.png)

### DVWA High

- [dvwa-high-01-codigo.png](../images/dvwa-high-01-codigo.png)
- [dvwa-high-02-falha.png](../images/dvwa-high-02-falha.png)
- [dvwa-high-03-sucesso.png](../images/dvwa-high-03-sucesso.png)
- [dvwa-high-04-controle-negativo.png](../images/dvwa-high-04-controle-negativo.png)
- [dvwa-high-05-medusa.png](../images/dvwa-high-05-medusa.png)
- [dvwa-high-06-log-parte1.png](../images/dvwa-high-06-log-parte1.png)
- [dvwa-high-06-log-parte2.png](../images/dvwa-high-06-log-parte2.png)
- [dvwa-high-06-log-parte3.png](../images/dvwa-high-06-log-parte3.png)

### SMB e diagnóstico

- [smb-01-enumeracao-anonima.png](../images/smb-01-enumeracao-anonima.png)
- [smb-02-politica-senhas.png](../images/smb-02-politica-senhas.png)
- [smb-04-controle-negativo.png](../images/smb-04-controle-negativo.png)
- [smb-05-password-spraying.png](../images/smb-05-password-spraying.png)
- [smb-06-listagem-negada.png](../images/smb-06-listagem-negada.png)
- [smb-07-erro-rpcclient.png](../images/smb-07-erro-rpcclient.png)
- [smb-08-config-global.png](../images/smb-08-config-global.png)
- [smb-09-log-smbd-parte1.png](../images/smb-09-log-smbd-parte1.png)
- [smb-09-log-smbd-parte2.png](../images/smb-09-log-smbd-parte2.png)
- [smb-09-log-smbd-parte3.png](../images/smb-09-log-smbd-parte3.png)
- [smb-10-debug-antes.png](../images/smb-10-debug-antes.png)
- [smb-11-debug-durante.png](../images/smb-11-debug-durante.png)
- [smb-12-debug-controle-negativo.png](../images/smb-12-debug-controle-negativo.png)
- [smb-13-debug-controle-positivo.png](../images/smb-13-debug-controle-positivo.png)
- [smb-14-log-sucesso-parte1.png](../images/smb-14-log-sucesso-parte1.png)
- [smb-14-log-sucesso-parte2.png](../images/smb-14-log-sucesso-parte2.png)
- [smb-14-log-sucesso-parte3.png](../images/smb-14-log-sucesso-parte3.png)
- [smb-15-relogio-kali.png](../images/smb-15-relogio-kali.png)
- [smb-16-relogio-metasploitable.png](../images/smb-16-relogio-metasploitable.png)
- [smb-17-auth-resumo-parte1.png](../images/smb-17-auth-resumo-parte1.png)
- [smb-17-auth-resumo-parte2.png](../images/smb-17-auth-resumo-parte2.png)
- [smb-17-auth-resumo-parte3.png](../images/smb-17-auth-resumo-parte3.png)
- [smb-18-debug-restaurado.png](../images/smb-18-debug-restaurado.png)

### Defesas SMB

- [defesa-smb-01-edicao.png](../images/defesa-smb-01-edicao.png)
- [defesa-smb-02-validacao.png](../images/defesa-smb-02-validacao.png)
- [defesa-smb-03-enumeracao-negada.png](../images/defesa-smb-03-enumeracao-negada.png)
- [defesa-smb-04-troca-senha.png](../images/defesa-smb-04-troca-senha.png)
- [defesa-smb-05-senha-antiga.png](../images/defesa-smb-05-senha-antiga.png)
- [defesa-smb-06-senha-nova-sucesso.png](../images/defesa-smb-06-senha-nova-sucesso.png)

### Defesas FTP

- [defesa-ftp-01-troca-senha.png](../images/defesa-ftp-01-troca-senha.png)
- [defesa-ftp-02-lista-sem-sucesso.png](../images/defesa-ftp-02-lista-sem-sucesso.png)
- [defesa-ftp-03-senha-nova-sucesso.png](../images/defesa-ftp-03-senha-nova-sucesso.png)
- [defesa-ftp-04-log-servidor.png](../images/defesa-ftp-04-log-servidor.png)
- [defesa-ftp-05-log-no-kali.png](../images/defesa-ftp-05-log-no-kali.png)

### Transferência

- [transferencia-01-hash-metasploitable.png](../images/transferencia-01-hash-metasploitable.png)
- [transferencia-02-download-hash-kali.png](../images/transferencia-02-download-hash-kali.png)
- [transferencia-03-arquivos-extraidos.png](../images/transferencia-03-arquivos-extraidos.png)

