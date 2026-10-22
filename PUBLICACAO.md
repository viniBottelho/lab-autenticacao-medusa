# Como atualizar este repositório

O projeto está publicado em [viniBottelho/lab-autenticacao-medusa](https://github.com/viniBottelho/lab-autenticacao-medusa).

## Atualização pelo navegador

1. Extraia o pacote de atualização no Windows.
2. Abra a pasta extraída até encontrar `README.md`, `PUBLICACAO.md`, `SHA256SUMS` e a pasta `docs`.
3. No GitHub, abra a raiz do repositório e selecione **Add file → Upload files**.
4. Pelo Explorador de Arquivos do Windows, arraste esses três arquivos e a pasta `docs` inteira para a área de upload. Envie o conteúdo da pasta extraída, sem acrescentar outra pasta acima dele.
5. Confira os caminhos: `README.md` deve ficar na raiz e os capítulos em `docs/`.
6. Confirme o commit com a mensagem sugerida abaixo.

```text
Revisa documentação e detalha classificação CWE e mitigações
```

Os arquivos com os mesmos caminhos serão atualizados. Imagens, logs, listas e o script de verificação já estão no repositório e não fazem parte deste pacote de atualização. Não é necessário excluir o repositório ou enviar os 66 prints novamente.

## Conferência após o envio

Abra o README e confira os links para os capítulos. O capítulo de defesas deve apresentar recomendações técnicas, administrativas e formas de verificar os resultados. As referências devem incluir CWE-1393, CWE-307 e CWE-598.

Para verificar os hashes, baixe uma cópia completa do repositório atualizado. Na raiz, execute:

```bash
python3 scripts/verificar_integridade.py
```

O pacote de atualização contém apenas os arquivos alterados; o verificador precisa da cópia completa. O manifesto corresponde aos documentos revisados e às evidências já publicadas. Edições posteriores exigem atualizar os hashes para que a verificação continue passando.

## Novas evidências

Use nomes descritivos e mantenha os caminhos utilizados nos documentos. Revise os novos registros antes de publicar, principalmente cookies, tokens e senhas. A captura `dvwa-low-04-medusa.png` do pacote original foi excluída por expor um cookie ao fundo do terminal e não deve ser reintroduzida.

Guarde os originais em local privado. O `.gitignore` ajuda a evitar inclusões acidentais em um fluxo Git local, mas não remove arquivos já publicados. Nenhuma licença de código aberto foi escolhida automaticamente para este projeto.
