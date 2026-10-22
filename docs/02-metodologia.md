# Metodologia e limites dos testes

[Início](../README.md) · [Anterior: ambiente](01-ambiente.md) · [Próximo: FTP](03-ftp.md)

## Como conduzi os testes

Para cada serviço, comecei por uma senha incorreta e uma credencial conhecida válida. Esses controles permitiram reconhecer as respostas de falha e sucesso antes de interpretar a saída do Medusa. Depois executei uma lista pequena, procurei os eventos no servidor e repeti os testes após as mudanças defensivas.

No FTP e no DVWA, testei cinco senhas para uma conta. No SMB, testei a mesma senha em três contas, demonstrando password spraying em escala reduzida. Usei `-t 1` para limitar a concorrência de logins. As listas incluíam intencionalmente a senha padrão: o objetivo era observar o comportamento dos serviços, não medir quanto tempo levaria para descobrir uma senha desconhecida.

## Critérios de interpretação

No FTP, comparei as respostas `530 Login incorrect` e `230 Login successful` com os registros `FAIL LOGIN` e `OK LOGIN` do servidor. No DVWA, a aplicação retornou HTTP `200` em falhas e sucessos; por isso, observei a mensagem da página e configurei no Medusa o sinal de rejeição `Username and/or password incorrect.`.

A ausência dessa mensagem, isoladamente, poderia ser causada por uma sessão expirada, redirecionamento ou erro. Os controles ajudaram a verificar que o teste estava chegando ao formulário esperado.

No SMB, separei autenticação de autorização. A indicação `ACCOUNT FOUND` precisava ser confrontada com os logs e com uma operação concreta sobre o compartilhamento. Essa verificação foi necessária quando o módulo mencionou `ADMIN$`, mas o cliente não conseguiu listar seu conteúdo.

## Registro das execuções

Usei `script` em parte dos testes FTP e `tee` nas demais coletas. Alguns arquivos contêm o comando completo; outros registram apenas a saída. Os capítulos apresentam os comandos a partir desses registros e das capturas, sem pressupor um histórico integral do terminal.

Para novas senhas, usei `read -r -s`, uma variável de shell e um filtro antes de gravar a saída. Isso evita eco na entrada e remove a senha do registro filtrado. Ainda assim, o valor é expandido nos argumentos do processo durante a execução. O comando `unset` remove a variável da sessão e não desfaz a alteração da senha no serviço.

O filtro `s/(Password: ).*/\1[OCULTA]/` também remove o restante da linha depois do campo, inclusive o sufixo `[SUCCESS]` quando presente. Os controles positivos posteriores mantêm a indicação `ACCOUNT FOUND`.

## Alcance dos resultados

Os testes abrangeram um cliente, um alvo e poucas tentativas. Não houve repetição estatística, teste de carga ou avaliação completa de políticas de bloqueio. Uma senha ficar fora da lista utilizada não demonstra, por si só, resistência a ataques maiores.

As durações totais foram medidas apenas no DVWA High. Nos outros níveis, timestamps iguais ao segundo não significam duração zero. A divergência entre relógios e a presença de navegação anterior nos logs também exigiram selecionar os eventos associados a cada rodada.

Não foram executados testes de exploração de outras falhas do Metasploitable, escalada de privilégios ou movimentação lateral. Os controles defensivos implementados e as propostas de melhoria estão no [capítulo de defesas](06-defesas.md).

## Uso de CWE e CVE

As referências CWE contextualizam o tipo de fraqueza observado. A associação é acompanhada da evidência e de seu alcance: senhas padrão aceitas, tratamento de tentativas no código do DVWA e senhas presentes na URL.

CVE identifica uma vulnerabilidade específica. A identificação de serviços antigos orienta uma pesquisa, mas a versão exibida não confirma todas as condições de um CVE nem demonstra sua exploração. Como este projeto se concentrou em autenticação, não atribuí CVEs ou notas CVSS aos resultados. As fontes utilizadas estão nas [referências](09-referencias.md).
